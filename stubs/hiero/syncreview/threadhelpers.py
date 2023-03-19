from PySide2.QtCore import Qt, Slot, QObject, QThread, QMetaObject

from . import log


class CallInObjectsThreadHelper(QObject):
    def __init__(self):
        super(CallInObjectsThreadHelper, self).__init__()
        self._exception = None
        self._func = None
        self._args = None

    def call(self, func, *args):
        self._func = func
        self._args = args
        # If in a different thread, invoke with a blocking connection (this would
        # deadlock if called from the same thread)
        if self.thread() != QThread.currentThread():
            QMetaObject.invokeMethod(self, '_internalCall', Qt.BlockingQueuedConnection)
        else:
            self._internalCall()
        self._func = None
        self._args = None
        # If there was an exception rethrow it
        if self._exception:
            exc = self._exception
            self._exception = None
            raise exc

    @Slot()
    def _internalCall(self):
        try:
            self._func(*self._args)
        except Exception as e:
            log.logException()
            # Store the exception so it can be rethrown on the calling thread
            self._exception = e


def callInObjectsThread(obj, func, *args):
    """ Make a function call on a QObject ensuring that the call happens in the
    QThread it belongs to (which must be running an event loop). Blocks until the
    call is finished.
    """
    helper = CallInObjectsThreadHelper()
    helper.moveToThread(obj.thread())
    helper.call(func, *args)
