"""Build one host version: emit the stubs, lay out the package, run the gate."""
from __future__ import annotations

import shutil
import logging
from pathlib import Path

from hoststubs.emit import emit, package
from hoststubs.gate import check_names, check_syntax, gate, run_corpus, write_snapshot
from hoststubs.host import load_host
from hoststubs.report import load_context

LOGGER = logging.getLogger(__name__)


def build(dump_path: Path, out: Path, update_snapshot: bool = False) -> list[str]:
    """Write `out/stubs` and `out/package` and return the gate findings.

    With `update_snapshot`, what pyright reveals for the corpus is recorded
    instead of checked. Review the snapshot diff before committing it.
    """
    context = load_context(dump_path)
    dump = context.dump

    if out.exists():
        shutil.rmtree(out)
    stubs = out / 'stubs'
    written = emit(context, stubs)
    package(context, load_host(dump.host), stubs, out / 'package')
    LOGGER.info('Wrote %d files under %s.', len(written), out)

    if not update_snapshot:
        return gate(stubs, dump.host, dump.host_version, dump.python)

    found = run_corpus(stubs, dump.python)
    LOGGER.info('Wrote %s.', write_snapshot(found, dump.host, dump.host_version))
    return check_syntax(stubs) + check_names(stubs)
