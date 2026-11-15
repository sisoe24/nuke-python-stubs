# Phase 0: prior-art decision

Date: 2026-11-15. Branch: `revamp/generic-core`.

Legend: **[verified]** means I read the code or ran the command.
**[assumed]** means I did not check it.

## Recommendation

1. **Rebuild here. Do not contribute the generator to cg-stubs.** Its Nuke
   package is not a generator to extend: it is one `stubgen` call, three
   `sed` lines, and hand edits, frozen at Nuke 13.2 since 2023.
2. **Do not use `stubgen` as-is for track A.** It gives 2% of returns a
   concrete type on the vendor source. Use `pyright --createstub`, which
   gives 25% and keeps docstrings. This needs one small change to the "parse with `ast`" rule
   (see below).
3. **Keep the prompt's architecture.** Nothing in the prior art replaces
   the dump / resolve / override / gate split.

## cg-stubs, Nuke package

All **[verified]** on a clone at `690330c` (2026-08-15) and on PyPI.

| Question | Finding |
|---|---|
| Does it already do this? | No. `types-nuke` is at `13.2.8.0`, the only release. `nuke/stubs` was last changed 2023-06-12. Later commits touch packaging only. |
| How is it generated? | `nuke/stubgen_nuke.sh`: mypy `stubgen` inside Nuke on `_nuke`, `nuke_internal`, and six small C modules, then `sed` for `string`, `Bool`, `MenuorNone`. The shipped file also has hand edits (`NodeConstructor[NodeT]`, commented-out defs), so the script no longer reproduces the output. |
| Docstrings? | None. 0 in `_nuke.pyi`. |
| Hiero, nukescripts, ocionuke? | Not covered. |
| How much is typed? | `_nuke.pyi`: 1,134 defs, 496 return `Any` (44%), 408 are `(*args, **kwargs)` (36%). |
| Does it type knobs? | No. `Node.__getitem__(name: str) -> Knob`, `Node.knob(...) -> Optional[Knob]`. No per-node knob names or classes. `nuke.nodes` types four classes only. |
| Is it maintained for Nuke? | Open and unmerged: PR 5 (2024-01), PR 24 (2025-07, one line), issue 20 "Update Nuke stubs to reflect API additions in 16.0+" (2025-05). |

The shared library (`common/src/stubgenlib`, about 1,700 lines) extends
`stubgen`'s C path with a `docstring_parser` signature generator and a
signature fixer. The Nuke package does not use it. Houdini does, plus a
2,175-line cleanup config. It has no IR, no probe, no override format
keyed by qualified name, and no `reveal_type` corpus.

**Why not contribute.** A contribution would replace the whole Nuke
directory with a different architecture, for maintainers who do not merge
one-line Nuke PRs. This repo's measurements say the value is in docstrings,
hiero, the probe, and the review step. cg-stubs has none of them.

**What to take from it:**

- Its hand-typed signatures are a free review list. Example: it has
  `root() -> Root` and `Node.rootNode() -> Group`; the old post-fixes here
  say `Node` for both. At Phase 4, diff the resolver output against
  `_nuke.pyi` and review each disagreement. Do not import its types
  unreviewed: they describe Nuke 13.2.
- Versioning (`<host version>.<stub revision>`) matches the prompt.
- Package layout: a `nuke-stubs/` directory inside the distribution.
- **Smallest useful contribution later:** once Nuke 15+ packages exist,
  open an issue on cg-stubs that offers them as the source for
  `types-nuke`. Not before.

`nuke-stubs` is free on PyPI (404). **[verified]**

## Track A tool: measured

Input: the vendor source already in `stubs/` on `main` (Nuke 15.0v1):
`nukescripts`, `hiero`, `ocionuke`, `nuke_internal`, without the generated
`classes/` directories. 271 files parse, 1 does not
(`hiero/exporters/FnNukeShotExporter.py`). **[verified, ran both tools]**

| | mypy 2.4.1 `stubgen --include-docstrings` | pyright 1.1.414 `--createstub` |
|---|---|---|
| Functions emitted | 3,056 | 3,051 |
| Return `None` | 1,681 (55%) | 1,760 (58%) |
| Return concrete | 57 (2%), all copied source annotations | 756 (25%): 666 inferred, 90 copied |
| Return partly known (a union or container with `Any` inside) | 0 | 240 (8%) |
| Return unknown | 1,318 (43%) | 295 (10%) |
| Params typed | 268 of 3,352 (8%), from literal defaults | 0 |
| Docstrings kept | yes | yes |
| Time | about 10 s | about 8 s |

`stubgen` does no inference from bodies: it copies source annotations and
writes `None` when a function has no `return`. Pyright runs its real
inference. Neither infers parameter types from call sites.

**Decision: pyright `--createstub` for track A.** Three consequences:

1. **Small conflict with the prompt.** Pyright writes inferred returns as
   a trailing comment: `def getViews(read): # -> list[Any]:`. `ast` drops
   comments. The loader must rewrite `# -> T:` to `-> T:` (one regex per
   `def` line) and then `ast.parse`. Still one intermediate, one resolver,
   one emitter. I need your approval for this deviation.
2. **Widen before accepting.** `Literal[False]` becomes `bool`,
   `LiteralString` becomes `str`. Any type that contains `Unknown` falls
   to `Any`. A base-class hook with an empty body (104 functions) is
   inferred as `None`, but subclasses return values: emit `Any` for
   empty bodies and for `raise NotImplementedError`.
3. **Parameters.** The dump records defaults from `inspect.signature`, so
   the literal-default rule (`x=False` gives `bool`) can live in the
   resolver. It is the same 8% `stubgen` gives, without a second tool.
   `None` defaults give no type.

## `stubgen` C path and `stubtest`

- `stubgen`'s C path reads the first docstring line (`name(args) -> ret`)
  and `__text_signature__`. It does not read epydoc `@return:` /
  `@param:`. Track B needs both, so track B stays a custom collector, as
  the prompt says. `docstring_parser` handles the epydoc fields, as
  cg-stubs' `DocstringSignatureGenerator` shows. **[verified in source]**
- `stubtest` must import the runtime, so it runs inside Nuke's Python
  with mypy on `PYTHONPATH`. cg-stubs does the same for `stubgen`.
  **[verified in `stubgen_nuke.sh`]** For C functions with no
  `__text_signature__` it checks existence and kind, not parameters.
  **[assumed, from mypy documentation]** Expect it to find missing and
  extra names in `nuke`, and real signature mismatches in the pure-Python
  modules.

## Open problems for your decision

1. **Branch base.** The prompt says cut from `main`. `main` lacks
   `ai_stubs_fixer.py`, `generate_dataset.py`, `training_data.jsonl`, and
   the AI-fixer edits to 379 stub files. The evaluation and baselines were
   measured on `feature/virgilsisoe/0.4.0`. I cut from `main` as
   instructed. Recommendation: keep it. Every missing file is on the
   Phase 8 delete list, `nukestubsgen.py` is identical on both, and the
   feature branch stays as the baseline reference.
2. **Track A needs vendor source on disk, so it is not a CI step.** The
   offline half has no Nuke install. Putting source text in `dump.json`
   and committing it would redistribute Foundry code. Recommendation: run
   pyright on the machine that has Nuke (no licence needed, only the
   files), and commit its bodiless `.pyi` output next to `dump.json` as a
   third input. CI then stays offline and deterministic.
3. **Track A baseline.** I count 3,751 `def`s in the 271 vendor files, not
   5,563. The difference is probably the generated `classes/` files, which
   are C-extension output and belong to track B. Re-measure on the real
   dump.
4. **The OpenAI key is still live.** `.envrc` is now in the repo
   `.gitignore` (commit `e7ee15b`). Rotation is yours to do.
