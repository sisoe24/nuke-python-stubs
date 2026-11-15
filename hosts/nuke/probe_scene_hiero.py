"""The hiero scene the probe runs against. Runs inside a Nuke Studio GUI session.

One project with a sequence, a video and an audio track, a bin, a tag, and
one clip from a generated image, placed on the video track.
"""
import os
import sys
import tempfile

import hiero.ui
import hiero.core

try:
    from PySide6 import QtGui
except ImportError:
    from PySide2 import QtGui

# probe.py stores this in probe.json. build() appends what it created.
DESCRIPTION = []

_projects = []


def _attempt(label, create):
    """Create one scene object. A failure is noted, not fatal."""
    # Written first, so the log names the step if it takes the host down.
    sys.stderr.write('scene: {}\n'.format(label))
    sys.stderr.flush()

    try:
        created = create()
    except Exception as error:
        DESCRIPTION.append('{}: not created ({}: {})'.format(label, type(error).__name__, error))
        return []

    DESCRIPTION.append(label)
    if created is None:
        return []
    return list(created) if isinstance(created, (list, tuple)) else [created]


def _image_file():
    image = QtGui.QImage(64, 64, QtGui.QImage.Format_RGB32)
    image.fill(0)
    path = os.path.join(tempfile.mkdtemp(prefix='hoststubs_probe_'), 'probe.png')
    image.save(path)
    return path


def build():
    project = hiero.core.newProject()
    _projects.append(project)
    DESCRIPTION.append('new project')

    sequence = hiero.core.Sequence('probe_sequence')
    video = hiero.core.VideoTrack('video')
    audio = hiero.core.AudioTrack('audio')
    sequence.addTrack(video)
    sequence.addTrack(audio)
    sequence_item = hiero.core.BinItem(sequence)
    project.clipsBin().addItem(sequence_item)
    DESCRIPTION.append('sequence with one video and one audio track')

    objects = [project, sequence, video, audio, sequence_item, project.clipsBin()]

    source = _attempt(
        'media source from a generated image', lambda: hiero.core.MediaSource(_image_file()),
    )
    clip = _attempt('clip', lambda: hiero.core.Clip(source[0]))
    objects += source + clip
    if clip:
        clip_item = _attempt('clip in bin', lambda: hiero.core.BinItem(clip[0]))
        if clip_item:
            _attempt('add clip to bin', lambda: project.clipsBin().addItem(clip_item[0]))
        objects += clip_item
        objects += _attempt('track item on the video track', lambda: video.addTrackItem(clip[0], 0))
        objects += _attempt('clip versions', lambda: clip_item[0].items() if clip_item else [])

    objects += _attempt('bin', lambda: hiero.core.Bin('probe_bin'))
    objects += _attempt('tag', lambda: hiero.core.Tag('probe_tag'))
    objects += _attempt('format', lambda: hiero.core.Format(1920, 1080, 1.0, 'probe_format'))
    objects += _attempt('time base', lambda: hiero.core.TimeBase(24))
    objects += _attempt('application settings', lambda: hiero.core.ApplicationSettings())
    objects += _attempt('sequence format', sequence.format)
    objects += _attempt('main window', hiero.ui.mainWindow)
    objects += _attempt('window manager', hiero.ui.windowManager)
    objects += _attempt('current viewer', hiero.ui.currentViewer)
    objects += _attempt('active view', hiero.ui.activeView)

    return objects


def candidates():
    """Values the parameter probe offers to each argument position, most common first."""
    project = _projects[0]
    sequence = project.sequences()[0]
    values = [
        'hoststubs_probe', 1, 0.5, True, None, [], (), {},
        project, sequence, sequence.videoTracks()[0], project.clipsBin(),
        hiero.core.TimeBase(24), sequence.format(), _callback,
    ]
    clips = project.clips()
    if clips:
        values.append(clips[0])
        values += list(sequence.videoTracks()[0].items())[:1]
    return values


def _callback(*args, **kwargs):
    return None


def teardown():
    for project in _projects:
        project.close()
