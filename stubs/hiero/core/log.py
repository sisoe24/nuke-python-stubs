import os
import logging

# Logging functions for Hiero
# This is just a thin wrapper around the Python logging module,
# but we might want to extend the interface, e.g. to have separate
# channels for different Hiero modules.

# Our log levels
kDebug = 0
kInfo = 1
kError = 2

# String used for formatting log messages.
# Currently we just get e.g. 'ERROR: Something went wrong'
_format = '%(levelname)s %(asctime)s.%(msecs)03d:%(name)s(%(process)d): %(message)s'
_dateFormat = '%H:%M:%S'

_logLevel = kError

_levelMap = {
    kDebug: logging.DEBUG,
    kInfo: logging.INFO,
    kError: logging.ERROR
}

# Set the default logging output level to only show errors.
logging.basicConfig(format=_format, level=_levelMap[_logLevel], datefmt=_dateFormat)
_logger = logging.getLogger('Hiero')


def _formatMessage(message, *args):
    if isinstance(message, str) and message.find('%') != -1 and args:
        try:
            return message % args
        except:
            pass
    result = str(message)
    for arg in args:
        result += ' ' + str(arg)
    return result


def setLogLevel(level):
    """ Set the logging output level.  Possible values are: kDebug, kInfo, kError """
    global _logLevel
    _logLevel = level
    _logger.setLevel(_levelMap[level])


def logLevel():
    """ Get the current log output level.  Possible values are: kDebug, kInfo, kError """
    return _logLevel


def debug(message, *args):
    """
    Log message at kDebug level. If the message is a string containing formatting placeholders, args will  be merged into it using the string formatting operator.
    Otherwise the arguments will be concatenated into a string with spaces separating them.
    """
    _logger.debug(_formatMessage(message, *args))


def info(message, *args):
    """ Log message at kInfo level. If the message is a string containing formatting placeholders, args will  be merged into it using the string formatting operator.
    Otherwise the arguments will be concatenated into a string with spaces separating them. """
    _logger.info(_formatMessage(message, *args))


def error(message, *args):
    """ Log message at kError level. If the message is a string containing formatting placeholders, args will  be merged into it using the string formatting operator.
    Otherwise the arguments will be concatenated into a string with spaces separating them. """
    _logger.error(_formatMessage(message, *args))


def exception(message, *args):
    """ The same as error(), but also prints a stack trace.  Only call from an exception handler. """
    _logger.exception(_formatMessage(message, *args))


_fileLoggers = {}
_logDir = os.path.join(os.environ['NUKE_TEMP_DIR'], 'logs')


def getFileLogger(name):
    """ Get a logger which writes to a file in the user's NUKE_TEMP_DIR """
    try:
        return _fileLoggers[name]
    except KeyError:
        fileLogger = _logger.getChild(name)
        _fileLoggers[name] = fileLogger
        fileLogger.propagate = False
        logPath = os.path.join(_logDir, '{}.log'.format(name))
        fileHandler = logging.FileHandler(logPath, mode='w')
        fileLogFormat = '%(levelname)s %(asctime)s.%(msecs)03d: %(filename)s:%(lineno)d %(funcName)s(): %(message)s'
        fileHandler.setFormatter(logging.Formatter(fileLogFormat))
        fileHandler.setLevel(logging.DEBUG)
        fileLogger.setLevel(logging.DEBUG)
        fileLogger.addHandler(fileHandler)
        return fileLogger
