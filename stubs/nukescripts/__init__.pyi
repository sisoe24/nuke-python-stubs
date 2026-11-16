# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from typing import final
import nukescripts.flipbooking as _nukescripts_flipbooking
from . import ViewerProcess as ViewerProcess
from . import all_plugins as all_plugins
from . import animation as animation
from . import applymaterial as applymaterial
from . import autobackdrop as autobackdrop
from . import blinkscripteditor as blinkscripteditor
from . import bookmarks as bookmarks
from . import cache as cache
from . import camera as camera
from . import camerapresets as camerapresets
from . import cameratracker as cameratracker
from . import captureViewer as captureViewer
from . import cattery as cattery
from . import create as create
from . import crop as crop
from . import drop as drop
from . import edit as edit
from . import execute as execute
from . import flags as flags
from . import flip as flip
from . import flipbooking as flipbooking
from . import fnFlipbookRenderer as fnFlipbookRenderer
from . import frame as frame
from . import framerangepanel as framerangepanel
from . import group as group
from . import hardwareinfo as hardwareinfo
from . import importexport as importexport
from . import info as info
from . import localisationprefs as localisationprefs
from . import misc as misc
from . import modelbuilder as modelbuilder
from . import nodepresets as nodepresets
from . import nodes as nodes
from . import nukeprofiler as nukeprofiler
from . import openurl as openurl
from . import panels as panels
from . import plugin_menu as plugin_menu
from . import precomp as precomp
from . import psd as psd
from . import pyAppUtils as pyAppUtils
from . import pythonhighlighter as pythonhighlighter
from . import reads as reads
from . import readviewscheck as readviewscheck
from . import renderdialog as renderdialog
from . import renderpanel as renderpanel
from . import script as script
from . import scripteditorknob as scripteditorknob
from . import searchreplace as searchreplace
from . import select as select
from . import snap3d as snap3d
from . import stereo as stereo
from . import toolbars as toolbars
from . import toolsets as toolsets
from . import udim as udim
from . import unrealreader as unrealreader
from . import usdhighlighter as usdhighlighter
from . import utils as utils
from . import version as version
from . import viewsettingsprefs as viewsettingsprefs
from nuke_internal.executeInMain import executeInMainThread as executeInMainThread
from nuke_internal.executeInMain import executeInMainThreadWithResult as executeInMainThreadWithResult
from nukescripts.all_plugins import load_all_plugins as load_all_plugins
from nukescripts.animation import animation_loop as animation_loop
from nukescripts.animation import animation_move as animation_move
from nukescripts.animation import animation_negate as animation_negate
from nukescripts.animation import animation_reverse as animation_reverse
from nukescripts.autobackdrop import autoBackdrop as autoBackdrop
from nukescripts.autobackdrop import nodeIsInside as nodeIsInside
from nukescripts.blinkscripteditor import InputHighlighter as InputHighlighter
from nukescripts.blinkscripteditor import LineNumberArea as LineNumberArea
from nukescripts.blinkscripteditor import ScriptInputArea as ScriptInputArea
from nukescripts.cache import ReportTree as ReportTree
from nukescripts.cache import ValueLabel as ValueLabel
from nukescripts.cache import clearAllCaches as clearAllCaches
from nukescripts.cache import humanReadable as humanReadable
from nukescripts.cache import showReportDialog as showReportDialog
from nukescripts.camera import camera_down as camera_down
from nukescripts.camera import camera_up as camera_up
from nukescripts.camera import create_camera_here as create_camera_here
from nukescripts.create import createNodeLocal as createNodeLocal
from nukescripts.create import create_curve as create_curve
from nukescripts.create import create_read as create_read
from nukescripts.create import create_viewsplitjoin as create_viewsplitjoin
from nukescripts.create import isAudioFilename as isAudioFilename
from nukescripts.create import isDeepFilename as isDeepFilename
from nukescripts.create import isGeoFilename as isGeoFilename
from nukescripts.create import isSceneBrowserFilename as isSceneBrowserFilename
from nukescripts.crop import autocrop as autocrop
from nukescripts.drop import addDropDataCallback as addDropDataCallback
from nukescripts.drop import dropData as dropData
from nukescripts.edit import branch as branch
from nukescripts.edit import cut_paste_file as cut_paste_file
from nukescripts.edit import extract as extract
from nukescripts.edit import node_copypaste as node_copypaste
from nukescripts.edit import remove_inputs as remove_inputs
from nukescripts.execute import execute_panel as execute_panel
from nukescripts.flags import KnobFlagClearer as KnobFlagClearer
from nukescripts.flags import get_fully_qualified_name as get_fully_qualified_name
from nukescripts.flags import toggle as toggle
from nukescripts.flip import flipbook as flipbook
from nukescripts.flipbooking import FlipbookApplication as FlipbookApplication
from nukescripts.flipbooking import FlipbookFactory as FlipbookFactory
from nukescripts.flipbooking import FlipbookLUTPathRegistry as FlipbookLUTPathRegistry
from nukescripts.flipbooking import getLUTPath as getLUTPath
from nukescripts.flipbooking import register as register
from nukescripts.flipbooking import registerLUTPath as registerLUTPath
from nukescripts.fnFlipbookRenderer import getFlipbookRenderer as getFlipbookRenderer
from nukescripts.frame import goto_frame as goto_frame
from nukescripts.frame import replaceHashes as replaceHashes
from nukescripts.framerangepanel import FrameRangePanel as FrameRangePanel
from nukescripts.group import groupmake as groupmake
from nukescripts.importexport import export_nodes_as_script as export_nodes_as_script
from nukescripts.importexport import import_boujou as import_boujou
from nukescripts.importexport import import_script as import_script
from nukescripts.info import getallnodeinfo as getallnodeinfo
from nukescripts.info import infoviewer as infoviewer
from nukescripts.misc import clear_selection_recursive as clear_selection_recursive
from nukescripts.misc import connect_selected_to_viewer as connect_selected_to_viewer
from nukescripts.misc import copy_knobs as copy_knobs
from nukescripts.misc import declone as declone
from nukescripts.misc import goofy_title as goofy_title
from nukescripts.misc import print_callback_info as print_callback_info
from nukescripts.misc import showname as showname
from nukescripts.misc import swapAB as swapAB
from nukescripts.nodepresets import CreateNodePresetsPanel as CreateNodePresetsPanel
from nukescripts.nodepresets import PresetsDeletePanel as PresetsDeletePanel
from nukescripts.nodepresets import PresetsLoadPanel as PresetsLoadPanel
from nukescripts.nodepresets import UserPresetsDeletePanel as UserPresetsDeletePanel
from nukescripts.nodepresets import UserPresetsLoadPanel as UserPresetsLoadPanel
from nukescripts.nodepresets import buildPresetDeletePanel as buildPresetDeletePanel
from nukescripts.nodepresets import buildPresetFileList as buildPresetFileList
from nukescripts.nodepresets import buildPresetLoadPanel as buildPresetLoadPanel
from nukescripts.nodepresets import buildPresetSavePanel as buildPresetSavePanel
from nukescripts.nodepresets import buildUserPresetDeletePanel as buildUserPresetDeletePanel
from nukescripts.nodepresets import buildUserPresetLoadPanel as buildUserPresetLoadPanel
from nukescripts.nodepresets import createNodePreset as createNodePreset
from nukescripts.nodepresets import createNodePresetsMenu as createNodePresetsMenu
from nukescripts.nodepresets import deleteNodePreset as deleteNodePreset
from nukescripts.nodepresets import deleteUserNodePreset as deleteUserNodePreset
from nukescripts.nodepresets import getItemDirName as getItemDirName
from nukescripts.nodepresets import getNukeUserFolder as getNukeUserFolder
from nukescripts.nodepresets import populatePresetsMenu as populatePresetsMenu
from nukescripts.nodepresets import processPresetFile as processPresetFile
from nukescripts.nodepresets import saveNodePresets as saveNodePresets
from nukescripts.nodes import color_nodes as color_nodes
from nukescripts.nodes import node_delete as node_delete
from nukescripts.nukeprofiler import NukeProfiler as NukeProfiler
from nukescripts.openurl import start as start
from nukescripts.panels import PythonPanel as PythonPanel
from nukescripts.panels import PythonPanelKnobChanged as PythonPanelKnobChanged
from nukescripts.panels import WidgetKnob as WidgetKnob
from nukescripts.panels import registerPanel as registerPanel
from nukescripts.panels import registerWidgetAsPanel as registerWidgetAsPanel
from nukescripts.panels import restorePanel as restorePanel
from nukescripts.panels import unregisterPanel as unregisterPanel
from nukescripts.plugin_menu import update_plugin_menu as update_plugin_menu
from nukescripts.precomp import PrecompOptions as PrecompOptions
from nukescripts.precomp import PrecompOptionsDialog as PrecompOptionsDialog
from nukescripts.precomp import precomp_copyToGroup as precomp_copyToGroup
from nukescripts.precomp import precomp_open as precomp_open
from nukescripts.precomp import precomp_render as precomp_render
from nukescripts.precomp import precomp_selected as precomp_selected
from nukescripts.pythonhighlighter import PythonHighlighter as PythonHighlighter
from nukescripts.reads import get_reads as get_reads
from nukescripts.renderdialog import DialogState as DialogState
from nukescripts.renderdialog import ExecuteDialog as ExecuteDialog
from nukescripts.renderdialog import FlipbookDialog as FlipbookDialog
from nukescripts.renderdialog import RenderDialog as RenderDialog
from nukescripts.renderdialog import ViewerCaptureDialog as ViewerCaptureDialog
from nukescripts.renderdialog import ViewerCaptureDialogThread as ViewerCaptureDialogThread
from nukescripts.renderdialog import bboxToTopLeft as bboxToTopLeft
from nukescripts.renderdialog import setFlipbookDefaultOption as setFlipbookDefaultOption
from nukescripts.renderdialog import setRenderDialogDefaultOption as setRenderDialogDefaultOption
from nukescripts.renderdialog import showExecuteDialog as showExecuteDialog
from nukescripts.renderdialog import showFlipbookDialog as showFlipbookDialog
from nukescripts.renderdialog import showFlipbookDialogForSelected as showFlipbookDialogForSelected
from nukescripts.renderdialog import showRenderDialog as showRenderDialog
from nukescripts.renderdialog import showViewerCaptureDialog as showViewerCaptureDialog
from nukescripts.renderpanel import cache_particles_panel as cache_particles_panel
from nukescripts.renderpanel import render_panel as render_panel
from nukescripts.script import VersionConflictDialog as VersionConflictDialog
from nukescripts.script import VersionHelper as VersionHelper
from nukescripts.script import findMaxVersionForFileName as findMaxVersionForFileName
from nukescripts.script import get_script_data as get_script_data
from nukescripts.script import script_and_write_nodes_version_up as script_and_write_nodes_version_up
from nukescripts.script import script_command as script_command
from nukescripts.script import script_data as script_data
from nukescripts.script import script_directory as script_directory
from nukescripts.script import script_version_up as script_version_up
from nukescripts.script import set_fileknob_version as set_fileknob_version
from nukescripts.script import timeline_write_version_set as timeline_write_version_set
from nukescripts.scripteditorknob import ScriptEditor as ScriptEditor
from nukescripts.scripteditorknob import ScriptEditorWidgetKnob as ScriptEditorWidgetKnob
from nukescripts.scripteditorknob import makeScriptEditorKnob as makeScriptEditorKnob
from nukescripts.searchreplace import search_replace as search_replace
from nukescripts.select import select_by_name as select_by_name
from nukescripts.select import select_similar as select_similar
from nukescripts.snap3d import VertexInfo as VertexInfo
from nukescripts.snap3d import VertexSelection as VertexSelection
from nukescripts.snap3d import addSnapFunc as addSnapFunc
from nukescripts.snap3d import allNodes as allNodes
from nukescripts.snap3d import allNodesWithGeoSelectKnob as allNodesWithGeoSelectKnob
from nukescripts.snap3d import anySelectedPoint as anySelectedPoint
from nukescripts.snap3d import anySelectedVertexInfo as anySelectedVertexInfo
from nukescripts.snap3d import averageNormal as averageNormal
from nukescripts.snap3d import calcAveragePosition as calcAveragePosition
from nukescripts.snap3d import calcBounds as calcBounds
from nukescripts.snap3d import calcRotationVector as calcRotationVector
from nukescripts.snap3d import callSnapFunc as callSnapFunc
from nukescripts.snap3d import cameraProjectionMatrix as cameraProjectionMatrix
from nukescripts.snap3d import checkAllPointCollinear as checkAllPointCollinear
from nukescripts.snap3d import degrees as degrees
from nukescripts.snap3d import fuzzyIsZero as fuzzyIsZero
from nukescripts.snap3d import fuzzyVector3Add as fuzzyVector3Add
from nukescripts.snap3d import getAxisKnobPrefix as getAxisKnobPrefix
from nukescripts.snap3d import getSelection as getSelection
from nukescripts.snap3d import leastSignificantAxis as leastSignificantAxis
from nukescripts.snap3d import planeRotation as planeRotation
from nukescripts.snap3d import projectPoint as projectPoint
from nukescripts.snap3d import projectPoints as projectPoints
from nukescripts.snap3d import projectSelectedPoints as projectSelectedPoints
from nukescripts.snap3d import radians as radians
from nukescripts.snap3d import rotateMatrixXYZ as rotateMatrixXYZ
from nukescripts.snap3d import rotateMatrixZXY as rotateMatrixZXY
from nukescripts.snap3d import rotatePivotSelectionToPoints as rotatePivotSelectionToPoints
from nukescripts.snap3d import rotatePivotToPoints as rotatePivotToPoints
from nukescripts.snap3d import rotatePivotToPointsVerified as rotatePivotToPointsVerified
from nukescripts.snap3d import rotateToPointsVerified as rotateToPointsVerified
from nukescripts.snap3d import scaleToPointsVerified as scaleToPointsVerified
from nukescripts.snap3d import scalingMatrix as scalingMatrix
from nukescripts.snap3d import selectedPoints as selectedPoints
from nukescripts.snap3d import selectedVertexInfos as selectedVertexInfos
from nukescripts.snap3d import transformMatrix as transformMatrix
from nukescripts.snap3d import translateMatrix as translateMatrix
from nukescripts.snap3d import translatePivotSelectionToPoints as translatePivotSelectionToPoints
from nukescripts.snap3d import translatePivotToPoints as translatePivotToPoints
from nukescripts.snap3d import translatePivotToPointsVerified as translatePivotToPointsVerified
from nukescripts.snap3d import translateRotatePivot as translateRotatePivot
from nukescripts.snap3d import translateRotatePivotSelectionToPoints as translateRotatePivotSelectionToPoints
from nukescripts.snap3d import translateRotatePivotToPoints as translateRotatePivotToPoints
from nukescripts.snap3d import translateRotatePivotToPointsVerified as translateRotatePivotToPointsVerified
from nukescripts.snap3d import translateRotateScaleSelectionToPoints as translateRotateScaleSelectionToPoints
from nukescripts.snap3d import translateRotateScaleThisNodeToPoints as translateRotateScaleThisNodeToPoints
from nukescripts.snap3d import translateRotateScaleToPoints as translateRotateScaleToPoints
from nukescripts.snap3d import translateRotateScaleToPointsVerified as translateRotateScaleToPointsVerified
from nukescripts.snap3d import translateRotateSelectionToPoints as translateRotateSelectionToPoints
from nukescripts.snap3d import translateRotateThisNodeToPoints as translateRotateThisNodeToPoints
from nukescripts.snap3d import translateRotateToPoints as translateRotateToPoints
from nukescripts.snap3d import translateRotateToPointsVerified as translateRotateToPointsVerified
from nukescripts.snap3d import translateSelectionToPoints as translateSelectionToPoints
from nukescripts.snap3d import translateThisNodeToPoints as translateThisNodeToPoints
from nukescripts.snap3d import translateToPoints as translateToPoints
from nukescripts.snap3d import translateToPointsVerified as translateToPointsVerified
from nukescripts.snap3d import transpose as transpose
from nukescripts.snap3d import verifyNodeOrder as verifyNodeOrder
from nukescripts.snap3d import verifyNodeToSnap as verifyNodeToSnap
from nukescripts.snap3d import verifyVertexSelection as verifyVertexSelection
from nukescripts.toolbars import createCurveTool as createCurveTool
from nukescripts.toolbars import createKronos as createKronos
from nukescripts.toolbars import createOFlow as createOFlow
from nukescripts.toolbars import createPlanartracker as createPlanartracker
from nukescripts.toolbars import createPrmanRender as createPrmanRender
from nukescripts.toolbars import createUVTile as createUVTile
from nukescripts.toolbars import create_matrix as create_matrix
from nukescripts.toolbars import create_time_warp as create_time_warp
from nukescripts.toolbars import setup_toolbars as setup_toolbars
from nukescripts.toolbars import toolbar_sticky_note as toolbar_sticky_note
from nukescripts.toolsets import CreateToolsetsPanel as CreateToolsetsPanel
from nukescripts.toolsets import addToolsetsPanel as addToolsetsPanel
from nukescripts.toolsets import checkForEmptyToolsetDirectories as checkForEmptyToolsetDirectories
from nukescripts.toolsets import createToolsetMenuItems as createToolsetMenuItems
from nukescripts.toolsets import createToolsetsMenu as createToolsetsMenu
from nukescripts.toolsets import deleteToolset as deleteToolset
from nukescripts.toolsets import populateToolsetsMenu as populateToolsetsMenu
from nukescripts.toolsets import refreshToolsetsMenu as refreshToolsetsMenu
from nukescripts.toolsets import traversePluginPaths as traversePluginPaths
from nukescripts.trackerlinkingdialog import LinkToTrackPanel as LinkToTrackPanel
from nukescripts.trackerlinkingdialog import trackerlinkingdialog as trackerlinkingdialog
from nukescripts.trackerlinkingdialog import trackerlinkingdialogexpressionx as trackerlinkingdialogexpressionx
from nukescripts.trackerlinkingdialog import trackerlinkingdialogexpressiony as trackerlinkingdialogexpressiony
from nukescripts.udim import TableDelegate as TableDelegate
from nukescripts.udim import UDIMErrorDialog as UDIMErrorDialog
from nukescripts.udim import UDIMFile as UDIMFile
from nukescripts.udim import UDIMOptionsDialog as UDIMOptionsDialog
from nukescripts.udim import allign_nodes as allign_nodes
from nukescripts.udim import checkUdimValue as checkUdimValue
from nukescripts.udim import findNextName as findNextName
from nukescripts.udim import parseUdimFile as parseUdimFile
from nukescripts.udim import splitInSequence as splitInSequence
from nukescripts.udim import udimStr as udimStr
from nukescripts.udim import udim_group as udim_group
from nukescripts.udim import udim_import as udim_import
from nukescripts.udim import uv2udim as uv2udim
from nukescripts.unrealreader import cameraClass as cameraClass
from nukescripts.unrealreader import createCamera as createCamera
from nukescripts.unrealreader import createReadNode as createReadNode
from nukescripts.unrealreader import new3D as new3D
from nukescripts.usdhighlighter import UsdHighlighter as UsdHighlighter
from nukescripts.utils import executeDeferred as executeDeferred
from nukescripts.utils import findNextNodeName as findNextNodeName
from nukescripts.version import version_down as version_down
from nukescripts.version import version_get as version_get
from nukescripts.version import version_latest as version_latest
from nukescripts.version import version_set as version_set
from nukescripts.version import version_up as version_up
import nukescripts as nukescripts

PLUGINS_FILTER: list
blinkFuncsColour: Any
blinkTypesColour: Any
commentsFgColour: Any
gFlipbookFactory: _nukescripts_flipbooking.FlipbookFactory
gFlipbookLUTPathRegistry: _nukescripts_flipbooking.FlipbookLUTPathRegistry
isHiero: bool
kCommandField: str
kwdsFgColour: Any
last_cmd: str
prev_inrange: str
prev_userrange: str
profileCategories: dict
snapFuncs: list
stringLiteralsFgColourDQ: Any
stringLiteralsFgColourSQ: Any

@final
class TracebackType:
    """TracebackType(tb_next, tb_frame, tb_lasti, tb_lineno)
    --

    Create a new traceback object.
    """
    tb_frame: Any
    tb_lasti: Any
    tb_lineno: Any
    tb_next: Any
    def __new__(cls, *args: Any, **kwargs: Any) -> TracebackType: ...
