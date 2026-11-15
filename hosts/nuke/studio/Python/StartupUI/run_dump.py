"""Run the dump inside a Nuke Studio GUI session, then quit.

hiero's C module and the nukescripts panels exist only with the GUI, so
terminal mode cannot dump them. Nuke Studio runs this file at startup when
NUKE_PATH points at the `studio` directory. It does nothing unless
HOSTSTUBS_DUMP_ARGS is set, as a space-separated dump.py argument list.
"""
import os
import sys
import logging


try:
    from PySide6 import QtCore, QtWidgets
except ImportError:
    from PySide2 import QtCore, QtWidgets


def _run():
    sys.path.insert(0, os.environ['HOSTSTUBS_INHOST'])
    import dump

    # The host has already configured the root logger, so basicConfig would do nothing.
    dump.LOGGER.addHandler(logging.StreamHandler())
    dump.LOGGER.setLevel(logging.INFO)
    try:
        dump.main(os.environ['HOSTSTUBS_DUMP_ARGS'].split())
    except BaseException:
        logging.exception('Dump failed')
    QtWidgets.QApplication.instance().quit()


if os.environ.get('HOSTSTUBS_DUMP_ARGS'):
    # Let the startup finish, so every module is in its normal state.
    QtCore.QTimer.singleShot(5000, _run)
