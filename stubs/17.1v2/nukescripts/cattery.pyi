# Type stubs for nuke 17.1v2. Generated; do not edit.

"""This module is in charge of discovery and populating the cattery toolbar.

Although it might seem a simple problem at first sight, there are wrinkles regarding model
compatibility to take into account.

When authoring a cat-file/ML-model within Nuke, we guarantee it to be forward compatible,
this is to say it will work on future versions of nuke.

It doesn't work the other way around though! There might be specific features that the
model depends on that are not present on older versions of Nuke, making it non-backward compatible.

This module provides a simple mechanism to discover models in the Cattery that are compatible
with the current version of nuke by describing the model on a `cat.json` file describing all the
metadata necessary.

i.e.

.. code-block::

    .
    └── Cattery
        ├── modelA
        │   ├── cat.json    # minimum_nuke_version_required = 13.1
        │   ├── modelA.cat
        │   └── modelA.gizmo
        ├── modelB
        │   ├── cat.json    # minimum_nuke_version_required = 14.0
        │   ├── modelB.cat
        │   └── modelB.gizmo
        └─── modelD
            ├── cat.json    # minimum_nuke_version_required = 15.0
            ├── modelC.cat
            └── modelC.gizmo

Here an example of what is the expected result of filtering the models at runtime on the many
versions of Nuke.

- Nuke `13.1` sees `modelA`
- Nuke `13.2` sees `modelA`
- Nuke `14` sees `modelA` and `modelB`
- Nuke `14.1` sees `modelA` and `modelB`
- Nuke `15` sees `modelA`, `modelB` and `modelC`
"""

from typing import Any
from typing import Generator
from typing_extensions import Self

ICONS: dict

class CatInfo:
    def __init__(self, filepath: Any, name: str = ..., icon: str = ...) -> None: ...
    @classmethod
    def from_dict(cls, data: Any) -> Self | None: ...
    def nuke_script(self) -> str: ...
    def to_dict(self) -> dict[str, Any]: ...

class PackageInfo:
    def __init__(self) -> None: ...
    @classmethod
    def from_dict(cls, data: Any) -> Self: ...
    @classmethod
    def from_json(cls, filepath: Any) -> Self: ...
    def to_dict(self) -> dict[str, Any]: ...
    def to_json(self, filepath: Any) -> None: ...

def create_menu() -> None: ...

def discover_packages(repository: Any, target_version: Any) -> list[Any]: ...

def find_repositories() -> Generator[Any, Any, None]: ...

def normalise_path_for_nuke(filepath: Any) -> Any:
    """Nuke uses forward slash on all platforms, including Windows (which is odd and
    unconventional), this method encapsulates that.
    """

def populate_menu(menu: Any) -> None: ...

def register_cats() -> None: ...
