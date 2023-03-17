# Insert the Hiero Python modules into Shiboken's signature support code.
# Without this there will be errors when trying to run help() or  generate the
# docs.
#
# There are two parts to this:
#
# The shibokensupport.signature.mapping.Reloader.module_valid method filters
# for binary modules, but it misses the Hiero ones because they are compiled
# into the application libraries. Overriding it to return true for these
#
# C++ 'primitive' types seem to need to be manually inserted into the mapping
# type_map dict. This is done by defining an 'init_{modname}' function in the
# mapping module which will then be called back to when Reloader().update() is
# called.

import typing

import shibokensupport.signature.mapping as mapping

_module_valid_orig = mapping.Reloader.module_valid
_hiero_module_names = ('core', 'ui')


def _module_valid_override(_, mod):
    return _module_valid_orig(mod) or mod.__name__ in _hiero_module_names


mapping.Reloader.module_valid = _module_valid_override


def _init_core():
    mapping.type_map.update({
        'Hiero.Python.Time': int,
        'Hiero.Python.DTime': float,
        'Hiero.Python.String': str,
        'std.string': str,
        'std.set': typing.Set
    })
    return locals()


mapping.init_core = _init_core


mapping.Reloader().update()
