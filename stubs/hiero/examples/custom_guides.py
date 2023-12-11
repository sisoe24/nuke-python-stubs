# Example shows how you can add custom viewer guides and masks via Python
# If you wish for this code to be run on startup, copy it to your ~/.nuke directory.
# Note: Hiero and Nuke use the same viewer guides and masks list.

import guides

# SimpleGuide( name, r, g, b, amount, coords = kGuideSequence, aspect = 0.0, crosshairs = True)
titleSafeGuide = guides.SimpleGuide(
    'Custom Title Safe', 0.0, 1.0, 0.1, 1, guides.kGuideMasked)
actionSafeGuide = guides.SimpleGuide(
    'Custom Action Safe', 1, 1, 1, 1, guides.kGuideMasked, crosshairs=True)
sequenceFormatGuide = guides.SimpleGuide(
    'Custom Sequence Format', 1, 1, 0, 1, guides.kGuideSequence, crosshairs=False)
viewer_guides = [titleSafeGuide, actionSafeGuide, sequenceFormatGuide]


# MaskGuide( name, aspect)
viewer_masks = [
    guides.MaskGuide('NTSC', 0.91),
    guides.MaskGuide('PAL', 1.09),
    guides.MaskGuide('NTSC_16:9', 1.21),
    guides.MaskGuide('PAL_16:9', 1.46),
    guides.MaskGuide('Cinemascope 2:1', 2.0)
]
