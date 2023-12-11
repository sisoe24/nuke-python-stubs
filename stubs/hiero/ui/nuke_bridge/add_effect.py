import os
import sys

import hiero.ui
import hiero.core
from hiero.ui import registerAction
from hiero.core import log
from PySide2.QtGui import QIcon, QKeySequence
from PySide2.QtWidgets import QMenu, QAction

from .send_to_nuke import SendToNukeHandler

gNukeIconPath = 'icons:'


def createEffectActions():
    # Create the actions which should be added to the Effect button on the toolbar of the timeline view.
    # It will look for any actions which match foundry.timeline.effect.*
    # To have it create a soft effect we call setData with the node type.
    isPlayer = hiero.core.isHieroPlayer()

    if not isPlayer:
        action = QAction(QIcon(gNukeIconPath + '/ColorCorrect.png'), 'ColorCorrect', None)
        action.setObjectName('foundry.timeline.effect.addColorCorrect')
        action.setToolTip('ColorCorrect')
        action.setShortcut(QKeySequence('Alt+C'))
        action.setData('ColorCorrect')
        registerAction(action)

        action = QAction(QIcon(gNukeIconPath + '/Grade.png'), 'Grade', None)
        action.setObjectName('foundry.timeline.effect.addGrade')
        action.setToolTip('Grade')
        action.setShortcut(QKeySequence('Alt+G'))
        action.setData('Grade')
        registerAction(action)

        action = QAction(QIcon(gNukeIconPath + '/2D.png'), 'Transform', None)
        action.setObjectName('foundry.timeline.effect.addTransform')
        action.setToolTip('Transform')
        action.setShortcut(QKeySequence('Alt+T'))
        action.setData('Transform')
        registerAction(action)

        action = QAction()
        action.setObjectName('foundry.timeline.effect.separator')
        action.setSeparator(True)
        registerAction(action)

        action = QAction(QIcon(gNukeIconPath + '/Text.png'), 'Text', None)
        action.setObjectName('foundry.timeline.effect.addText')
        action.setToolTip('Text')
        action.setData('Text2')
        registerAction(action)

        action = QAction(QIcon(gNukeIconPath + '/TimeWarp.png'), 'Timewarp', None)
        action.setObjectName('foundry.timeline.effect.addTimewarp')
        action.setToolTip('Timewarp')
        action.setData('TimeWarp')
        registerAction(action)

        colorMenu = QMenu('Color')
        colorMenu.setObjectName('foundry.timeline.effect.colorMenuMain')

        action = QAction(QIcon(gNukeIconPath + 'ToolbarColor.png'), 'Color', None)
        action.setObjectName('foundry.timeline.effect.colorMenuAction')
        action.setToolTip('Color')
        action.setMenu(colorMenu)
        registerAction(action)

        action = QAction(QIcon(gNukeIconPath + '/ColorLookup.png'), 'ColorLookup', None)
        action.setObjectName('foundry.timeline.effect.addColorLookup')
        action.setToolTip('ColorLookup')
        action.setData('ColorLookup')
        colorMenu.addAction(action)
        registerAction(action)

        colorMenu.addSeparator()

    action = QAction(QIcon(gNukeIconPath + '/OCIO.png'), 'OCIO CDLTransform', None)
    action.setObjectName('foundry.timeline.effect.addOCIOCDLTransform')
    action.setToolTip('OCIOCDLTransform')
    action.setData('OCIOCDLTransform')
    if not isPlayer:
        colorMenu.addAction(action)
    registerAction(action)

    action = QAction(QIcon(gNukeIconPath + '/OCIO.png'), 'OCIO ColorSpace', None)
    action.setObjectName('foundry.timeline.effect.addOCIOColorSpace')
    action.setToolTip('OCIOColorSpace')
    action.setData('OCIOColorSpace')
    if not isPlayer:
        colorMenu.addAction(action)
    registerAction(action)

    action = QAction(QIcon(gNukeIconPath + '/OCIO.png'), 'OCIO Display', None)
    action.setObjectName('foundry.timeline.effect.addOCIODisplay')
    action.setToolTip('OCIODisplay')
    action.setData('OCIODisplay')
    if not isPlayer:
        colorMenu.addAction(action)
    registerAction(action)

    action = QAction(QIcon(gNukeIconPath + '/OCIO.png'), 'OCIO FileTransform LUT', None)
    action.setObjectName('foundry.timeline.effect.addOCIOFileTransform')
    action.setToolTip('OCIOFileTransform')
    action.setData('OCIOFileTransform')
    if not isPlayer:
        colorMenu.addAction(action)
    registerAction(action)

    action = QAction(QIcon(gNukeIconPath + '/OCIO.png'), 'OCIO LogConvert', None)
    action.setObjectName('foundry.timeline.effect.addOCIOLogConvert')
    action.setToolTip('OCIOLogConvert')
    action.setData('OCIOLogConvert')
    if not isPlayer:
        colorMenu.addAction(action)
    registerAction(action)

    action = QAction(QIcon(gNukeIconPath + '/OCIO.png'), 'OCIO LookTransform', None)
    action.setObjectName('foundry.timeline.effect.addOCIOLookTransform')
    action.setToolTip('OCIOLookTransform')
    action.setData('OCIOLookTransform')
    if not isPlayer:
        colorMenu.addAction(action)
    registerAction(action)

    action = QAction(QIcon(gNukeIconPath + '/OCIO.png'), 'OCIO NamedTransform', None)
    action.setObjectName('foundry.timeline.effect.addOCIONamedTransform')
    action.setToolTip('OCIONamedTransform')
    action.setData('OCIONamedTransform')
    if not isPlayer:
        colorMenu.addAction(action)
    registerAction(action)

    if not isPlayer:
        action = QAction(QIcon(gNukeIconPath + '/denoise.png'), 'Denoise', None)
        action.setObjectName('foundry.timeline.effect.Denoise')
        action.setToolTip('Denoise')
        action.setData('Denoise2')
        registerAction(action)

        action = QAction(QIcon(gNukeIconPath + '/ChromaKeyer.png'), 'ChromaKeyer', None)
        action.setObjectName('foundry.timeline.effect.ChromaKeyer')
        action.setToolTip('ChromaKeyer')
        action.setData('ChromaKeyer')
        registerAction(action)

        mergeMenu = QMenu('Merge')
        mergeMenu.setObjectName('foundry.timeline.effect.mergeMenuMain')

        action = QAction(QIcon(gNukeIconPath + '/Merge.png'), 'Merge', None)
        action.setObjectName('foundry.timeline.effect.mergeMenuAction')
        action.setToolTip('Merge')
        action.setMenu(mergeMenu)
        registerAction(action)

        action = QAction(QIcon(gNukeIconPath + '/Premult.png'), 'Premult', None)
        action.setObjectName('foundry.timeline.effect.Premult')
        action.setToolTip('Premult')
        action.setData('Premult')
        mergeMenu.addAction(action)
        registerAction(action)

        action = QAction(QIcon(gNukeIconPath + '/Unpremult.png'), 'Unpremult', None)
        action.setObjectName('foundry.timeline.effect.Unpremult')
        action.setToolTip('Unpremult')
        action.setData('Unpremult')
        mergeMenu.addAction(action)
        registerAction(action)

        transformsMenu = QMenu('Transformations')
        transformsMenu.setObjectName('foundry.timeline.effect.transformsMenuMain')

        action = QAction(QIcon(gNukeIconPath + 'ToolbarTransform.png'),
                         'Transformations', None)
        action.setObjectName('foundry.timeline.effect.transformsMenuAction')
        action.setToolTip('Transformations')
        action.setMenu(transformsMenu)
        registerAction(action)

        action = QAction(QIcon(gNukeIconPath + '/Crop.png'), 'Crop', None)
        action.setObjectName('foundry.timeline.effect.addCrop')
        action.setToolTip('Crop')
        action.setData('Crop')
        transformsMenu.addAction(action)
        registerAction(action)

        action = QAction(QIcon(gNukeIconPath + '/LensDistort.png'),
                         'LensDistortion', None)
        action.setObjectName('foundry.timeline.effect.LensDistortion')
        action.setToolTip('LensDistortion')
        action.setData('LensDistortion2')
        transformsMenu.addAction(action)
        registerAction(action)

        action = QAction(QIcon(gNukeIconPath + '/Mirror.png'), 'Mirror', None)
        action.setObjectName('foundry.timeline.effect.addMirror')
        action.setToolTip('Mirror')
        action.setData('Mirror2')
        transformsMenu.addAction(action)
        registerAction(action)

        action = QAction(QIcon(gNukeIconPath + '/CornerPin.png'), 'CornerPin', None)
        action.setObjectName('foundry.timeline.effect.CornerPin')
        action.setToolTip('CornerPin')
        action.setData('CornerPin2D')
        transformsMenu.addAction(action)
        registerAction(action)

        action = QAction(QIcon(gNukeIconPath + '/ModifyMetaData.png'),
                         'ModifyMetaData', None)
        action.setObjectName('foundry.timeline.effect.ModifyMetaData')
        action.setToolTip('ModifyMetaData')
        action.setData('ModifyMetaData')
        registerAction(action)

        action = QAction(QIcon(gNukeIconPath + '/BurnIn.png'), 'Burn-In', None)
        action.setObjectName('foundry.timeline.effect.addBurnIn')
        action.setToolTip('Burn-In')
        action.setData('BurnIn')
        registerAction(action)

        action = QAction(QIcon(gNukeIconPath + '/Inference.png'), 'Inference', None)
        action.setObjectName('foundry.timeline.effect.Inference')
        action.setToolTip('Inference')
        action.setData('Inference')
        registerAction(action)

        action = QAction(QIcon(gNukeIconPath + '/BlinkScript.png'), 'BlinkScript', None)
        action.setObjectName('foundry.timeline.effect.BlinkScript')
        action.setToolTip('BlinkScript')
        action.setData('BlinkScript')
        registerAction(action)


def createEffectActionsStudio():
    action = QAction('Create Comp', None)
    action.setObjectName('foundry.timeline.comp.createComp')
    action.setToolTip('Create Comp')
    action.setEnabled(False)
    registerAction(action)

    action = QAction('Create Comp Special...', None)
    action.setObjectName('foundry.timeline.comp.createCompSpecial')
    action.setToolTip('Create Comp Special')
    action.setEnabled(False)
    registerAction(action)

    createEffectActions()


class AddEffectHandler(SendToNukeHandler):
    def __init__(self, hieroState):
        log.debug('add effect handler')

        SendToNukeHandler.__init__(self, hieroState)

        fileMenu = hiero.ui.findMenuAction('foundry.menu.file')
        # Connect to the global 'Add Effect' action, which is added to the timeline toolbar
        createCompGlobalAction = hiero.ui.findRegisteredAction(
            'foundry.timeline.comp.createComp')
        createCompSpecialAction = hiero.ui.findRegisteredAction(
            'foundry.timeline.comp.createCompSpecial')
        if createCompGlobalAction:
            createCompGlobalAction.triggered.connect(self.onCreateComp)
            hiero.ui.insertMenuAction(createCompGlobalAction,
                                      fileMenu.menu(),
                                      after='foundry.project.export')

        if createCompSpecialAction:
            createCompSpecialAction.triggered.connect(self.onCreateCompSpecial)
            hiero.ui.insertMenuAction(createCompSpecialAction,
                                      fileMenu.menu(),
                                      after='foundry.project.export')

    def onCreateComp(self):
        from .create_comp import CreateCompAction
        """ Callback from the global 'Add Effect' action. """
        activeSequence = hiero.ui.activeSequence()
        timelineEditor = hiero.ui.getTimelineEditor(activeSequence)
        if timelineEditor:

            selection = timelineEditor.selection()
            if selection:
                action = self.makeCreateCompAction(selection, CreateCompAction)
                action.doit()

    def onCreateCompSpecial(self):
        from .create_comp import CreateCompSpecialAction
        activeSequence = hiero.ui.activeSequence()
        timelineEditor = hiero.ui.getTimelineEditor(activeSequence)
        if timelineEditor:
            selection = timelineEditor.selection()
            if selection:
                action = self.makeCreateCompAction(selection, CreateCompSpecialAction)
                action.doit()

    def makeCreateCompAction(self, selection, objectType):
        """ Create an CreateCompAction from the given selection, and return it """
        # only handle selections of trackitems, clips, and sequence items
        clips = []
        sequences = []
        trackItems = []
        effectItems = []
        bins = []
        annotations = []
        self._findItems(selection, clips, sequences, trackItems,
                        bins, effectItems, annotations)
        return objectType(trackItems, effectItems, annotations, title='Create Comp')

    # override

    def binContextMenuEventHandler(self, event):
        pass

    # override

    def timelineContextMenuEventHandler(self, event):
        pass
