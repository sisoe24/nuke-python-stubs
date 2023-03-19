# Copies the cut positions of shots in a 'From' Track to multiple Destination 'To' Tracks
# Optionally renames the new shots with the Cut names from the 'From' Track.

import itertools
from enum import Enum, auto
from typing import Sequence

import hiero.ui
import hiero.core
from PySide2 import QtGui, QtCore, QtWidgets
from hiero.core import VideoTrack, EffectTrackItem


class CutSelectionBehavior(Enum):
    eCopyAllFromTrack = auto()
    eCopySelected = auto()


class NameBehavior(Enum):
    eDontCopy = auto()
    eCopy = auto()


class EffectAndTagBehavior(Enum):
    eDontCopy = auto()
    eReplace = auto()
    eAdd = auto()


class CutDataCopier:
    """ Class for performing the copying of cuts and related behaviors """

    def execute(self,
                nameBehavior: NameBehavior,
                effectBehavior: EffectAndTagBehavior,
                tagBehavior: EffectAndTagBehavior,
                srcItems: Sequence[hiero.core.TrackItem],
                dstTracks: Sequence[hiero.core.TrackBase]):
        """ Main method for performing the cut copying. Will also copy names and
        effects depending on the specified parameters.
        """
        if not srcItems:
            raise RuntimeError('No source items')
        sequence = srcItems[0].parentSequence()
        project = sequence.project()
        srcRanges = self._itemRanges(srcItems)
        self._checkConflicts(srcRanges, dstTracks)
        try:
            project.beginUndo('Copy Cuts')
            self._applyCuts(srcRanges, dstTracks)

            for dstTrack in dstTracks:
                for srcItem in srcItems:
                    dstItem = next((i for i in dstTrack if i.timelineIn()
                                   == srcItem.timelineIn()), None)
                    if dstItem:
                        if nameBehavior == NameBehavior.eCopy:
                            dstItem.setName(srcItem.name())
                        self._copyEffects(srcItem, dstItem, effectBehavior)
                        self._copyTags(srcItem, dstItem, tagBehavior)

            project.endUndo()
        except Exception:
            project.cancelUndo()
            raise

    def _itemRanges(self, items):
        """ Get the ranges of a list of track items as a list of tuples """
        return [(item.timelineIn(), item.timelineOut()) for item in items]

    def _checkConflicts(self, srcRanges, dstTracks):
        """ Check for conflicts in the copy cuts. The destination tracks should
        not have any cuts in the middle of the source edits.
        Raises RuntimeError if conflicts were found.
        """
        for dstTrack in dstTracks:
            dstRanges = self._itemRanges(dstTrack.items())
            for srcIn, srcOut in srcRanges:
                for dstIn, dstOut in dstRanges:
                    if (dstIn > srcIn and dstIn < srcOut) or (dstOut > srcIn and dstOut < srcOut):
                        raise RuntimeError(
                            'The selected cuts conflict with existing cuts on Track %s.\nPlease choose a track with no conflicts.' % dstTrack.name())

    def _applyCuts(self, srcRanges, dstTracks):
        """ Apply cuts to the destination tracks. The cuts are made at the start
        and end of each source track item.
        """
        cutPoints = []
        for srcIn, srcOut in srcRanges:
            cutPoints.extend((srcIn, srcOut + 1))
        for dstTrack in dstTracks:
            dstTrack.razorAt(cutPoints)

    def _copyEffects(self, srcItem, dstItem, effectBehavior):
        """ Apply the specified effect copying behavior from a source trackitem to
        a destination one.
        """
        if effectBehavior == EffectAndTagBehavior.eDontCopy:
            return
        srcTrack = srcItem.parentTrack()
        dstTrack = dstItem.parentTrack()
        if not isinstance(srcTrack, VideoTrack) or not isinstance(dstTrack, VideoTrack):
            return

        def findLinkedEffects(item):  # Helper to get the effects attached to a track item
            return [linked for linked in item.linkedItems() if isinstance(linked, EffectTrackItem)]

        dstEffects = findLinkedEffects(dstItem)
        if effectBehavior == EffectAndTagBehavior.eReplace:
            for effect in dstEffects:
                dstTrack.removeSubTrackItem(
                    effect, hiero.core.TrackBase.eDontRemoveLinkedItems)
            insertIndex = 0
        else:
            insertIndex = len(dstEffects)
        srcEffects = findLinkedEffects(srcItem)
        for subTrackIndex, effect in enumerate(srcEffects, start=insertIndex):
            dstTrack.createEffect(copyFrom=effect, trackItem=dstItem,
                                  subTrackIndex=subTrackIndex)

    def _copyTags(self, srcItem, dstItem, tagBehavior):
        """ Apply the specified tag copying behavior from a source trackitem to
        a destination one.
        """
        if tagBehavior == EffectAndTagBehavior.eDontCopy:
            return
        if tagBehavior == EffectAndTagBehavior.eReplace:
            oldTags = dstItem.tags()
            for tag in oldTags:
                dstItem.removeTag(tag)
        for tag in srcItem.tags():
            dstItem.addTag(tag.copy())


class DestinationTracksFilterModel(QtCore.QSortFilterProxyModel):
    """ Model for filtering out the currently selected source track from the list
    of possible destination tracks.
    """

    def __init__(self, dialog):
        QtCore.QSortFilterProxyModel.__init__(self)
        self._copyCutsDialog = dialog

    def filterAcceptsRow(self, sourceRow, sourceParent):
        srcItem = self.sourceModel().item(sourceRow)
        accept = srcItem.data() != self._copyCutsDialog.getCurrentFromTrack()
        return accept


class EffectAndTagCopyWidget(QtWidgets.QWidget):
    """ Widget for choosing how effects and tags should be copied """

    def __init__(self, forTags):
        QtWidgets.QWidget.__init__(self)
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self._checkBox = QtWidgets.QCheckBox()
        self._checkBox.setChecked(True)
        self._copyTypeWidget = QtWidgets.QComboBox()
        self._copyTypeWidget.addItem('Replace', EffectAndTagBehavior.eReplace)
        addText = 'Add' if forTags else 'Add on Top'
        self._copyTypeWidget.addItem(addText, EffectAndTagBehavior.eAdd)
        self._checkBox.stateChanged.connect(
            lambda newState: self._copyTypeWidget.setEnabled(newState == QtCore.Qt.Checked))
        layout.addWidget(self._checkBox)
        layout.addWidget(self._copyTypeWidget)

    def copyBehavior(self):
        if self._checkBox.isChecked():
            return self._copyTypeWidget.currentData()
        else:
            return EffectAndTagBehavior.eDontCopy


class CopyCutsFromTrack(QtWidgets.QDialog):
    def __init__(self, sequence, parent=None):
        if not parent:
            parent = hiero.ui.mainWindow()
        super(CopyCutsFromTrack, self).__init__(parent)
        self.setWindowTitle('Copy Cuts')
        self.setSizeGripEnabled(False)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.setContentsMargins(5, 0, 5, 0)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(20, 20, 20, 20)

        self.buildTracksList(sequence)

        self.groupBox = QtWidgets.QGroupBox('Tracks')
        self.groupLayout = QtWidgets.QFormLayout()
        self.groupBox.setLayout(self.groupLayout)

        self._copyTaskType = QtWidgets.QComboBox()
        self._copyTaskType.setToolTip(
            'Choose to copy all cuts on the From Track or only selected cuts.')
        self.groupLayout.addRow('', self._copyTaskType)
        self._copyTaskType.addItem(
            'Copy All Cuts', CutSelectionBehavior.eCopyAllFromTrack)
        self._copyTaskType.addItem(
            'Copy Selected Cuts', CutSelectionBehavior.eCopySelected)

        self._copyNamesCheckBox = QtWidgets.QCheckBox('Copy Names')
        self._copyNamesCheckBox.setToolTip(
            'Checking this box will rename newly cut shots with names matching the From shots.Otherwise does not rename the newly cut shots.')
        self.groupLayout.addRow('', self._copyNamesCheckBox)

        self._copyEffectsWidget = EffectAndTagCopyWidget(False)
        self.groupLayout.addRow('Copy Soft Effects:', self._copyEffectsWidget)

        self._copyTagsWidget = EffectAndTagCopyWidget(True)
        self.groupLayout.addRow('Copy Tags:', self._copyTagsWidget)

        self._fromTrackDropdown = QtWidgets.QComboBox()
        self._fromTrackDropdown.setToolTip('The track you wish to copy cuts from.')
        self.groupLayout.addRow('From:', self._fromTrackDropdown)

        self._toTrackDropdown = QtWidgets.QWidget()
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(210, 50, 151, 181))
        self.verticalLayoutWidget.setObjectName('verticalLayoutWidget')

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName('verticalLayout')

        self.trackListModel = QtGui.QStandardItemModel()
        self.trackListView = QtWidgets.QListView()
        self.trackListView.setToolTip('Selected tracks will have cuts applied to them.')
        self.dstTracksFilterModel = DestinationTracksFilterModel(self)
        self.dstTracksFilterModel.setSourceModel(self.trackListModel)
        self.trackListView.setModel(self.dstTracksFilterModel)

        # Populate track list
        defaultIndex = -1
        for track in self.allTracks:
            if track.numItems() == 0:
                continue
            # This ensures that the defaultIndex is the bottom most (non-empty) video track, if there is one
            if isinstance(track, hiero.core.VideoTrack):
                defaultIndex += 1
            self._fromTrackDropdown.addItem(
                self.getIconForTrack(track), track.name(), track)

        self._fromTrackDropdown.setCurrentIndex(max(0, defaultIndex))

        self.sequence = sequence

        self.populateTrackListModel()
        self.groupLayout.addRow('To:', self.trackListView)
        self.toggleAll = QtWidgets.QPushButton('Select/Deselect All Tracks')
        self.toggleAll.setToolTip(
            'Selects or Deselects All Tracks except the currently set From Track')
        self.groupLayout.addRow('', self.toggleAll)
        self.toggleAll.clicked.connect(self.toggleAllTracks)

        self._fromTrackDropdown.currentIndexChanged.connect(
            self.fromTrackSelectionChanged)

        # Add the standard ok/cancel buttons, default to ok.
        self._buttonbox = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        self._buttonbox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setText('OK')
        self._buttonbox.button(
            QtWidgets.QDialogButtonBox.StandardButton.Ok).setDefault(True)
        self._buttonbox.accepted.connect(self.accept)
        self._buttonbox.rejected.connect(self.reject)
        self.groupLayout.addWidget(self._buttonbox)

        self.setLayout(self.groupLayout)
        self.layout.addWidget(self.groupBox)

    # Sets the Video/Audio Icon according to Track Type
    def getIconForTrack(self, track):
        trackIcon = None
        if isinstance(track, hiero.core.AudioTrack):
            trackIcon = QtGui.QIcon('icons:AudioOnly.png')
        elif isinstance(track, hiero.core.VideoTrack):
            trackIcon = QtGui.QIcon('icons:VideoOnly.png')
        return trackIcon

    def getCurrentFromTrack(self):
        """ Get the selected source track """
        return self._fromTrackDropdown.itemData(self._fromTrackDropdown.currentIndex())

    def getDestinationTracks(self):
        """ Get the selected destination tracks """
        tracks = []
        fromTrack = self.getCurrentFromTrack()
        for row in range(self.trackListModel.rowCount()):
            item = self.trackListModel.item(row)
            track = item.data()
            if item.checkState() == QtCore.Qt.Checked and track != fromTrack:
                tracks.append(track)
        return tracks

    def populateTrackListModel(self):
        """ Build the model for the target track selection. Empty or locked tracks
        are disabled, all other video tracks are enabled by default.
        """

        # Allow copying to effect-only video tracks
        def _isTrackEmpty(track):
            return not (len(track.items()) > 0 or
                        isinstance(track, VideoTrack) and len(track.subTrackItems()) > 0)

        for track in self.allTracks:
            item = QtGui.QStandardItem(track.name())
            item.setData(track)
            item.setIcon(self.getIconForTrack(track))

            if track.isLocked():
                item.setEnabled(False)
                item.setToolTip('%s is Locked. Unlock to apply cuts.' % track.name())
            elif _isTrackEmpty(track):
                item.setEnabled(False)
                item.setToolTip('%s is Empty.' % track.name())
            else:
                if isinstance(track, VideoTrack):
                    item.setCheckState(QtCore.Qt.Checked)
                else:
                    item.setCheckState(QtCore.Qt.Unchecked)

            item.setCheckable(True)
            item.setEditable(False)
            self.trackListModel.appendRow(item)

    # Get the initial list of all tracks in the sequence, ordered as they should
    # appear in the UI
    def buildTracksList(self, sequence):
        self.allTracks = []
        for existingtrack in reversed(sequence.videoTracks()):
            self.allTracks.append(existingtrack)
        for existingtrack in sequence.audioTracks():
            self.allTracks.append(existingtrack)

    def fromTrackSelectionChanged(self, item):
        self.dstTracksFilterModel.invalidate()

    def toggleAllTracks(self):
        checkState = QtCore.Qt.Checked
        for row in range(self.trackListModel.rowCount()):
            if self.trackListModel.item(row).checkState() == QtCore.Qt.Checked:
                checkState = QtCore.Qt.Unchecked
                break
        for row in range(self.trackListModel.rowCount()):
            item = self.trackListModel.item(row)
            if item.isEnabled():
                item.setCheckState(checkState)

    def cutSelectionBehavior(self):
        return self._copyTaskType.currentData()

    def nameBehavior(self):
        return NameBehavior.eCopy if self._copyNamesCheckBox.isChecked() else NameBehavior.eDontCopy

    def effectBehavior(self):
        return self._copyEffectsWidget.copyBehavior()

    def tagBehavior(self):
        return self._copyTagsWidget.copyBehavior()


class CopyCutsFromTrackAction(QtWidgets.QAction):
    def __init__(self):
        QtWidgets.QAction.__init__(self, 'Copy Cuts', None)
        self.triggered.connect(self.doCuts)
        hiero.core.events.registerInterest(
            'kShowContextMenu/kTimeline', self.eventHandler)

    def toggleTrackLock(self, tracklist, lockstate=True):
        for track in tracklist:
            if lockstate:
                track.setLocked(True)
            else:
                track.setLocked(False)

    def doCuts(self):
        selection = hiero.ui.activeView().selection()
        sequence = hiero.ui.activeView().sequence()
        project = sequence.project()
        dialog = CopyCutsFromTrack(sequence)

        dialog._copyTaskType.setVisible(self.enableSelectedCutsCopyMode)
        dialog._copyTaskType.setCurrentIndex(0)

        if dialog.exec_():
            fromTrack = dialog.getCurrentFromTrack()
            destinationTracks = dialog.getDestinationTracks()
            selectionBehavior = dialog.cutSelectionBehavior()
            if selectionBehavior == CutSelectionBehavior.eCopySelected:
                # Note that the selected items don't have to be on the selected 'from'
                # track. Slightly odd but it has always worked like this
                srcTrackItems = [item for item in selection if isinstance(
                    item, hiero.core.TrackItem)]
            else:
                srcTrackItems = fromTrack.items()
            nameBehavior = dialog.nameBehavior()
            effectBehavior = dialog.effectBehavior()
            tagBehavior = dialog.tagBehavior()

            try:
                copier = CutDataCopier()
                copier.execute(nameBehavior, effectBehavior, tagBehavior,
                               srcTrackItems, destinationTracks)
            except RuntimeError as exc:
                # If an error happens, most likely the conflict checking, show a warning
                # and go round again
                QtWidgets.QMessageBox.warning(None, 'Copy Cuts', str(exc))
                self.doCuts()

    def eventHandler(self, event):
        if not hasattr(event.sender, 'selection'):
            # Something has gone wrong, we should only be here if raised
            # by the timeline view which will give a selection.
            return

        # We don't enable Copy Cuts action for a Clip opened in a Timeline View
        if not hiero.ui.activeView() or hiero.ui.activeView().sequence() == None:
            return

        shotSelection = [item for item in event.sender.selection(
        ) if isinstance(item, hiero.core.TrackItem)]

        self.enableSelectedCutsCopyMode = True
        if len(shotSelection) == 0:
            # We disable the Selected Cuts option if no shots are selected
            self.enableSelectedCutsCopyMode = False
        title = 'Copy Cuts...'
        self.setText(title)

        for a in event.menu.actions():
            if a.text().lower().strip() == 'editorial':
                hiero.ui.insertMenuAction(
                    self, a.menu(), after='foundry.timeline.enableItem')


# Instantiate the action to get it to register itself.
copyCutsFromTrackAction = CopyCutsFromTrackAction()
