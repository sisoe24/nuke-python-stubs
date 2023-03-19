import hiero.core

from . import connect_ui, connectionmanager, syncreviewstatuspanel
from .syncreviewstatuswidget import SyncReviewStatusWidget

syncEnabled = 'syncreview' in hiero.core.env['Features']
if not syncEnabled:
    raise ImportError('Sync Review is disabled')


try:
    import hiero.ui.FnStatusBar
except ImportError as e:
    hiero.core.log.debug('Importing FnStatusBar failed %s' % e)


# Globals for the connection state and the UI
connectionManagerInstance = None
menuBuilderInstance = None


def initialise():
    """ Initialise the objects and UI for the sync review functionality """
    global connectionManagerInstance
    global menuBuilderInstance

    # Create the connection manager
    connectionManagerInstance = connectionmanager.ConnectionManager()
    hiero.core.events.registerInterest(
        'kShutdown', lambda event: connectionManagerInstance.shutdown())

    # Set up the UI
    menuBuilderInstance = connect_ui.MenuBuilder(connectionManagerInstance)
    menuBuilderInstance.createMenus()

    # Add the SyncReviewStatusWidget to the status bar
    if hasattr(hiero.ui, 'mainStatusBar'):
        hiero.ui.mainStatusBar.setSyncReviewStatusWidget(
            SyncReviewStatusWidget(connectionManagerInstance))

    # Add SyncReviewStatusPanel to the window manager.
    syncreviewstatuspanel.initialise(connectionManagerInstance)
