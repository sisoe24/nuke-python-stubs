# Type stubs for nuke 15.2v9. Generated; do not edit.

"""This package provides all the Nuke-specific functions and Classes.

Note: to support importing Nuke from an external Python interpreter, this package
is now called nuke_internal. Any internal Python code (particularly when imported
at application startup) should import this directly, and *not* 'import nuke'.

External scripts should 'import nuke' which imports everything through the nuke.py
wrapper script.
"""

from typing import Any
import nuke as _nuke
from . import callbacks as callbacks
from . import colorspaces as colorspaces
from . import curveknob as curveknob
from . import curvelib as curvelib
from . import executeInMain as executeInMain
from . import geo as geo
from . import localization as localization
from . import memory2 as memory2
from . import overrides as overrides
from . import rotopaint as rotopaint
from . import scripts as scripts
from . import splinewarp as splinewarp
from . import utils as utils
from nuke import AColor_Knob as AColor_Knob
from nuke import AnimationCurve as AnimationCurve
from nuke import AnimationKey as AnimationKey
from nuke import Array_Knob as Array_Knob
from nuke import Axis_Knob as Axis_Knob
from nuke import BBox_Knob as BBox_Knob
from nuke import BackdropNode as BackdropNode
from nuke import BeginTabGroup_Knob as BeginTabGroup_Knob
from nuke import Bitmask_Knob as Bitmask_Knob
from nuke import Boolean_Knob as Boolean_Knob
from nuke import Box as Box
from nuke import Box3_Knob as Box3_Knob
from nuke import CancelledError as CancelledError
from nuke import CascadingEnumeration_Knob as CascadingEnumeration_Knob
from nuke import ChannelMask_Knob as ChannelMask_Knob
from nuke import Channel_Knob as Channel_Knob
from nuke import ColorChip_Knob as ColorChip_Knob
from nuke import Color_Knob as Color_Knob
from nuke import Disable_Knob as Disable_Knob
from nuke import Double_Knob as Double_Knob
from nuke import EditableEnumeration_Knob as EditableEnumeration_Knob
from nuke import EndTabGroup_Knob as EndTabGroup_Knob
from nuke import Enumeration_Knob as Enumeration_Knob
from nuke import EvalString_Knob as EvalString_Knob
from nuke import Eyedropper_Knob as Eyedropper_Knob
from nuke import File_Knob as File_Knob
from nuke import Font_Knob as Font_Knob
from nuke import Format as Format
from nuke import Format_Knob as Format_Knob
from nuke import FrameRange as FrameRange
from nuke import FrameRanges as FrameRanges
from nuke import FreeType_Knob as FreeType_Knob
from nuke import GeoSelect_Knob as GeoSelect_Knob
from nuke import GeoSelection as GeoSelection
from nuke import GeoSelectionItem as GeoSelectionItem
from nuke import Gizmo as Gizmo
from nuke import GlobalsEnvironment as GlobalsEnvironment
from nuke import Group as Group
from nuke import Gsv_Knob as Gsv_Knob
from nuke import Hash as Hash
from nuke import Help_Knob as Help_Knob
from nuke import Histogram_Knob as Histogram_Knob
from nuke import IArray_Knob as IArray_Knob
from nuke import Info as Info
from nuke import Int_Knob as Int_Knob
from nuke import Keyer_Knob as Keyer_Knob
from nuke import Knob as Knob
from nuke import KnobType as KnobType
from nuke import Layer as Layer
from nuke import Link_Knob as Link_Knob
from nuke import LinkableKnobInfo as LinkableKnobInfo
from nuke import LiveGroup as LiveGroup
from nuke import LookupCurves_Knob as LookupCurves_Knob
from nuke import Lut as Lut
from nuke import Menu as Menu
from nuke import MenuBar as MenuBar
from nuke import MenuItem as MenuItem
from nuke import MultiView_Knob as MultiView_Knob
from nuke import Multiline_Eval_String_Knob as Multiline_Eval_String_Knob
from nuke import Node as Node
from nuke import NodeConstructor as NodeConstructor
from nuke import Nodes as Nodes
from nuke import Obsolete_Knob as Obsolete_Knob
from nuke import OneView_Knob as OneView_Knob
from nuke import OutputContext as OutputContext
from nuke import Panel as Panel
from nuke import PanelNode as PanelNode
from nuke import ParticleChannels_Knob as ParticleChannels_Knob
from nuke import Password_Knob as Password_Knob
from nuke import PathExpression_Knob as PathExpression_Knob
from nuke import Path_Knob as Path_Knob
from nuke import Precomp as Precomp
from nuke import ProgressTask as ProgressTask
from nuke import Pulldown_Knob as Pulldown_Knob
from nuke import PyCustom_Knob as PyCustom_Knob
from nuke import PyScript_Knob as PyScript_Knob
from nuke import PythonCustomKnob as PythonCustomKnob
from nuke import PythonKnob as PythonKnob
from nuke import Radio_Knob as Radio_Knob
from nuke import Range_Knob as Range_Knob
from nuke import Root as Root
from nuke import RunInMainThread as RunInMainThread
from nuke import Scale_Knob as Scale_Knob
from nuke import SceneGraph_Knob as SceneGraph_Knob
from nuke import SceneView_Knob as SceneView_Knob
from nuke import Script_Knob as Script_Knob
from nuke import String_Knob as String_Knob
from nuke import Tab_Knob as Tab_Knob
from nuke import Text_Knob as Text_Knob
from nuke import ToolBar as ToolBar
from nuke import Transform2d_Knob as Transform2d_Knob
from nuke import UV_Knob as UV_Knob
from nuke import Undo as Undo
from nuke import Unsigned_Knob as Unsigned_Knob
from nuke import View as View
from nuke import ViewView_Knob as ViewView_Knob
from nuke import Viewer as Viewer
from nuke import ViewerProcess as ViewerProcess
from nuke import ViewerWindow as ViewerWindow
from nuke import WH_Knob as WH_Knob
from nuke import XYZ_Knob as XYZ_Knob
from nuke import XY_Knob as XY_Knob
from nuke import activeGroup as activeGroup
from nuke import activeViewer as activeViewer
from nuke import addFavoriteDir as addFavoriteDir
from nuke import addFormat as addFormat
from nuke import addNodePresetExcludePaths as addNodePresetExcludePaths
from nuke import addSequenceFileExtension as addSequenceFileExtension
from nuke import addToolsetExcludePaths as addToolsetExcludePaths
from nuke import addView as addView
from nuke import alert as alert
from nuke import allNodes as allNodes
from nuke import animation as animation
from nuke import animationEnd as animationEnd
from nuke import animationIncrement as animationIncrement
from nuke import animationStart as animationStart
from nuke import animations as animations
from nuke import applyPreset as applyPreset
from nuke import applyUserPreset as applyUserPreset
from nuke import ask as ask
from nuke import askWithCancel as askWithCancel
from nuke import autoplace as autoplace
from nuke import autoplaceSnap as autoplaceSnap
from nuke import autoplace_all as autoplace_all
from nuke import autoplace_snap_all as autoplace_snap_all
from nuke import autoplace_snap_selected as autoplace_snap_selected
from nuke import cacheUsage as cacheUsage
from nuke import canCreateNode as canCreateNode
from nuke import cancel as cancel
from nuke import center as center
from nuke import channels as channels
from nuke import choice as choice
from nuke import clearAssetCache as clearAssetCache
from nuke import clearBlinkCache as clearBlinkCache
from nuke import clearDiskCache as clearDiskCache
from nuke import clearGeoSelection as clearGeoSelection
from nuke import clearRAMCache as clearRAMCache
from nuke import clearTabMenuFavorites as clearTabMenuFavorites
from nuke import clearTabMenuWeighting as clearTabMenuWeighting
from nuke import clone as clone
from nuke import cloneSelected as cloneSelected
from nuke import collapseToGroup as collapseToGroup
from nuke import collapseToLiveGroup as collapseToLiveGroup
from nuke import collapseToVariableGroup as collapseToVariableGroup
from nuke import connectNodes as connectNodes
from nuke import connectViewer as connectViewer
from nuke import createLiveInput as createLiveInput
from nuke import createNode as createNode
from nuke import createScenefileBrowser as createScenefileBrowser
from nuke import createToolset as createToolset
from nuke import critical as critical
from nuke import debug as debug
from nuke import defaultFontPathname as defaultFontPathname
from nuke import defaultNodeColor as defaultNodeColor
from nuke import delete as delete
from nuke import deletePreset as deletePreset
from nuke import deleteUserPreset as deleteUserPreset
from nuke import deleteView as deleteView
from nuke import display as display
from nuke import duplicateSelectedNodes as duplicateSelectedNodes
from nuke import endGroup as endGroup
from nuke import error as error
from nuke import execute as execute
from nuke import executeBackgroundNuke as executeBackgroundNuke
from nuke import executeMultiple as executeMultiple
from nuke import executing as executing
from nuke import exists as exists
from nuke import expandSelectedGroup as expandSelectedGroup
from nuke import expr as expr
from nuke import expression as expression
from nuke import extractSelected as extractSelected
from nuke import filename as filename
from nuke import forceClone as forceClone
from nuke import forceLoad as forceLoad
from nuke import fork as fork
from nuke import formats as formats
from nuke import frame as frame
from nuke import fromNode as fromNode
from nuke import getAllUserPresets as getAllUserPresets
from nuke import getClipname as getClipname
from nuke import getColor as getColor
from nuke import getDeletedPresets as getDeletedPresets
from nuke import getFileNameList as getFileNameList
from nuke import getFilename as getFilename
from nuke import getFonts as getFonts
from nuke import getFramesAndViews as getFramesAndViews
from nuke import getGeoSelection as getGeoSelection
from nuke import getInput as getInput
from nuke import getNodeClassName as getNodeClassName
from nuke import getNodePresetExcludePaths as getNodePresetExcludePaths
from nuke import getNodePresetID as getNodePresetID
from nuke import getOcioColorSpaces as getOcioColorSpaces
from nuke import getPaneFor as getPaneFor
from nuke import getPresetKnobValues as getPresetKnobValues
from nuke import getPresets as getPresets
from nuke import getPresetsMenu as getPresetsMenu
from nuke import getReadFileKnob as getReadFileKnob
from nuke import getRenderProgress as getRenderProgress
from nuke import getToolsetExcludePaths as getToolsetExcludePaths
from nuke import getUserPresetKnobValues as getUserPresetKnobValues
from nuke import getUserPresets as getUserPresets
from nuke import hotkeys as hotkeys
from nuke import inputs as inputs
from nuke import invertSelection as invertSelection
from nuke import knob as knob
from nuke import knobDefault as knobDefault
from nuke import knobTooltip as knobTooltip
from nuke import lastHitGroup as lastHitGroup
from nuke import layers as layers
from nuke import licenseInfo as licenseInfo
from nuke import link as link
from nuke import linkSelected as linkSelected
from nuke import load as load
from nuke import loadToolset as loadToolset
from nuke import localiseFiles as localiseFiles
from nuke import localizationEnabled as localizationEnabled
from nuke import makeGroup as makeGroup
from nuke import maxPerformanceInfo as maxPerformanceInfo
from nuke import menu as menu
from nuke import message as message
from nuke import modified as modified
from nuke import nodeAtPath as nodeAtPath
from nuke import nodeCopy as nodeCopy
from nuke import nodeDelete as nodeDelete
from nuke import nodePaste as nodePaste
from nuke import nodeTypes as nodeTypes
from nuke import nodesSelected as nodesSelected
from nuke import numvalue as numvalue
from nuke import oculaPresent as oculaPresent
from nuke import ofxAddPluginAliasExclusion as ofxAddPluginAliasExclusion
from nuke import ofxMenu as ofxMenu
from nuke import ofxPluginPath as ofxPluginPath
from nuke import ofxRemovePluginAliasExclusion as ofxRemovePluginAliasExclusion
from nuke import openPanels as openPanels
from nuke import pan as pan
from nuke import performanceProfileFilename as performanceProfileFilename
from nuke import pluginExists as pluginExists
from nuke import pluginInstallLocation as pluginInstallLocation
from nuke import pluginPath as pluginPath
from nuke import plugins as plugins
from nuke import recentFile as recentFile
from nuke import redo as redo
from nuke import registerFlipbook as registerFlipbook
from nuke import removeFavoriteDir as removeFavoriteDir
from nuke import render as render
from nuke import rescanFontFolders as rescanFontFolders
from nuke import resetPerformanceTimers as resetPerformanceTimers
from nuke import resumePathProcessing as resumePathProcessing
from nuke import root as root
from nuke import runIn as runIn
from nuke import sample as sample
from nuke import saveEventGraphTimers as saveEventGraphTimers
from nuke import saveToScript as saveToScript
from nuke import saveUserPreset as saveUserPreset
from nuke import scriptClear as scriptClear
from nuke import scriptName as scriptName
from nuke import scriptNew as scriptNew
from nuke import scriptReadFile as scriptReadFile
from nuke import scriptReadText as scriptReadText
from nuke import scriptSave as scriptSave
from nuke import scriptSaveAs as scriptSaveAs
from nuke import scriptSaveToTemp as scriptSaveToTemp
from nuke import scriptSource as scriptSource
from nuke import selectAll as selectAll
from nuke import selectPattern as selectPattern
from nuke import selectSimilar as selectSimilar
from nuke import selectedNode as selectedNode
from nuke import selectedNodes as selectedNodes
from nuke import setGeoSelection as setGeoSelection
from nuke import setPreset as setPreset
from nuke import setReadOnlyPresets as setReadOnlyPresets
from nuke import setUserPreset as setUserPreset
from nuke import show as show
from nuke import showBookmarkChooser as showBookmarkChooser
from nuke import showCreateViewsDialog as showCreateViewsDialog
from nuke import showDag as showDag
from nuke import showInfo as showInfo
from nuke import showSettings as showSettings
from nuke import splayNodes as splayNodes
from nuke import startEventGraphTimers as startEventGraphTimers
from nuke import startPerformanceTimers as startPerformanceTimers
from nuke import stopEventGraphTimers as stopEventGraphTimers
from nuke import stopPerformanceTimers as stopPerformanceTimers
from nuke import stripFrameRange as stripFrameRange
from nuke import suspendPathProcessing as suspendPathProcessing
from nuke import tabClose as tabClose
from nuke import tabNext as tabNext
from nuke import tcl as tcl
from nuke import thisClass as thisClass
from nuke import thisGroup as thisGroup
from nuke import thisKnob as thisKnob
from nuke import thisNode as thisNode
from nuke import thisPane as thisPane
from nuke import thisParent as thisParent
from nuke import thisRoot as thisRoot
from nuke import thisView as thisView
from nuke import toNode as toNode
from nuke import toggleFullscreen as toggleFullscreen
from nuke import toggleViewers as toggleViewers
from nuke import toolbar as toolbar
from nuke import tprint as tprint
from nuke import undo as undo
from nuke import unlinkSelected as unlinkSelected
from nuke import usingOcio as usingOcio
from nuke import usingPerformanceTimers as usingPerformanceTimers
from nuke import value as value
from nuke import views as views
from nuke import waitForThreadsToFinish as waitForThreadsToFinish
from nuke import warning as warning
from nuke import zoom as zoom
from nuke import zoomToFitSelected as zoomToFitSelected
from nuke_internal.callbacks import addAfterBackgroundFrameRender as addAfterBackgroundFrameRender
from nuke_internal.callbacks import addAfterBackgroundRender as addAfterBackgroundRender
from nuke_internal.callbacks import addAfterFrameRender as addAfterFrameRender
from nuke_internal.callbacks import addAfterRecording as addAfterRecording
from nuke_internal.callbacks import addAfterRender as addAfterRender
from nuke_internal.callbacks import addAfterReplay as addAfterReplay
from nuke_internal.callbacks import addAutoSaveDeleteFilter as addAutoSaveDeleteFilter
from nuke_internal.callbacks import addAutoSaveFilter as addAutoSaveFilter
from nuke_internal.callbacks import addAutoSaveRestoreFilter as addAutoSaveRestoreFilter
from nuke_internal.callbacks import addAutolabel as addAutolabel
from nuke_internal.callbacks import addBeforeBackgroundRender as addBeforeBackgroundRender
from nuke_internal.callbacks import addBeforeFrameRender as addBeforeFrameRender
from nuke_internal.callbacks import addBeforeRecording as addBeforeRecording
from nuke_internal.callbacks import addBeforeRender as addBeforeRender
from nuke_internal.callbacks import addBeforeReplay as addBeforeReplay
from nuke_internal.callbacks import addFilenameFilter as addFilenameFilter
from nuke_internal.callbacks import addKnobChanged as addKnobChanged
from nuke_internal.callbacks import addOnCreate as addOnCreate
from nuke_internal.callbacks import addOnDestroy as addOnDestroy
from nuke_internal.callbacks import addOnScriptClose as addOnScriptClose
from nuke_internal.callbacks import addOnScriptLoad as addOnScriptLoad
from nuke_internal.callbacks import addOnScriptSave as addOnScriptSave
from nuke_internal.callbacks import addOnUserCreate as addOnUserCreate
from nuke_internal.callbacks import addRenderProgress as addRenderProgress
from nuke_internal.callbacks import addUpdateUI as addUpdateUI
from nuke_internal.callbacks import addValidateFilename as addValidateFilename
from nuke_internal.callbacks import afterBackgroundFrameRender as afterBackgroundFrameRender
from nuke_internal.callbacks import afterBackgroundRender as afterBackgroundRender
from nuke_internal.callbacks import afterFrameRender as afterFrameRender
from nuke_internal.callbacks import afterRecording as afterRecording
from nuke_internal.callbacks import afterRender as afterRender
from nuke_internal.callbacks import afterReplay as afterReplay
from nuke_internal.callbacks import autoSaveDeleteFilter as autoSaveDeleteFilter
from nuke_internal.callbacks import autoSaveFilter as autoSaveFilter
from nuke_internal.callbacks import autoSaveRestoreFilter as autoSaveRestoreFilter
from nuke_internal.callbacks import autolabel as autolabel
from nuke_internal.callbacks import beforeBackgroundRender as beforeBackgroundRender
from nuke_internal.callbacks import beforeFrameRender as beforeFrameRender
from nuke_internal.callbacks import beforeRecording as beforeRecording
from nuke_internal.callbacks import beforeRender as beforeRender
from nuke_internal.callbacks import beforeReplay as beforeReplay
from nuke_internal.callbacks import filenameFilter as filenameFilter
from nuke_internal.callbacks import knobChanged as knobChanged
from nuke_internal.callbacks import onCreate as onCreate
from nuke_internal.callbacks import onDestroy as onDestroy
from nuke_internal.callbacks import onScriptClose as onScriptClose
from nuke_internal.callbacks import onScriptLoad as onScriptLoad
from nuke_internal.callbacks import onScriptSave as onScriptSave
from nuke_internal.callbacks import onUserCreate as onUserCreate
from nuke_internal.callbacks import removeAfterBackgroundFrameRender as removeAfterBackgroundFrameRender
from nuke_internal.callbacks import removeAfterBackgroundRender as removeAfterBackgroundRender
from nuke_internal.callbacks import removeAfterFrameRender as removeAfterFrameRender
from nuke_internal.callbacks import removeAfterRecording as removeAfterRecording
from nuke_internal.callbacks import removeAfterRender as removeAfterRender
from nuke_internal.callbacks import removeAfterReplay as removeAfterReplay
from nuke_internal.callbacks import removeAutoSaveDeleteFilter as removeAutoSaveDeleteFilter
from nuke_internal.callbacks import removeAutoSaveFilter as removeAutoSaveFilter
from nuke_internal.callbacks import removeAutoSaveRestoreFilter as removeAutoSaveRestoreFilter
from nuke_internal.callbacks import removeAutolabel as removeAutolabel
from nuke_internal.callbacks import removeBeforeBackgroundRender as removeBeforeBackgroundRender
from nuke_internal.callbacks import removeBeforeFrameRender as removeBeforeFrameRender
from nuke_internal.callbacks import removeBeforeRecording as removeBeforeRecording
from nuke_internal.callbacks import removeBeforeRender as removeBeforeRender
from nuke_internal.callbacks import removeBeforeReplay as removeBeforeReplay
from nuke_internal.callbacks import removeFilenameFilter as removeFilenameFilter
from nuke_internal.callbacks import removeFilenameValidate as removeFilenameValidate
from nuke_internal.callbacks import removeKnobChanged as removeKnobChanged
from nuke_internal.callbacks import removeOnCreate as removeOnCreate
from nuke_internal.callbacks import removeOnDestroy as removeOnDestroy
from nuke_internal.callbacks import removeOnScriptClose as removeOnScriptClose
from nuke_internal.callbacks import removeOnScriptLoad as removeOnScriptLoad
from nuke_internal.callbacks import removeOnScriptSave as removeOnScriptSave
from nuke_internal.callbacks import removeOnUserCreate as removeOnUserCreate
from nuke_internal.callbacks import removeRenderProgress as removeRenderProgress
from nuke_internal.callbacks import removeUpdateUI as removeUpdateUI
from nuke_internal.callbacks import renderProgress as renderProgress
from nuke_internal.callbacks import updateUI as updateUI
from nuke_internal.callbacks import validateFilename as validateFilename
from nuke_internal.colorspaces import ColorspaceLookupError as ColorspaceLookupError
from nuke_internal.colorspaces import addDefaultColorspaceMapper as addDefaultColorspaceMapper
from nuke_internal.colorspaces import defaultColorspaceMapper as defaultColorspaceMapper
from nuke_internal.colorspaces import getColorspaceList as getColorspaceList
from nuke_internal.colorspaces import removeDefaultColorspaceMapper as removeDefaultColorspaceMapper
from nuke_internal.executeInMain import executeInMainThread as executeInMainThread
from nuke_internal.executeInMain import executeInMainThreadWithResult as executeInMainThreadWithResult
from nuke_internal.overrides import dependencies as dependencies
from nuke_internal.overrides import dependentNodes as dependentNodes
from nuke_internal.overrides import pluginAddPath as pluginAddPath
from nuke_internal.overrides import pluginAppendPath as pluginAppendPath
from nuke_internal.overrides import selectConnectedNodes as selectConnectedNodes
from nuke_internal.scripts import scriptSaveAndClear as scriptSaveAndClear
from nuke_internal.utils import FnPySingleton as FnPySingleton
from nuke_internal.utils import loadModuleFromPath as loadModuleFromPath
from nuke_internal.utils import script_directory as script_directory

ADD_VIEWS: int
AFTER_CONST: int
AFTER_LINEAR: int
ALL: int
ALWAYS_SAVE: int
BEFORE_CONST: int
BEFORE_LINEAR: int
BREAK: int
CATMULL_ROM: int
CONSTANT: int
CUBIC: int
DISABLED: int
DONT_CREATE_VIEWS: int
DONT_SAVE_TO_NODEPRESET: int
DO_NOT_READ: int
DO_NOT_WRITE: int
ENDLINE: int
EXE_PATH: str
EXPAND_TO_WIDTH: int
EXPRESSIONS: int
FLAGS_LOCKED: int
FLOAT: int
FONT: int
GEO: int
GUI: bool
HIDDEN_INPUTS: int
HORIZONTAL: int
IMAGE: int
INPUTS: int
INT16: int
INT8: int
INTERACTIVE: bool
INVALIDHINT: int
INVISIBLE: int
KNOB_CHANGED_ALWAYS: int
KNOB_CHANGED_RECURSIVE: int
KNOB_CHANGED_RIGHTCONTEXT: int
LINEAR: int
LINKINPUTS: int
LINKNODE_INPUTS: int
LIVEGROUP_CALLBACK_CAN_MAKE_EDITABLE: str
LIVEGROUP_CALLBACK_CAN_PUBLISH: str
LIVEGROUP_CALLBACK_MADE_EDITABLE: str
LIVEGROUP_CALLBACK_PUBLISHED: str
LIVEGROUP_CALLBACK_RELOADED: str
LOG: int
MATCH_CLASS: int
MATCH_COLOR: int
MATCH_LABEL: int
MONITOR: int
NODIR: int
NOREADERWRITER: int
NO_ANIMATION: int
NO_CHECKMARKS: int
NO_MULTIVIEW: int
NO_POSTAGESTAMPS: bool
NO_UNDO: int
NUKE_VERSION_DATE: str
NUKE_VERSION_MAJOR: int
NUKE_VERSION_MINOR: int
NUKE_VERSION_PHASE: str
NUKE_VERSION_PHASENUMBER: int
NUKE_VERSION_RELEASE: int
NUKE_VERSION_STRING: str
NUM_CPUS: int
NUM_INTERPOLATIONS: int
PLUGIN_EXT: str
PRECOMP_CALLBACK_OPENED: str
PREPEND: int
PROFILE_ENGINE: int
PROFILE_REQUEST: int
PROFILE_STORE: int
PROFILE_VALIDATE: int
PYTHON: int
READ_ONLY: int
READ_ONLY_IN_SCRIPTS: int
REGISTERED: int
REPLACE: int
REPLACE_VIEWS: int
SAVE_MENU: int
SCRIPT: int
SINGLE_SELECTION_ONLY: int
SMOOTH: int
STARTLINE: int
STORE_INTEGER: int
STRIP_CASCADE_PREFIX: int
TABBEGINCLOSEDGROUP: int
TABBEGINGROUP: int
TABENDGROUP: int
TABKNOB: int
THREADS: int
TO_SCRIPT: int
TO_VALUE: int
USER_SET_SLOPE: int
VIEWER: int
VIEW_NAMES: str
WRITE_ALL: int
WRITE_NON_DEFAULT_ONLY: int
WRITE_USER_KNOB_DEFS: int
afterBackgroundFrameRenders: list
afterBackgroundRenders: list
afterFrameRenders: dict
afterRenders: dict
autoSaveDeleteFilters: dict
autoSaveFilters: dict
autoSaveRestoreFilters: dict
autolabels: dict
beforeBackgroundRenders: list
beforeFrameRenders: dict
beforeRenders: dict
defaultLUTMappers: dict
env: _nuke.GlobalsEnvironment
filenameFilters: dict
knobChangeds: dict
nodes: _nuke.Nodes
onCreates: dict
onDestroys: dict
onScriptCloses: dict
onScriptLoads: dict
onScriptSaves: dict
onUserCreates: dict
rawArgs: list
renderProgresses: dict
untitled: str
updateUIs: dict
validateFilenames: dict

def import_module(name: Any, filterRule: Any) -> None: ...

def restoreWindowLayout(i: Any) -> None:
    """restoreWindowLayout(i) -> None.

    Restores a saved window layout.

    :param i: Layout number
    :return: None
    """

def saveWindowLayout(i: Any = ...) -> None:
    """saveWindowLayout(i=-1) -> None

    Saves the current window layout.

    :param i: Optional layout index. If this is omitted or set to a negative value, save as the default layout.
    :return: None.
    """

def scriptClose(*args: Any, **kwargs: Any) -> Any:
    """Close the current script or group. Returns True if successful."""

def scriptExit(*args: Any, **kwargs: Any) -> Any:
    """Exit Nuke."""

def scriptOpen(*args: Any, **kwargs: Any) -> Any:
    """Opens a new script containing the contents of the named file."""
