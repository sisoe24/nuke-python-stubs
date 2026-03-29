"""AI-powered type annotation fixer for Nuke Python stubs.

Reads generated stub files, extracts function signatures and docstrings,
sends them to an LLM (Anthropic, OpenAI, or Ollama) for correction, validates
the output, and applies fixes back to the files.

Usage:
    python ai_stubs_fixer.py [--dry-run] [--file nuke/classes/Node.py]
                              [--stubs-path PATH] [--provider anthropic|openai|ollama]
                              [--model MODEL] [--base-url URL] [--api-key KEY]
                              [--exclude FOLDER [FOLDER ...]] [--verbose]

Integration:
    from ai_stubs_fixer import ai_post_fixes
    ai_post_fixes(stubs_path, provider="anthropic")
"""
from __future__ import annotations

import ast
import json
import logging
import pathlib
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


class AnthropicFixer(BaseAnnotationFixer):
    """Fixer using the Anthropic API."""

    DEFAULT_MODEL = 'claude-sonnet-4-6'

    def __init__(self, model: str | None = None, api_key: str | None = None,
                 logger: logging.Logger | None = None):
        super().__init__(model or self.DEFAULT_MODEL, logger or logging.getLogger(__name__))
        try:
            import anthropic as _anthropic
        except ImportError as e:
            raise ImportError(
                'anthropic package is required for the anthropic provider. '
                'Install it with: pip install anthropic'
            ) from e
        self._client = _anthropic.Anthropic(api_key=api_key)

    def _call_api(self, functions: list[FunctionInfo]) -> list[CorrectionPayload]:
        response = self._client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            messages=[{'role': 'user', 'content': self._build_user_prompt(functions)}],
        )
        return self._parse_response(response.content[0].text)


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


def create_fixer(
    provider: str,
    model: str | None = None,
    api_key: str | None = None,
    base_url: str | None = None,
    logger: logging.Logger | None = None,
) -> BaseAnnotationFixer:
    """Factory: create the right fixer for the given provider name."""
    match provider:
        case 'anthropic':
            return AnthropicFixer(model, api_key, logger)
        case 'openai':
            return OpenAIFixer(model, api_key, base_url, logger)
        case 'ollama':
            return OllamaFixer(model, base_url, logger)
        case _:
            raise ValueError(
                f"Unknown provider {provider!r}. Choose from: anthropic, openai, ollama"
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
    provider: str = 'anthropic',
    model: str | None = None,
    api_key: str | None = None,
    base_url: str | None = None,
    logger: logging.Logger | None = None,
) -> list[dict]:
    """Run AI-powered annotation fixes on generated stubs.

    This is the integration entry point for nukestubsgen.py.
    API keys are read from environment variables if not provided explicitly:
      - Anthropic: ANTHROPIC_API_KEY
      - OpenAI:    OPENAI_API_KEY

    Args:
        stubs_path:  Path to the stubs directory.
        dry_run:     If True, propose changes without writing files.
        file_filter: Relative path to a single file (e.g. 'nuke/classes/Node.py').
        exclude:     List of folder names to skip (e.g. ['nuke_internal', 'nukescripts']).
                     Matched against each path component, so 'nuke_internal' skips
                     every file anywhere under a directory named 'nuke_internal'.
        provider:    'anthropic', 'openai', or 'ollama'.
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
        description='AI-powered type annotation fixer for Nuke Python stubs.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dry-run on a single file
  python ai_stubs_fixer.py --dry-run --file nuke/classes/Node.py

  # Fix all files using OpenAI
  python ai_stubs_fixer.py --provider openai --model gpt-4o

  # Fix using local Ollama
  python ai_stubs_fixer.py --provider ollama --model llama3

  # Specify a custom stubs path
  python ai_stubs_fixer.py --stubs-path /path/to/stubs
        """,
    )
    parser.add_argument(
        '--dry-run', action='store_true',
        help='Show proposed changes without writing to files.',
    )
    parser.add_argument(
        '--file', default=None, metavar='PATH',
        help='Process a single file (relative to --stubs-path).',
    )
    parser.add_argument(
        '--stubs-path', type=pathlib.Path, default=STUBS_PATH, metavar='PATH',
        help=f'Path to the stubs directory (default: {STUBS_PATH}).',
    )
    parser.add_argument(
        '--provider', default='anthropic', choices=['anthropic', 'openai', 'ollama'],
        help='AI provider to use (default: anthropic).',
    )
    parser.add_argument(
        '--model', default=None,
        help='Model name override. Defaults: anthropic=claude-sonnet-4-6, openai=gpt-4o, ollama=llama3.',
    )
    parser.add_argument(
        '--base-url', default=None, metavar='URL',
        help='Base URL for Ollama server (default: http://localhost:11434/v1).',
    )
    parser.add_argument(
        '--api-key', default=None, metavar='KEY',
        help='API key override (default: read from environment variable).',
    )
    parser.add_argument(
        '--exclude', nargs='+', default=None, metavar='FOLDER',
        help=(
            'One or more folder names to skip entirely (e.g. --exclude nuke_internal nukescripts). '
            'Matched against each path component of every discovered file.'
        ),
    )
    parser.add_argument(
        '--verbose', action='store_true',
        help='Enable debug logging.',
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()
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


if __name__ == '__main__':
    main()
