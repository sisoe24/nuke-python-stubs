# Copyright (c) 2023 The Foundry Visionmongers Ltd.  All Rights Reserved.

from hiero.core import effectInputSourceCoods

# Override knob defaults


def _overrideTextEffectKnobDefaults(effectItemNode):
    effectItemNode['cliptype'].setValue(0)


OverrideEffectKnobDefaults = {'Text2': _overrideTextEffectKnobDefaults}


def overrideKnobDefaults(effectItem):
    """ Override timeline specific knob defaults for the given soft effect
    @param effectItem: the effect who's knob will be overriden
    """
    effectItemNode = effectItem.node()
    overrideKnobDefaultsFunc = OverrideEffectKnobDefaults.get(effectItemNode.Class(), None)
    if overrideKnobDefaultsFunc:
        overrideKnobDefaultsFunc(effectItemNode)

# After effect created


def _afterCornerPinEffectCreated(effectItem):
    (x, y, r, t) = effectInputSourceCoods(effectItem)
    effectItemNode = effectItem.node()
    effectItemNode['from1'].fromScript(str(x) + ' ' + str(y))
    effectItemNode['from2'].fromScript(str(r) + ' ' + str(y))
    effectItemNode['from3'].fromScript(str(r) + ' ' + str(t))
    effectItemNode['from4'].fromScript(str(x) + ' ' + str(t))
    effectItemNode['copy_from'].execute()


AfterEffectCreatedOperations = {'CornerPin2D': _afterCornerPinEffectCreated}


def afterEffectCreated(effectItem):
    """ Perform timeline specific operation for the given soft effect
    that has just been created.
    @param effectItem: the effect that has just been created
    """
    overrideKnobDefaults(effectItem)

    afterEffectCreatedFunc = AfterEffectCreatedOperations.get(effectItem.node().Class(), None)
    if afterEffectCreatedFunc:
        afterEffectCreatedFunc(effectItem)
