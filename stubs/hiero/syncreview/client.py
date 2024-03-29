from PySide2.QtCore import QTimer, Signal, QObject

from . import config, messages
from .log import logDebug, logMessage, logException
from .socket import ClientSocket
from .connectionstate import ConnectionState


def allowClientTimeout(clientId):
    """ Check if the client should time out, this does not happen for the client
    object used by the host.
    """
    return clientId != config.HOST_ID


class Client(QObject):
    """
    Class representing a client in the sync. Maintains a connection to the server
    and allows for sending and receiving messages.
    """

    # Notification of a change in the number of clients
    numberOfClientsChanged = Signal(int)

    # Signal emitted when a message is received from the server
    messageReceived = Signal(messages.Message)

    # Initialise with a ConnectionState object which may be shared with other classes,
    # and an id which is used to identify this client across connections
    def __init__(self, connectionState, clientId):
        super(Client, self).__init__()
        self._connectionState = connectionState
        self._clientId = clientId
        self._allowTimeout = allowClientTimeout(clientId)
        self._socket = None
        self._heartbeatSendTimer = None
        self._heartbeatTimeoutTimer = None

    def connectionState(self):
        """ Get the client's connection state """
        return self._connectionState

    def socketId(self):
        """ Get the socket Id used by this client. """
        return self._socket.socketId()

    def connectToHost(self, host, port, clientData):
        """ Try to connect on the given host and port. May raise an exception if the
        host isn't valid.
        """
        logMessage("Client.connectToHost host: '{}' port: {}".format(host, port))
        try:
            self._connectionState.setState(ConnectionState.CLIENT_CONNECTING)
            self._socket = ClientSocket(self)
            self._socket.dataReceived.connect(self._onDataReceived)
            self._socket.connectToHost('tcp://{}:{}'.format(host, port))
            message = messages.Connect(protocolVersion=config.PROTOCOL_VERSION,
                                       applicationVersion=config.APPLICATION_VERSION,
                                       clientData=clientData)
            logMessage('Client.connectToHost sending connect message '
                       'clientId: {} socketId: {} message: {}'.format(
                           self._clientId, self.socketId(), message))
            self.sendMessage(message)
            if self._allowTimeout:
                self._createHeartbeatTimers()
                self._heartbeatTimeoutTimer.start()
        except:
            self._connectionState.setError(ConnectionState.ERROR_CONNECT_INVALID_HOST)
            raise

    def _createHeartbeatTimers(self):
        if self._allowTimeout:
            self._heartbeatSendTimer = QTimer(self)
            self._heartbeatSendTimer.setInterval(config.HEARTBEAT_INTERVAL)
            self._heartbeatSendTimer.timeout.connect(self._onHeartbeatSendTimeout)
            self._heartbeatTimeoutTimer = QTimer(self)
            self._heartbeatTimeoutTimer.setSingleShot(True)
            self._heartbeatTimeoutTimer.setInterval(config.HEARTBEAT_TIMEOUT)
            self._heartbeatTimeoutTimer.timeout.connect(self._onServerTimeout)

    def disconnectFromHost(self):
        """ Close the connection. If a connection had been successfully established
        with the host, a disconnect message is sent, otherwise just close the socket
        etc
        """
        if self._connectionState == ConnectionState.CLIENT_CONNECTED:
            logMessage('Client.disconnectFromHost')
            self.sendMessage(messages.Disconnect())
        self._disconnected()

    def _disconnected(self):
        self._connectionState.setState(ConnectionState.DISCONNECTED)
        self._socket.close()
        if self._allowTimeout:
            self._heartbeatTimeoutTimer.stop()
            self._heartbeatSendTimer.stop()

    def _onDataReceived(self, data):
        if self._allowTimeout:
            self._heartbeatTimeoutTimer.start()

        # data may contain multiple messages. deserialize then apply filters before
        # handling them
        logDebug('Client._onDataReceived messages: {}'.format([d[0] for d in data]))
        msgList = [messages.deserializeMessage(d) for d in data]
        msgList = messages.applyMessageFilters(msgList)
        for msg in msgList:
            if self._connectionState == ConnectionState.CLIENT_CONNECTING:
                if isinstance(msg, messages.ConnectResponse):
                    self._handleConnectResponse(msg)
            elif self._connectionState == ConnectionState.CLIENT_CONNECTED:
                if isinstance(msg, messages.Disconnect):
                    logDebug('Client: received Disconnect message')
                    self._disconnected()
                elif isinstance(msg, messages.Pong):
                    pass
                elif isinstance(msg, messages.NumberOfPeers):
                    self.numberOfClientsChanged.emit(msg.content)
                else:
                    self.messageReceived.emit(msg)

    def _handleConnectResponse(self, msg):
        if msg.result == ConnectionState.ERROR_NONE:
            self._connectionState.setState(ConnectionState.CLIENT_CONNECTED)
            if self._allowTimeout:
                self._heartbeatSendTimer.start()
        else:
            self._connectionState.setError(msg.result, msg.responseText)

    def sendMessage(self, msg):
        logDebug('Client.sendMessage {}'.format(type(msg)))
        msg.sender = self._clientId
        self._socket.send(msg.serialize())

    def _onHeartbeatSendTimeout(self):
        logDebug('Client._onHeartbeatSendTimeout')
        self.sendMessage(messages.Ping())

    def _onServerTimeout(self):
        logMessage('Client: Connection to server timed out')
        # Set error state, with different codes if already connected vs trying to connect
        if self._connectionState == ConnectionState.CLIENT_CONNECTING:
            self._connectionState.setError(ConnectionState.ERROR_CONNECT_TIMEOUT)
        else:
            self._connectionState.setError(ConnectionState.ERROR_CONNECTION_LOST)
