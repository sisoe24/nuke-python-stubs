# Rewrite the stub generator

Replaces `nukestubsgen.py` with the generator in `src/hoststubs/`. The stubs are now `.pyi` files built from a dump of the live API, committed in `stubs/` for Nuke 15.2v9 and 17.1v2.

Details are in [CHANGELOG.md](CHANGELOG.md).

Closes #5
