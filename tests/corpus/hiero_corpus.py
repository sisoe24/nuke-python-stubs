"""Hiero usage that the stubs must type. Checked by `python -m hoststubs build`."""
from typing_extensions import reveal_type

import hiero.ui
import hiero.core

# Seeds.
reveal_type(hiero.core.projects())
project = hiero.core.projects()[0]
reveal_type(project.sequences())
sequence = project.sequences()[0]

# Every override in hosts/nuke/overrides/hiero.core.pyi and hiero.ui.pyi.
reveal_type(hiero.core.project)
reveal_type(hiero.core.projects)
reveal_type(hiero.core.Project.clips)
reveal_type(hiero.core.Project.bins)
reveal_type(hiero.core.Project.tracks)
reveal_type(hiero.core.Project.videoTracks)
reveal_type(hiero.core.Project.audioTracks)
reveal_type(hiero.core.Project.trackItems)
reveal_type(hiero.core.Project.videoTrackItems)
reveal_type(hiero.core.Project.audioTrackItems)
reveal_type(hiero.core.Project.extractSettings)
reveal_type(hiero.core.Project.setOutputFormat)
reveal_type(sequence.videoTracks())
reveal_type(sequence.items())
reveal_type(hiero.core.Sequence.addClip)
reveal_type(hiero.core.VideoTrack.items)
reveal_type(hiero.core.VideoTrack.addTrackItem)
reveal_type(hiero.core.Clip.addToNukeScript)
reveal_type(hiero.core.EffectTrackItem.addToNukeScript)
reveal_type(hiero.core.EffectTrackItem.isRetimeEffect)
reveal_type(hiero.core.EffectTrackItem.setName)
reveal_type(hiero.core.TrackItem.source)
reveal_type(hiero.core.TrackItem.thumbnail)
reveal_type(hiero.core.Bin.importSequence)
reveal_type(hiero.ui.activeSequence())
reveal_type(hiero.ui.getTimelineEditor)

# Old post-fixes the pipeline now derives.
reveal_type(hiero.core.conformer())
reveal_type(hiero.core.Clip.readNode)
reveal_type(hiero.core.EffectTrackItem.name)
reveal_type(sequence.project())

# `@return: nuke.Node` in a hiero docstring is Nuke's Node.
reveal_type(hiero.core.Transition.dissolveNode)

# A default that is an instance of a host class types the parameter.
reveal_type(hiero.core.TrackItem.addToNukeScript)

# Return probe in a Nuke Studio session.
reveal_type(hiero.core.Bin.parentBin)
reveal_type(hiero.core.BinItem.activeItem)
reveal_type(hiero.core.Bin.name)
reveal_type(hiero.core.AudioTrack.channel)

# Classes owned by hiero.ui, not by the first module that re-exports them.
reveal_type(hiero.ui.Viewer)
reveal_type(hiero.ui.currentViewer())

# Wrong on purpose. Each line must be reported.
project.sequences(42)
sequence.nope()
hiero.core.project()
