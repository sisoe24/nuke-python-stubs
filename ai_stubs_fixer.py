"""AI-powered type annotation fixer for Nuke Python stubs.

Reads generated stub files, extracts function signatures and docstrings,
sends them to an LLM (OpenAI, or Ollama) for correction, validates
the output, and applies fixes back to the files.

Usage:
    python ai_stubs_fixer.py [--dry-run] [--file nuke/classes/Node.py]
                              [--stubs-path PATH] [--provider openai|openai-batch|ollama]
                              [--model MODEL] [--base-url URL] [--api-key KEY]
                              [--exclude FOLDER [FOLDER ...]] [--verbose]

Integration:
    from ai_stubs_fixer import ai_post_fixes
    ai_post_fixes(stubs_path, provider="openai")
"""
from __future__ import annotations

import ast
import json
import logging
import pathlib
import random
import re
import time
import argparse
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


STUBS_PATH = pathlib.Path.home() / '.nuke' / 'NukeTools' / 'stubs'
CHANGE_LOG_PATH = STUBS_PATH.parent / 'ai_fixer_changes.json'

MAX_FUNCTIONS_PER_BATCH = 50
RATE_LIMIT_DELAY = 1.0
BACKOFF_SECONDS = 30
MAX_API_RETRIES = 3

SYSTEM_PROMPT = """\
You are a Python type stub expert for the Nuke VFX application API.
You will receive a JSON list of Python function stubs with their current signatures
and docstrings. Your task is to correct incorrect type annotations.

Use the following priority order:

1. DOCUMENTATION FIRST: Check the full docstring carefully.
   - If @return: is present, its described type is authoritative.
   - If @param <name>: is present, use it for parameter types.
   - Cross-reference the function name and parameter names against
     the docstring to confirm the annotation makes sense.
   - If the docstring description and @return: tag conflict, prefer @return:.

2. BEST GUESS: If no docstring or the docstring is ambiguous,
   infer from the function name and parameter names:
   - "get*", "find*", "create*" -> likely returns the named type or None
   - "is*", "has*", "can*" -> likely returns bool
   - "count", "num*", "len*", "size*" -> likely returns int
   - Setters / "set*" -> likely returns None

3. Known dunder corrections (apply unless docstring contradicts):
   __new__                                 -> Self (or the class name)
   __repr__, __str__                       -> str
   __hash__, __len__, __sizeof__           -> int
   __bool__, __contains__                  -> bool
   __eq__, __ne__, __lt__, __le__, __gt__, __ge__ -> bool
   __getitem__, __setitem__                -> depends on docstring

4. Other rules:
   - Replace `int | float` with `int` for counts, indices, or lengths
   - Replace `-> None` with the specific type when @return: describes a value
   - Replace `-> Any` with a specific type when docstring names a concrete type
   - Preserve the exact parameter names; only add/fix type annotations
   - Keep `self` as the first parameter for instance methods
   - Do NOT add imports; only use types already in scope (typing, nuke classes)

Return ONLY a valid JSON array. No markdown, no prose, no code fences.
Each element must have exactly these fields:
  "function_name": str
  "class_name": str or null
  "corrected_signature": str  (complete def line ending with ":")
  "confidence": "high" | "medium" | "low"
  "reasoning": str (one sentence)
  "changed": bool

Only include entries where "changed" is true.
If nothing needs changing, return an empty array: []
"""

DATASET_SYSTEM_PROMPT = """\
You are a Python type annotation expert specializing in VFX software APIs (Nuke, Hiero).
Add the most accurate type annotations to Python functions, methods, and classes
based on all available evidence: parameter names, function names, docstrings, return
behavior, and surrounding context.

Rules:
- Use conservative inference. Prefer `Any` over a wrong confident type.
- Use modern Python 3.10+ syntax unless the file already uses legacy typing imports.
- Never invent types that are not implied by the code.
- Always annotate return types, even if `-> None`.
- Use `X | None` instead of `Optional[X]`.
- Use built-in generics: `list[str]`, `dict[str, int]`, not `List`, `Dict`.
- For `*args`/`**kwargs` without docstring evidence, annotate as `Any`.
- For bare `list` returns: use docstring context to determine element type; fallback to `list[Any]`.
- Keep `self` and `cls` unannotated.
- Keep method bodies as `...`.
- Output the annotated code block followed by a <rationale> section explaining each
  type decision as a bullet point. Mention alternatives considered and why they were rejected.
"""

DATASET_SYSTEM_PROMPT_STUB_ONLY = """\
You are a Python type stub engineer specializing in VFX software APIs (Nuke, Hiero).
Given Python code with missing or incomplete type annotations, produce a .pyi-style stub:
function signatures with precise type annotations and `...` as the body.

Rules:
- Use modern Python 3.10+ syntax (`X | None`, `list[T]`, `dict[K, V]`).
- Prefer `Any` over a wrong guess when evidence is insufficient.
- Keep `self` and `cls` unannotated.
- Output the annotated stub code block followed by a <rationale> section explaining
  each annotation decision as a bullet point.
"""


@dataclass
class FunctionInfo:
    name: str
    class_name: str | None
    current_signature: str
    docstring: str
    line_number: int
    file_path: pathlib.Path


@dataclass
class CorrectionPayload:
    function_name: str
    class_name: str | None
    corrected_signature: str
    confidence: str
    reasoning: str
    changed: bool = True


@dataclass
class FileCorrections:
    file_path: pathlib.Path
    corrections: list[CorrectionPayload] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------

class StubFileParser:
    """Extract FunctionInfo entries from a stub .py file using the AST."""

    def __init__(self, file_path: pathlib.Path):
        self.file_path = file_path
        self._source = file_path.read_text(encoding='utf-8')
        self._lines = self._source.splitlines()
        self._tree = ast.parse(self._source, filename=str(file_path))

    def extract_functions(self) -> list[FunctionInfo]:
        results: list[FunctionInfo] = []
        for node in ast.iter_child_nodes(self._tree):
            if isinstance(node, ast.ClassDef):
                for child in ast.iter_child_nodes(node):
                    if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        info = self._make_info(child, node.name)
                        if info:
                            results.append(info)
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                info = self._make_info(node, class_name=None)
                if info:
                    results.append(info)
        return results

    def _make_info(
        self,
        node: ast.FunctionDef | ast.AsyncFunctionDef,
        class_name: str | None,
    ) -> FunctionInfo | None:
        docstring = ast.get_docstring(node) or ''
        sig = self._extract_signature(node)
        return FunctionInfo(
            name=node.name,
            class_name=class_name,
            current_signature=sig,
            docstring=docstring,
            line_number=node.lineno,
            file_path=self.file_path,
        )

    def _extract_signature(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
        """Extract the raw def line(s) from the source."""
        start = node.lineno - 1  # 0-indexed
        # Find where the def header ends (the line ending with ':')
        end = start
        for i in range(start, min(start + 20, len(self._lines))):
            if self._lines[i].rstrip().endswith(':'):
                end = i
                break
        return '\n'.join(self._lines[start:end + 1])


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def _validate_correction(item: dict) -> bool:
    """Return True if the correction item is structurally safe to apply."""
    sig = item.get('corrected_signature', '')
    stripped = sig.strip()
    if not stripped.startswith('def ') and not stripped.startswith('async def '):
        return False
    if not stripped.rstrip().endswith(':'):
        return False
    # Must be parseable as Python
    try:
        ast.parse(stripped + '\n    ...')
    except SyntaxError:
        return False
    return True


# ---------------------------------------------------------------------------
# Providers (abstract base + concrete implementations)
# ---------------------------------------------------------------------------

class BaseAnnotationFixer(ABC):
    """Provider-agnostic base that handles batching and throttling."""

    MAX_BATCH = MAX_FUNCTIONS_PER_BATCH
    DELAY = RATE_LIMIT_DELAY

    def __init__(self, model: str | None, logger: logging.Logger):
        self.model = model
        self.logger = logger

    def fix_file(self, functions: list[FunctionInfo]) -> list[CorrectionPayload]:
        all_corrections: list[CorrectionPayload] = []
        batches = [functions[i:i + self.MAX_BATCH] for i in range(0, len(functions), self.MAX_BATCH)]
        for batch in batches:
            corrections = self._call_with_retry(batch)
            all_corrections.extend(corrections)
            if len(batches) > 1:
                time.sleep(self.DELAY)
        return all_corrections

    def _call_with_retry(self, functions: list[FunctionInfo]) -> list[CorrectionPayload]:
        for attempt in range(1, MAX_API_RETRIES + 1):
            try:
                return self._call_api(functions)
            except Exception as exc:
                if self._is_rate_limit(exc) and attempt < MAX_API_RETRIES:
                    self.logger.warning('Rate limit hit, backing off %ds (attempt %d/%d)',
                                        BACKOFF_SECONDS, attempt, MAX_API_RETRIES)
                    time.sleep(BACKOFF_SECONDS)
                elif attempt == MAX_API_RETRIES:
                    self.logger.error('API call failed after %d attempts: %s', MAX_API_RETRIES, exc)
                    return []
                else:
                    self.logger.error('API error: %s', exc)
                    return []
        return []

    @abstractmethod
    def _call_api(self, functions: list[FunctionInfo]) -> list[CorrectionPayload]: ...

    @staticmethod
    def _is_rate_limit(exc: Exception) -> bool:
        name = type(exc).__name__.lower()
        msg = str(exc).lower()
        return 'ratelimit' in name or '429' in msg or 'rate limit' in msg

    def _build_user_prompt(self, functions: list[FunctionInfo]) -> str:
        file_name = functions[0].file_path.name if functions else 'unknown'
        class_ctx = functions[0].class_name if functions and functions[0].class_name else 'module-level'
        items = [
            {
                'name': f.name,
                'class_name': f.class_name,
                'current_signature': f.current_signature,
                'docstring': f.docstring,
            }
            for f in functions
        ]
        return (
            f'File: {file_name}\n'
            f'Class context: {class_ctx}\n\n'
            f'Fix the type annotations for these {len(functions)} functions.\n'
            f'Return a JSON array. Only include entries where "changed" is true.\n\n'
            f'{json.dumps(items, indent=2)}'
        )

    def _parse_response(self, text: str) -> list[CorrectionPayload]:
        """Parse and validate the JSON response from the LLM."""
        raw: list[dict] = []
        try:
            raw = json.loads(text)
        except json.JSONDecodeError:
            match = re.search(r'\[.*\]', text, re.DOTALL)
            if match:
                try:
                    raw = json.loads(match.group())
                except json.JSONDecodeError:
                    self.logger.warning('Could not parse LLM response as JSON')
                    return []
            else:
                self.logger.warning('No JSON array found in LLM response')
                return []

        if not isinstance(raw, list):
            self.logger.warning('LLM response was not a JSON array')
            return []

        corrections: list[CorrectionPayload] = []
        for item in raw:
            if not isinstance(item, dict):
                continue
            if not item.get('changed', False):
                continue
            if not _validate_correction(item):
                self.logger.debug('Rejected invalid correction: %s', item.get('corrected_signature', ''))
                continue
            try:
                corrections.append(CorrectionPayload(
                    function_name=item['function_name'],
                    class_name=item.get('class_name'),
                    corrected_signature=item['corrected_signature'],
                    confidence=item.get('confidence', 'medium'),
                    reasoning=item.get('reasoning', ''),
                    changed=True,
                ))
            except KeyError as e:
                self.logger.debug('Missing key in correction item: %s', e)
        return corrections


class OpenAIFixer(BaseAnnotationFixer):
    """Fixer using the OpenAI API."""

    DEFAULT_MODEL = 'gpt-4o'

    def __init__(self, model: str | None = None, api_key: str | None = None,
                 base_url: str | None = None, logger: logging.Logger | None = None):
        super().__init__(model or self.DEFAULT_MODEL, logger or logging.getLogger(__name__))
        try:
            import openai as _openai
        except ImportError as e:
            raise ImportError(
                'openai package is required for the openai provider. '
                'Install it with: pip install openai'
            ) from e
        kwargs: dict = {}
        if api_key:
            kwargs['api_key'] = api_key
        if base_url:
            kwargs['base_url'] = base_url
        self._client = _openai.OpenAI(**kwargs)

    def _call_api(self, functions: list[FunctionInfo]) -> list[CorrectionPayload]:
        response = self._client.chat.completions.create(
            model=self.model,
            messages=[
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': self._build_user_prompt(functions)},
            ],
            max_tokens=4096,
        )
        return self._parse_response(response.choices[0].message.content or '')


class OllamaFixer(BaseAnnotationFixer):
    """Fixer using a local Ollama server (OpenAI-compatible API)."""

    DEFAULT_MODEL = 'llama3'
    DEFAULT_BASE_URL = 'http://localhost:11434/v1'
    DELAY = 0.0  # local server, no rate limiting needed

    def __init__(self, model: str | None = None, base_url: str | None = None,
                 logger: logging.Logger | None = None):
        super().__init__(model or self.DEFAULT_MODEL, logger or logging.getLogger(__name__))
        try:
            import openai as _openai
        except ImportError as e:
            raise ImportError(
                'openai package is required for the ollama provider (uses OpenAI-compatible API). '
                'Install it with: pip install openai'
            ) from e
        self._client = _openai.OpenAI(
            base_url=base_url or self.DEFAULT_BASE_URL,
            api_key='ollama',
        )

    def _call_api(self, functions: list[FunctionInfo]) -> list[CorrectionPayload]:
        response = self._client.chat.completions.create(
            model=self.model,
            messages=[
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': self._build_user_prompt(functions)},
            ],
        )
        return self._parse_response(response.choices[0].message.content or '')


class OpenAIBatchFixer(BaseAnnotationFixer):
    """OpenAI fixer using the Batch API — async, 50% cheaper than synchronous calls.

    Instead of making one API call per file/batch, this fixer:
    1. Queues all requests from all files into a single JSONL payload.
    2. Uploads it and submits one Batch job.
    3. Polls until the job completes (up to 24 h, typically minutes).
    4. Returns all results mapped back via custom_id.

    Use via provider='openai-batch' or by calling queue_file()/flush_batch() directly.
    Not compatible with base-url overrides (Batch API is OpenAI-hosted only).
    """

    DEFAULT_MODEL = 'gpt-5-mini'
    POLL_INTERVAL_START = 10   # seconds between first status checks
    POLL_INTERVAL_MAX = 60     # cap poll interval at 60 s

    def __init__(
        self,
        model: str | None = None,
        api_key: str | None = None,
        max_tokens: int | None = None,
        logger: logging.Logger | None = None,
    ):
        super().__init__(model or self.DEFAULT_MODEL, logger or logging.getLogger(__name__))
        try:
            import openai as _openai
        except ImportError as e:
            raise ImportError(
                'openai package is required for the openai-batch provider. '
                'Install it with: pip install openai'
            ) from e
        self._client = _openai.OpenAI(api_key=api_key)
        # max_tokens is intentionally optional — not all models support it.
        # None means the field is omitted from each batch request body entirely.
        self._max_tokens = max_tokens
        # Accumulates (custom_id, user_prompt) pairs across all queued files.
        self._queue: list[tuple[str, str]] = []

    # _call_api is not used in batch mode; the orchestrator calls queue_file + flush_batch.
    def _call_api(self, functions: list[FunctionInfo]) -> list[CorrectionPayload]:
        raise NotImplementedError('OpenAIBatchFixer uses queue_file() + flush_batch()')

    def queue_file(self, file_path: pathlib.Path, functions: list[FunctionInfo]) -> list[str]:
        """Enqueue all function batches for one file.

        Returns the list of custom_ids assigned to this file's batches,
        which the orchestrator uses to retrieve results after flush_batch().
        """
        rel = str(file_path)
        batches = [functions[i:i + self.MAX_BATCH]
                   for i in range(0, len(functions), self.MAX_BATCH)]
        ids: list[str] = []
        for idx, batch in enumerate(batches):
            custom_id = f'{rel}::b{idx}'
            self._queue.append((custom_id, self._build_user_prompt(batch)))
            ids.append(custom_id)
        return ids

    def flush_batch(self) -> dict[str, list[CorrectionPayload]]:
        """Upload all queued requests, wait for the batch to finish, return results.

        Returns a dict mapping each custom_id to its list of CorrectionPayload objects.
        An empty list for a given custom_id means the request failed or returned nothing.
        """
        if not self._queue:
            return {}

        # Build JSONL payload — one line per queued request.
        lines: list[str] = []
        for custom_id, user_prompt in self._queue:
            body: dict = {
                'model': self.model,
                'messages': [
                    {'role': 'system', 'content': SYSTEM_PROMPT},
                    {'role': 'user',   'content': user_prompt},
                ],
            }
            if self._max_tokens is not None:
                body['max_tokens'] = self._max_tokens
            lines.append(json.dumps({
                'custom_id': custom_id,
                'method': 'POST',
                'url': '/v1/chat/completions',
                'body': body,
            }))
        jsonl_bytes = '\n'.join(lines).encode()

        # Upload the input file.
        self.logger.info('Uploading batch input (%d requests)...', len(self._queue))
        uploaded = self._client.files.create(
            file=('batch_input.jsonl', jsonl_bytes, 'application/jsonl'),
            purpose='batch',
        )

        # Submit the batch job.
        batch_job = self._client.batches.create(
            input_file_id=uploaded.id,
            endpoint='/v1/chat/completions',
            completion_window='24h',
        )
        self.logger.info('Batch job submitted: %s', batch_job.id)

        # Poll until the job reaches a terminal state.
        interval = float(self.POLL_INTERVAL_START)
        while True:
            batch_job = self._client.batches.retrieve(batch_job.id)
            counts = batch_job.request_counts
            self.logger.info(
                'Batch %s: status=%s  completed=%s/%s  failed=%s',
                batch_job.id, batch_job.status,
                getattr(counts, 'completed', '?'),
                getattr(counts, 'total', '?'),
                getattr(counts, 'failed', '?'),
            )
            if batch_job.status in ('completed', 'failed', 'expired', 'cancelled'):
                break
            time.sleep(interval)
            interval = min(interval * 1.5, self.POLL_INTERVAL_MAX)

        if batch_job.status != 'completed':
            self.logger.error('Batch job did not complete successfully: status=%s', batch_job.status)
            return {}

        # Download and parse the output JSONL.
        raw = self._client.files.content(batch_job.output_file_id).content
        results: dict[str, list[CorrectionPayload]] = {}
        for line in raw.decode().splitlines():
            if not line.strip():
                continue
            entry = json.loads(line)
            custom_id = entry['custom_id']
            if entry.get('error'):
                self.logger.warning('Batch request %s failed: %s', custom_id, entry['error'])
                results[custom_id] = []
                continue
            content = (
                entry.get('response', {})
                     .get('body', {})
                     .get('choices', [{}])[0]
                     .get('message', {})
                     .get('content') or ''
            )
            results[custom_id] = self._parse_response(content)

        # Clean up the uploaded input file to avoid storage accumulation.
        try:
            self._client.files.delete(uploaded.id)
        except Exception:
            pass

        return results


def create_fixer(
    provider: str,
    model: str | None = None,
    api_key: str | None = None,
    base_url: str | None = None,
    logger: logging.Logger | None = None,
) -> BaseAnnotationFixer:
    """Factory: create the right fixer for the given provider name."""
    match provider:
        case 'openai':
            return OpenAIFixer(model, api_key, base_url, logger)
        case 'ollama':
            return OllamaFixer(model, base_url, logger)
        case 'openai-batch':
            return OpenAIBatchFixer(model=model, api_key=api_key, logger=logger)
        case _:
            raise ValueError(
                f"Unknown provider {provider!r}. "
                f"Choose from: openai, openai-batch, ollama"
            )


# ---------------------------------------------------------------------------
# Applicator
# ---------------------------------------------------------------------------

class CorrectionApplicator:
    """Apply a list of CorrectionPayload objects back to a stub file."""

    def __init__(self, file_path: pathlib.Path, dry_run: bool = False,
                 logger: logging.Logger | None = None):
        self.file_path = file_path
        self.dry_run = dry_run
        self.logger = logger or logging.getLogger(__name__)

    def apply(
        self,
        corrections: list[CorrectionPayload],
        function_infos: list[FunctionInfo],
    ) -> list[dict]:
        if not corrections:
            return []

        # Build lookup by (function_name, class_name)
        info_map: dict[tuple[str, str | None], FunctionInfo] = {
            (f.name, f.class_name): f for f in function_infos
        }

        lines = self.file_path.read_text(encoding='utf-8').splitlines(keepends=True)
        applied: list[dict] = []

        # Process in reverse line order to avoid line-shift issues
        sorted_corrections = sorted(
            corrections,
            key=lambda c: info_map.get((c.function_name, c.class_name),
                                       FunctionInfo('', None, '', '', 0, self.file_path)).line_number,
            reverse=True,
        )

        for correction in sorted_corrections:
            key = (correction.function_name, correction.class_name)
            info = info_map.get(key)
            if not info:
                self.logger.debug('No location found for %s (class=%s)', *key)
                continue

            start_idx = info.line_number - 1  # 0-indexed
            end_idx = self._find_def_end(lines, start_idx)
            old_text = ''.join(lines[start_idx:end_idx + 1])

            # Safety check: verify current source matches what we extracted
            if old_text.strip() != info.current_signature.strip():
                self.logger.debug(
                    'Signature mismatch for %s, skipping (source may have changed)', info.name
                )
                continue

            new_sig = self._match_indentation(old_text, correction.corrected_signature)
            if not new_sig.endswith('\n'):
                new_sig += '\n'

            applied.append({
                'file': str(self.file_path),
                'function': correction.function_name,
                'class': correction.class_name,
                'old': old_text.rstrip(),
                'new': new_sig.rstrip(),
                'confidence': correction.confidence,
                'reasoning': correction.reasoning,
            })

            if not self.dry_run:
                lines[start_idx:end_idx + 1] = [new_sig]

        if not self.dry_run and applied:
            self.file_path.write_text(''.join(lines), encoding='utf-8')

        return applied

    @staticmethod
    def _find_def_end(lines: list[str], start: int) -> int:
        """Return the 0-indexed last line of a def statement (handles multi-line sigs)."""
        for i in range(start, min(start + 20, len(lines))):
            if lines[i].rstrip().endswith(':'):
                return i
        return start

    @staticmethod
    def _match_indentation(original: str, new_sig: str) -> str:
        """Preserve the indentation level of original in new_sig."""
        stripped = original.lstrip()
        indent = original[:len(original) - len(stripped)]
        return indent + new_sig.lstrip()


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

class StubsFixerOrchestrator:
    """Coordinate extraction → fixing → application across all stub files."""

    def __init__(
        self,
        stubs_path: pathlib.Path,
        fixer: BaseAnnotationFixer,
        dry_run: bool = False,
        file_filter: str | None = None,
        exclude: list[str] | None = None,
        logger: logging.Logger | None = None,
    ):
        self.stubs_path = stubs_path
        self.fixer = fixer
        self.dry_run = dry_run
        self.file_filter = file_filter
        self.exclude: set[str] = set(exclude or [])
        self.logger = logger or logging.getLogger(__name__)
        self.change_log: list[dict] = []

    def run(self) -> list[dict]:
        if isinstance(self.fixer, OpenAIBatchFixer):
            return self.run_batch()

        files = self._collect_files()
        if not files:
            self.logger.warning('No stub files found under %s', self.stubs_path)
            return []

        self.logger.info('AI stub fixer: processing %d file(s) [dry_run=%s]', len(files), self.dry_run)

        for file_path in files:
            self._process_file(file_path)

        self._write_change_log()
        self.logger.info('AI stub fixer done. %d correction(s) applied.', len(self.change_log))
        return self.change_log

    def run_batch(self) -> list[dict]:
        """Run using the OpenAI Batch API: parse all files, submit one job, apply results."""
        if not isinstance(self.fixer, OpenAIBatchFixer):
            raise TypeError('run_batch() requires an OpenAIBatchFixer instance')

        files = self._collect_files()
        if not files:
            self.logger.warning('No stub files found under %s', self.stubs_path)
            return []

        # Phase 1 — parse every file and enqueue its batches.
        # file_data maps each file to (documented_functions, [custom_ids])
        file_data: dict[pathlib.Path, tuple[list[FunctionInfo], list[str]]] = {}
        for file_path in files:
            try:
                funcs = StubFileParser(file_path).extract_functions()
            except SyntaxError as exc:
                self.logger.error('Syntax error in %s: %s', file_path.name, exc)
                continue
            with_docs = [f for f in funcs if f.docstring.strip()]
            if not with_docs:
                self.logger.debug('No documented functions in %s, skipping', file_path.name)
                continue
            custom_ids = self.fixer.queue_file(file_path, with_docs)
            file_data[file_path] = (with_docs, custom_ids)

        self.logger.info(
            'AI stub fixer (batch): %d file(s) queued, %d total request(s) [dry_run=%s]',
            len(file_data), len(self.fixer._queue), self.dry_run,
        )

        # Phase 2 — submit the batch and wait for all results.
        results_by_id = self.fixer.flush_batch()

        # Phase 3 — apply corrections file by file.
        for file_path, (with_docs, custom_ids) in file_data.items():
            corrections: list[CorrectionPayload] = []
            for cid in custom_ids:
                corrections.extend(results_by_id.get(cid, []))
            if not corrections:
                continue
            applicator = CorrectionApplicator(file_path, self.dry_run, self.logger)
            changes = applicator.apply(corrections, with_docs)
            self.change_log.extend(changes)
            if changes:
                rel = file_path.relative_to(self.stubs_path)
                self.logger.info('  %d correction(s) in %s', len(changes), rel)

        self._write_change_log()
        self.logger.info('AI stub fixer done. %d correction(s) applied.', len(self.change_log))
        return self.change_log

    def _collect_files(self) -> list[pathlib.Path]:
        if self.file_filter:
            candidate = self.stubs_path / self.file_filter
            if not candidate.exists():
                raise FileNotFoundError(f'File not found: {candidate}')
            return [candidate]

        all_files = sorted(self.stubs_path.glob('**/*.py'))

        if not self.exclude:
            return all_files

        # Filter out any file whose relative path contains an excluded folder name
        filtered: list[pathlib.Path] = []
        skipped_dirs: set[str] = set()
        for file_path in all_files:
            rel = file_path.relative_to(self.stubs_path)
            excluded_by = next(
                (ex for ex in self.exclude if ex in rel.parts), None
            )
            if excluded_by:
                skipped_dirs.add(excluded_by)
            else:
                filtered.append(file_path)

        for d in sorted(skipped_dirs):
            self.logger.info('  Excluding folder: %s', d)

        return filtered

    def _process_file(self, file_path: pathlib.Path) -> None:
        rel = file_path.relative_to(self.stubs_path)
        self.logger.info('  Processing: %s', rel)
        try:
            parser = StubFileParser(file_path)
            functions = parser.extract_functions()
        except SyntaxError as exc:
            self.logger.error('  Syntax error in %s: %s', rel, exc)
            return

        if not functions:
            return

        # Only send functions that have a docstring (primary signal)
        with_docs = [f for f in functions if f.docstring.strip()]
        if not with_docs:
            self.logger.debug('  No documented functions in %s, skipping', rel)
            return

        corrections = self.fixer.fix_file(with_docs)
        if not corrections:
            return

        applicator = CorrectionApplicator(file_path, self.dry_run, self.logger)
        changes = applicator.apply(corrections, with_docs)
        self.change_log.extend(changes)

        if changes:
            self.logger.info('  %d correction(s) in %s', len(changes), rel)

    def _write_change_log(self) -> None:
        log_path = self.stubs_path.parent / 'ai_fixer_changes.json'
        try:
            log_path.write_text(json.dumps(self.change_log, indent=2), encoding='utf-8')
            self.logger.info('Change log: %s', log_path)
        except OSError as exc:
            self.logger.warning('Could not write change log: %s', exc)


# ---------------------------------------------------------------------------
# Public integration entry point
# ---------------------------------------------------------------------------

def ai_post_fixes(
    stubs_path: pathlib.Path = STUBS_PATH,
    dry_run: bool = False,
    file_filter: str | None = None,
    exclude: list[str] | None = None,
    provider: str = 'openai-batch',
    model: str | None = None,
    api_key: str | None = None,
    base_url: str | None = None,
    logger: logging.Logger | None = None,
) -> list[dict]:
    """Run AI-powered annotation fixes on generated stubs.

    This is the integration entry point for nukestubsgen.py.
    API keys are read from environment variables if not provided explicitly:
      - OpenAI:    OPENAI_API_KEY

    Args:
        stubs_path:  Path to the stubs directory.
        dry_run:     If True, propose changes without writing files.
        file_filter: Relative path to a single file (e.g. 'nuke/classes/Node.py').
        exclude:     List of folder names to skip (e.g. ['nuke_internal', 'nukescripts']).
                     Matched against each path component, so 'nuke_internal' skips
                     every file anywhere under a directory named 'nuke_internal'.
        provider:    'openai', 'openai-batch', or 'ollama'.
                     'openai-batch' collects all requests and submits them as a single
                     OpenAI Batch API job (async, 50% cost reduction, ~minutes wait).
        model:       Override the default model for the chosen provider.
        api_key:     Override the environment-variable API key.
        base_url:    Ollama server base URL (default: http://localhost:11434/v1).
        logger:      Optional logger; creates a default one if not provided.

    Returns:
        List of applied-correction dicts (each has file, function, old, new, reasoning).
    """
    _logger = logger or _make_logger()
    fixer = create_fixer(provider, model, api_key, base_url, _logger)
    orchestrator = StubsFixerOrchestrator(stubs_path, fixer, dry_run, file_filter, exclude, _logger)
    return orchestrator.run()


# ---------------------------------------------------------------------------
# Logging helper
# ---------------------------------------------------------------------------

def _make_logger(verbose: bool = False) -> logging.Logger:
    logger = logging.getLogger('ai_stubs_fixer')
    if logger.handlers:
        return logger
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG if verbose else logging.INFO)
    handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
    logger.addHandler(handler)
    logger.propagate = False
    return logger


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='ai_stubs_fixer.py',
        description='AI-powered type annotation tools for Nuke Python stubs.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest='command', metavar='COMMAND')
    subparsers.required = True

    # -- fix subcommand -------------------------------------------------------
    fix_parser = subparsers.add_parser(
        'fix',
        help='Apply AI type-annotation fixes to stub files.',
        description='Use an LLM to correct type annotations in Nuke/Hiero stub files.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dry-run on a single file
  python ai_stubs_fixer.py fix --dry-run --file nuke/classes/Node.py

  # Fix all files using OpenAI (synchronous)
  python ai_stubs_fixer.py fix --provider openai --model gpt-4o

  # Fix all files using OpenAI Batch API (async, 50% cheaper)
  python ai_stubs_fixer.py fix --provider openai-batch

  # Fix using local Ollama
  python ai_stubs_fixer.py fix --provider ollama --model llama3

  # Specify a custom stubs path
  python ai_stubs_fixer.py fix --stubs-path /path/to/stubs
        """,
    )
    fix_parser.add_argument(
        '--dry-run', action='store_true',
        help='Show proposed changes without writing to files.',
    )
    fix_parser.add_argument(
        '--file', default=None, metavar='PATH',
        help='Process a single file (relative to --stubs-path).',
    )
    fix_parser.add_argument(
        '--stubs-path', type=pathlib.Path, default=STUBS_PATH, metavar='PATH',
        help=f'Path to the stubs directory (default: {STUBS_PATH}).',
    )
    fix_parser.add_argument(
        '--provider', default='openai-batch',
        choices=['openai', 'openai-batch', 'ollama'],
        help=(
            'AI provider to use (default: openai). '
            "'openai-batch' submits one async Batch API job (50% cheaper, ~minutes wait)."
        ),
    )
    fix_parser.add_argument(
        '--model', default='gpt-5-mini',
        help='Model name override. Defaults: openai=gpt-5-mini, ollama=llama3.',
    )
    fix_parser.add_argument(
        '--base-url', default=None, metavar='URL',
        help='Base URL for Ollama server (default: http://localhost:11434/v1).',
    )
    fix_parser.add_argument(
        '--api-key', default=None, metavar='KEY',
        help='API key override (default: read from environment variable).',
    )
    fix_parser.add_argument(
        '--exclude', nargs='+', default=None, metavar='FOLDER',
        help=(
            'One or more folder names to skip entirely '
            '(e.g. --exclude nuke_internal nukescripts). '
            'Matched against each path component of every discovered file.'
        ),
    )
    fix_parser.add_argument(
        '--verbose', action='store_true',
        help='Enable debug logging.',
    )
    fix_parser.set_defaults(func=_run_fixer)

    # -- generate-dataset subcommand ------------------------------------------
    gen_parser = subparsers.add_parser(
        'generate-dataset',
        help='Generate JSONL fine-tuning data from stub files via OpenAI API.',
        description='Generate JSONL fine-tuning data from Nuke/Hiero stub files via OpenAI API.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate up to 500 examples using default model
  python ai_stubs_fixer.py generate-dataset --stubs-dir stubs/ --output data.jsonl

  # Limit scope, use a specific model, exclude internal modules
  python ai_stubs_fixer.py generate-dataset \\
      --stubs-dir stubs/ --output data.jsonl \\
      --max-examples 200 --model gpt-4.1-mini \\
      --exclude nuke_internal ocionuke --verbose
        """,
    )
    gen_parser.add_argument(
        '--stubs-dir', type=pathlib.Path, default=pathlib.Path('stubs'),
        metavar='PATH', help='Root of the stubs directory (default: stubs/).',
    )
    gen_parser.add_argument(
        '--output', type=pathlib.Path, default=pathlib.Path('training_data.jsonl'),
        metavar='FILE', help='Output JSONL file (default: training_data.jsonl).',
    )
    gen_parser.add_argument(
        '--max-examples', type=int, default=500, metavar='N',
        help='Maximum number of training examples to generate (default: 500).',
    )
    gen_parser.add_argument(
        '--model', default='gpt-4.1-mini',
        help='OpenAI model to use (default: gpt-4.1-mini).',
    )
    gen_parser.add_argument(
        '--base-url', default=None, metavar='URL',
        help='OpenAI-compatible base URL (e.g. for Ollama: http://localhost:11434/v1).',
    )
    gen_parser.add_argument(
        '--api-key', default=None, metavar='KEY',
        help='OpenAI API key (default: read from OPENAI_API_KEY env var).',
    )
    gen_parser.add_argument(
        '--exclude', nargs='+', default=['nuke_internal', 'ocionuke'], metavar='FOLDER',
        help=(
            'Folder names to skip (default: nuke_internal ocionuke). '
            'Matched against each path component.'
        ),
    )
    gen_parser.add_argument(
        '--verbose', action='store_true', help='Enable debug logging.',
    )
    gen_parser.set_defaults(func=_run_generate_dataset)

    return parser


def _run_fixer(args: argparse.Namespace) -> None:
    logger = _make_logger(args.verbose)
    changes = ai_post_fixes(
        stubs_path=args.stubs_path,
        dry_run=args.dry_run,
        file_filter=args.file,
        exclude=args.exclude,
        provider=args.provider,
        model=args.model,
        api_key=args.api_key,
        base_url=args.base_url,
        logger=logger,
    )
    if args.dry_run:
        if not changes:
            print('\nDry run complete. No changes proposed.')
        else:
            print(f'\nDry run complete. {len(changes)} change(s) would be applied:\n')
            for change in changes:
                loc = f"{change['file']} :: {change.get('class') or '<module>'}.{change['function']}"
                print(f'  [{change["confidence"].upper()}] {loc}')
                print(f'    OLD: {change["old"].strip()}')
                print(f'    NEW: {change["new"].strip()}')
                print(f'    WHY: {change["reasoning"]}')
                print()
    else:
        print(f'\nDone. {len(changes)} correction(s) applied.')


def main() -> None:
    args = _build_parser().parse_args()
    args.func(args)


# ---------------------------------------------------------------------------
# Dataset generation — type stripping
# ---------------------------------------------------------------------------

class TypeStripper(ast.NodeTransformer):
    """Remove all PEP 3107 / PEP 526 type annotations from an AST."""

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        node.returns = None
        for arg in (
            node.args.args
            + node.args.posonlyargs
            + node.args.kwonlyargs
        ):
            arg.annotation = None
        if node.args.vararg:
            node.args.vararg.annotation = None
        if node.args.kwarg:
            node.args.kwarg.annotation = None
        self.generic_visit(node)
        return node

    visit_AsyncFunctionDef = visit_FunctionDef  # type: ignore[assignment]

    def visit_AnnAssign(self, node: ast.AnnAssign) -> ast.Assign | None:
        """Convert `x: int = 5` → `x = 5`; drop bare `x: int`."""
        if node.value is not None:
            new_node = ast.Assign(
                targets=[node.target],
                value=node.value,
                lineno=node.lineno,
                col_offset=node.col_offset,
            )
            return ast.fix_missing_locations(new_node)
        return None  # bare annotation-only statement — drop it


def strip_types(source: str) -> str:
    """Return source with all type annotations removed."""
    tree = ast.parse(source)
    stripped = TypeStripper().visit(tree)
    ast.fix_missing_locations(stripped)
    return ast.unparse(stripped)


# ---------------------------------------------------------------------------
# Dataset generation — chunk extraction
# ---------------------------------------------------------------------------

_BOILERPLATE_DOCSTRINGS = frozenset({
    'Create and return a new object',
    'Initialize self',
    'Return hash(self)',
})

_TRIVIAL_METHOD_NAMES = frozenset({'__init__', '__new__', '__hash__'})


@dataclass
class CodeChunk:
    """A snippet of stub code to be used as training input."""
    raw_source: str              # original source (may be stripped for Mode A)
    class_name: str | None
    base_classes: list[str]
    file_path: pathlib.Path
    is_trivial: bool             # True → skip this chunk


class ChunkExtractor:
    """Extract CodeChunk objects from a single stub .py file."""

    SMALL_CLASS_LIMIT = 50  # lines; classes at or below this become a single chunk

    def __init__(self, file_path: pathlib.Path) -> None:
        self.file_path = file_path
        self._source = file_path.read_text(encoding='utf-8')
        self._tree = ast.parse(self._source, filename=str(file_path))

    def extract(self) -> list[CodeChunk]:
        chunks: list[CodeChunk] = []
        for node in ast.iter_child_nodes(self._tree):
            if isinstance(node, ast.ClassDef):
                chunks.extend(self._process_class(node))
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                chunks.extend(self._process_module_function(node))
        return chunks

    # ------------------------------------------------------------------

    def _process_class(self, cls_node: ast.ClassDef) -> list[CodeChunk]:
        bases = [ast.unparse(b) for b in cls_node.bases]
        class_source = ast.get_source_segment(self._source, cls_node) or ''
        class_lines = class_source.count('\n') + 1
        trivial = self._class_is_trivial(cls_node)

        if class_lines <= self.SMALL_CLASS_LIMIT:
            return [CodeChunk(
                raw_source=class_source,
                class_name=cls_node.name,
                base_classes=bases,
                file_path=self.file_path,
                is_trivial=trivial,
            )]
        else:
            return self._extract_methods(cls_node, bases)

    def _extract_methods(
        self, cls_node: ast.ClassDef, bases: list[str]
    ) -> list[CodeChunk]:
        chunks: list[CodeChunk] = []
        base_str = f'({", ".join(bases)})' if bases else ''
        class_doc = ast.get_docstring(cls_node) or ''
        header_lines = [f'# Class: {cls_node.name}{base_str}']
        if class_doc:
            header_lines.append(f'# Docstring: {class_doc[:120]}')
        header = '\n'.join(header_lines) + '\n'

        for child in ast.iter_child_nodes(cls_node):
            if not isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            method_source = ast.get_source_segment(self._source, child) or ''
            if not method_source.strip():
                continue
            chunks.append(CodeChunk(
                raw_source=header + method_source,
                class_name=cls_node.name,
                base_classes=bases,
                file_path=self.file_path,
                is_trivial=self._method_is_trivial(child),
            ))
        return chunks

    def _process_module_function(
        self, node: ast.FunctionDef | ast.AsyncFunctionDef
    ) -> list[CodeChunk]:
        source = ast.get_source_segment(self._source, node) or ''
        if not source.strip():
            return []
        return [CodeChunk(
            raw_source=source,
            class_name=None,
            base_classes=[],
            file_path=self.file_path,
            is_trivial=False,
        )]

    # ------------------------------------------------------------------

    def _class_is_trivial(self, cls_node: ast.ClassDef) -> bool:
        methods = [
            n for n in ast.iter_child_nodes(cls_node)
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]
        if not methods:
            return True
        return all(self._method_is_trivial(m) for m in methods)

    def _method_is_trivial(
        self, node: ast.FunctionDef | ast.AsyncFunctionDef
    ) -> bool:
        if node.name not in _TRIVIAL_METHOD_NAMES:
            return False
        # Must have no real parameters (besides self/cls)
        args = node.args
        has_real_params = bool(
            args.args[1:]        # skip self/cls
            or args.posonlyargs
            or args.kwonlyargs
        )
        if has_real_params:
            return False
        doc = ast.get_docstring(node) or ''
        return any(b in doc for b in _BOILERPLATE_DOCSTRINGS)


# ---------------------------------------------------------------------------
# Dataset generation — response parsing & JSONL writing
# ---------------------------------------------------------------------------

def _parse_dataset_response(text: str) -> tuple[str, str] | None:
    """
    Extract (code, rationale) from a response.
    Returns None if the response is invalid or code is not syntactically valid.
    """
    code_match = re.search(r'```python\s*\n(.*?)```', text, re.DOTALL)
    if not code_match:
        return None
    code = code_match.group(1).strip()
    try:
        ast.parse(code)
    except SyntaxError:
        return None
    rationale_match = re.search(
        r'<rationale>(.*?)(?:</rationale>|$)', text, re.DOTALL
    )
    rationale = rationale_match.group(1).strip() if rationale_match else ''
    return code, rationale


def _append_jsonl(
    output_path: pathlib.Path,
    system: str,
    user: str,
    assistant: str,
) -> None:
    """Append one training record to the JSONL file."""
    record = {
        'messages': [
            {'role': 'system',    'content': system},
            {'role': 'user',      'content': user},
            {'role': 'assistant', 'content': assistant},
        ]
    }
    with output_path.open('a', encoding='utf-8') as f:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')


# ---------------------------------------------------------------------------
# Dataset generation — main orchestrator
# ---------------------------------------------------------------------------

class TrainingDataGenerator:
    """Generate JSONL fine-tuning data from Nuke/Hiero stub files via OpenAI API."""

    SMALL_CLASS_LIMIT = 50
    STUB_ONLY_RATIO = 0.20   # fraction of examples using stub-only system prompt
    MODE_A_RATIO = 0.60      # fraction of examples that fully strip types (Mode A)

    def __init__(
        self,
        stubs_dir: pathlib.Path,
        output_path: pathlib.Path,
        model: str,
        max_examples: int,
        api_key: str | None = None,
        base_url: str | None = None,
        exclude: list[str] | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        self.stubs_dir = stubs_dir
        self.output_path = output_path
        self.model = model
        self.max_examples = max_examples
        self.exclude: set[str] = set(exclude or [])
        self.logger = logger or logging.getLogger(__name__)

        try:
            import openai as _openai
        except ImportError as exc:
            raise ImportError(
                'openai package is required. Install with: pip install openai'
            ) from exc
        kwargs: dict = {}
        if api_key:
            kwargs['api_key'] = api_key
        if base_url:
            kwargs['base_url'] = base_url
        self._client = _openai.OpenAI(**kwargs)

    def run(self) -> int:
        """Collect chunks, call OpenAI for each, write JSONL. Returns example count."""
        all_chunks = self._collect_chunks()
        self.logger.info('Collected %d non-trivial candidate chunks', len(all_chunks))

        random.shuffle(all_chunks)
        candidates = all_chunks[:self.max_examples]
        total = len(candidates)

        written = 0
        for i, chunk in enumerate(candidates, 1):
            rel = chunk.file_path.relative_to(self.stubs_dir)
            self.logger.info(
                '[%d/%d] %s :: %s', i, total, rel, chunk.class_name or '<module>'
            )
            example = self._process_chunk(chunk)
            if example is None:
                self.logger.debug('  Skipped (invalid/empty response)')
                continue
            system, user, assistant = example
            _append_jsonl(self.output_path, system, user, assistant)
            written += 1
            time.sleep(RATE_LIMIT_DELAY)

        self.logger.info(
            'Done. %d example(s) written to %s', written, self.output_path
        )
        return written

    # ------------------------------------------------------------------

    def _collect_chunks(self) -> list[CodeChunk]:
        chunks: list[CodeChunk] = []
        for py_file in sorted(self.stubs_dir.glob('**/*.py')):
            # Skip __init__.py and __pycache__
            if py_file.name.startswith('__'):
                continue
            rel = py_file.relative_to(self.stubs_dir)
            if any(ex in rel.parts for ex in self.exclude):
                continue
            try:
                extractor = ChunkExtractor(py_file)
                file_chunks = [c for c in extractor.extract() if not c.is_trivial]
                chunks.extend(file_chunks)
            except SyntaxError as exc:
                self.logger.warning('Skipping %s (syntax error): %s', py_file.name, exc)
        return chunks

    def _process_chunk(
        self, chunk: CodeChunk
    ) -> tuple[str, str, str] | None:
        """Return (system, user, assistant) or None on failure."""
        use_stub_only = random.random() < self.STUB_ONLY_RATIO
        system = DATASET_SYSTEM_PROMPT_STUB_ONLY if use_stub_only else DATASET_SYSTEM_PROMPT

        use_mode_a = random.random() < self.MODE_A_RATIO
        if use_mode_a:
            try:
                input_code = strip_types(chunk.raw_source)
            except SyntaxError:
                input_code = chunk.raw_source
            user = (
                'Add type annotations to the following Python code. '
                'Use modern Python 3.10+ syntax.\n\n'
                f'```python\n{input_code}\n```'
            )
        else:
            user = (
                'Improve and complete the type annotations in the following Python code. '
                'Some annotations may already be present but incomplete or imprecise.\n\n'
                f'```python\n{chunk.raw_source}\n```'
            )

        raw_response = self._call_api(system, user)
        if raw_response is None:
            return None

        parsed = _parse_dataset_response(raw_response)
        if parsed is None:
            self.logger.debug('  Invalid response format (no code block or syntax error)')
            return None

        code, rationale = parsed
        assistant = f'```python\n{code}\n```'
        if rationale:
            assistant += f'\n\n<rationale>\n{rationale}\n</rationale>'

        return system, user, assistant

    def _call_api(self, system: str, user: str) -> str | None:
        for attempt in range(1, MAX_API_RETRIES + 1):
            try:
                response = self._client.chat.completions.create(
                    model=self.model,
                    max_tokens=4096,
                    messages=[
                        {'role': 'system', 'content': system},
                        {'role': 'user', 'content': user},
                    ],
                )
                return response.choices[0].message.content or ''
            except Exception as exc:
                if BaseAnnotationFixer._is_rate_limit(exc) and attempt < MAX_API_RETRIES:
                    self.logger.warning(
                        'Rate limit hit, backing off %ds (attempt %d/%d)',
                        BACKOFF_SECONDS, attempt, MAX_API_RETRIES,
                    )
                    time.sleep(BACKOFF_SECONDS)
                elif attempt == MAX_API_RETRIES:
                    self.logger.error(
                        'OpenAI API call failed after %d attempts: %s', MAX_API_RETRIES, exc
                    )
                    return None
                else:
                    self.logger.error('OpenAI API error: %s', exc)
                    return None
        return None


def _run_generate_dataset(args: argparse.Namespace) -> None:
    logger = _make_logger(args.verbose)
    generator = TrainingDataGenerator(
        stubs_dir=args.stubs_dir,
        output_path=args.output,
        model=args.model,
        max_examples=args.max_examples,
        api_key=args.api_key,
        base_url=args.base_url,
        exclude=args.exclude,
        logger=logger,
    )
    try:
        count = generator.run()
        print(f'\nDone. {count} training example(s) written to {args.output}')
    except KeyboardInterrupt:
        print('\nInterrupted. Partial output has been saved.')


if __name__ == '__main__':
    main()
