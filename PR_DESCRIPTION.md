# Rewrite the stub generator

Replaces `nukestubsgen.py` with the generator in `src/hoststubs/`. The stubs are now `.pyi` files built from a dump of the live API, with the 15.2v9 tree committed in `stubs/`.

Details are in [CHANGELOG.md](CHANGELOG.md).

Closes #5
