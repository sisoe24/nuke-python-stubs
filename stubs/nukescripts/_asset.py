import urllib
from typing import Iterable
from pathlib import Path

import nuke
import _asset
import openassetio
from openassetio.access import ResolveAccess
from openassetio_mediacreation.traits.content import LocatableContentTrait


def deassetize(nodes: Iterable[nuke.Node]) -> tuple[bool, list[nuke.Knob]]:
    """
    Finds all assetized File_Knob's in nodes and replaces their entity reference
    by their respective resolved file path.

    :param nodes:      A list of nodes to be deassetized

    :return: A tuple. The first element is a boolean that is True if all assetized
             knobs were successfully deassetized and the second is a list of
             unresolved knobs that are assetized but failed to be resolved.

             If OpenAssetIO isn't correctly configured, (False, []) is returned.
    """

    failed_knobs = []

    manager = _asset.getManager()
    if not manager:
        nuke.tprint("Failed to retrieve Nuke's manager")
        return False, []

    context = _asset.getContext()
    if not context:
        nuke.tprint("Failed to retrieve Nuke's context")
        return False, []

    knobs_to_update = []
    entity_refs = []

    for node in nodes:
        for knob in node.allKnobs():
            if not isinstance(knob, nuke.File_Knob):
                continue
            if entity_ref := manager.createEntityReferenceIfValid(knob.value()):
                knobs_to_update.append(knob)
                entity_refs.append(entity_ref)

    # If there's no assetized knob to resolve, stop here
    if not entity_refs:
        return not failed_knobs, failed_knobs

    try:
        resolved_refs = manager.resolve(
            entity_refs,
            {LocatableContentTrait.kId},
            ResolveAccess.kRead,
            context,
            manager.BatchElementErrorPolicyTag.kVariant
        )
    except Exception as e:
        nuke.tprint(str(e))
        return not failed_knobs, failed_knobs

    for knob, resolved_ref in zip(knobs_to_update, resolved_refs):
        if isinstance(resolved_ref, openassetio.BatchElementError):
            nuke.tprint(f'{resolved_ref.message}, ignoring...')
            failed_knobs.append(knob)
            continue

        locatable_content = LocatableContentTrait(resolved_ref)

        if not locatable_content.isImbued() or not (url := locatable_content.getLocation(defaultValue='')):
            nuke.tprint(f'Bad LocatableContentTrait for {knob.value()}, ignoring...')
            failed_knobs.append(knob)
            continue

        url_path = urllib.parse.urlparse(url).path
        knob.setValue(
            Path(urllib.request.url2pathname(url_path)).as_posix()
        )

    return not failed_knobs, failed_knobs
