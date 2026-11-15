"""Run dump.py or probe.py inside a Nuke Studio GUI session, then quit.

hiero's C module and the nukescripts panels exist only with the GUI, so
terminal mode cannot reach them. Nuke Studio runs this file at startup when
NUKE_PATH points at the `studio` directory. It does nothing unless
HOSTSTUBS_RUN is `dump` or `probe`; HOSTSTUBS_ARGS is that script's
space-separated argument list.
"""
import os
import sys
import logging
import importlib

try:
    from PySide6 import QtCore
except ImportError:
    from PySide2 import QtCore


def _run():
    sys.path.insert(0, os.environ['HOSTSTUBS_INHOST'])
    script = importlib.import_module(os.environ['HOSTSTUBS_RUN'])

    # The host has already configured the root logger, so basicConfig would do nothing.
    script.LOGGER.addHandler(logging.StreamHandler())
    script.LOGGER.setLevel(logging.INFO)

    status = 0
    try:
        script.main(os.environ['HOSTSTUBS_ARGS'].split())
    except BaseException:
        logging.exception('%s failed', os.environ['HOSTSTUBS_RUN'])
        status = 1

    # A normal quit can ask to save the probe's project and wait for an answer.
    sys.stderr.flush()
    os._exit(status)


if os.environ.get('HOSTSTUBS_RUN') in ('dump', 'probe'):
    # Let the startup finish, so every module is in its normal state.
    QtCore.QTimer.singleShot(5000, _run)
