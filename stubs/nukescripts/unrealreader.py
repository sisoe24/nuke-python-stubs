"""Functions used by the UnrealReader node"""

import os

import nuke
import nukescripts


def new3D(node):
    """Checks if the node is using the new 3D system."""
    new3DKnob = node.knob('new3D')
    return new3DKnob and bool(new3DKnob.getValue())


def cameraClass(node):
    """Returns the correct camera class for the 3D system in use."""
    return 'Camera4' if new3D(node) else 'Camera3'


def createCamera(unrealReaderNode):
    """Create a camera node based on the values set in the given unreal reader node"""
    x = unrealReaderNode.xpos()
    y = unrealReaderNode.ypos()
    w = unrealReaderNode.screenWidth()
    h = unrealReaderNode.screenHeight()
    m = int(x + w/2)

    camera = nuke.createNode(cameraClass(unrealReaderNode), '', False)
    camera.setInput(0, None)
    camera.setXYpos(m - int(camera.screenWidth()/2), y + w)

    link = False
    linkKnob = unrealReaderNode.knob('linkOutput')
    if linkKnob:
        link = bool(linkKnob.getValue())

    if link:
        # Set camera values as links to what's stored in the Unreal Reader node
        camera.knob('projection_mode').setExpression(unrealReaderNode.name() + '.projectionMode')
        camera.knob('focal').setExpression(unrealReaderNode.name() + '.focalLength')
        camera.knob('haperture').setExpression(unrealReaderNode.name() + '.aperture.x')
        camera.knob('vaperture').setExpression(unrealReaderNode.name() + '.aperture.y')
        camera.knob('translate').setExpression(unrealReaderNode.name() + '.camTranslate')
        camera.knob('rotate').setExpression(unrealReaderNode.name() + '.camRotate')
    else:
        camera.knob('projection_mode').fromScript(
            unrealReaderNode.knob('projectionMode').toScript(False))
        camera.knob('focal').fromScript(unrealReaderNode.knob('focalLength').toScript(False))
        camera.knob('translate').fromScript(unrealReaderNode.knob('camTranslate').toScript(False))
        camera.knob('rotate').fromScript(unrealReaderNode.knob('camRotate').toScript(False))

        numKeys = unrealReaderNode['aperture'].getNumKeys()
        camera.knob('haperture').setAnimated()
        camera.knob('vaperture').setAnimated()
        for i in range(numKeys):
            frame = unrealReaderNode.knob('aperture').getKeyTime(i)
            camera.knob('haperture').setValueAt(
                unrealReaderNode.knob('aperture').getValueAt(frame, 0), frame)
            camera.knob('vaperture').setValueAt(
                unrealReaderNode.knob('aperture').getValueAt(frame, 1), frame)


def createReadNode(unrealReaderNode):
    """Create a read node for the rendered output"""
    createRead = False
    createReadKnob = unrealReaderNode.knob('createReadNode')
    if createReadKnob:
        createRead = bool(createReadKnob.getValue())

    if createRead:
        # Create node and set file
        filename = unrealReaderNode['file'].getValue()
        read = nuke.nodes.Read(file='%s' % (filename))

        # Set frame range
        frameStart = unrealReaderNode['startFrame'].getValue()
        frameEnd = unrealReaderNode['endFrame'].getValue()
        read['first'].setValue(int(frameStart))
        read['last'].setValue(int(frameEnd))

        # Don't let Nuke add the extra exr/ prefix before all the
        # metadata to make it match with the port render metadata
        # out of the box.
        read['noprefix'].setValue(True)

        # Set position in node graph
        x = unrealReaderNode.xpos()
        y = unrealReaderNode.ypos()
        w = unrealReaderNode.screenWidth()
        m = int(x + w/2)
        read.setXYpos(m - int(read.screenWidth()/2), y + w)
