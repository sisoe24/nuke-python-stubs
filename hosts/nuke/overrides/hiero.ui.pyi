# Corrections for hiero.ui. Format: src/hoststubs/overrides.py.
#
# Ported from HIERO_UI_POST_FIX in the old nukestubsgen.py, then checked
# against a Nuke Studio 15.2v9 session.

# verified: None when no sequence is active.
# src: manual
def activeSequence() -> hiero.core.Sequence | None: ...

# verified: None when no editor is found.
# src: manual
def getTimelineEditor(
    sequence: hiero.core.Sequence, creationFlag: TimelineEditorCreationFlag = ...,
) -> TimelineEditor | None: ...
