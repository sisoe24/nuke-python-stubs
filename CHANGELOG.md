# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.4.0] - 2026-11-16

### Changed
- The stubs are `.pyi` files with signatures, types and docstrings.
- A new generator in `src/hoststubs` replaces `nukestubsgen.py`.
- Stubs ship as release assets, one zip per Nuke version: 15.2v9 and 17.1v2. The `stubs/` folder is no longer in the repository.
- A type that cannot be found is `Any`, not a guess.

### Added
- Probes that run inside Nuke to find return and parameter types.
- Hand-written overrides in `src/hoststubs/hosts/nuke/overrides/`.
- A check on every build: files parse and names resolve. Files that failed to parse went from 6 to 0, undefined names from 930 to 0.

### Fixed
- Stubs on `PYTHONPATH` no longer break Nuke (#5).
- `nuke.formats()` was missing.

### Removed
- Foundry source code that was copied into the stubs.
