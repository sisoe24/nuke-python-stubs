# Changelog

## [0.4.0] - 2026-11-16

### Changed
- Stubs are now `.pyi` files with signatures, types and docstrings.
- New generator in `src/hoststubs`, replaces `nukestubsgen.py`.
- `stubs/` is built from Nuke 15.2v9. Nuke 17.1v2 can be built from `data/`.
- Unknown types are `Any`, no more guessed types.

### Added
- Runtime probes for return and parameter types.
- Overrides in `src/hoststubs/hosts/nuke/overrides/`.
- Build checks: every file parses, every name resolves.

### Fixed
- Stubs on `PYTHONPATH` no longer break Nuke (#5).
- `nuke.formats()` was missing.

### Removed
- Foundry source code copied into the stubs.
