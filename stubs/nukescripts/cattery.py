"""
This module is in charge of discovery and populating the cattery toolbar.

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

```
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
```

Here an example of what is the expected result of filtering the models at runtime on the many
versions of Nuke.

- Nuke `13.1` sees `modelA`
- Nuke `13.2` sees `modelA`
- Nuke `14` sees `modelA` and `modelB`
- Nuke `14.1` sees `modelA` and `modelB`
- Nuke `15` sees `modelA`, `modelB` and `modelC`
"""


import os
import json

import nuke_internal as nuke


class CatInfo:
    def __init__(self, filepath, name='', icon=''):
        self.filepath = filepath
        self.name = name or filepath
        self.icon = icon

    @classmethod
    def from_dict(cls, data):
        if not data.get('filepath'):
            return None
        self = cls(data['filepath'], data.get('name', ''), data.get('icon', ''))
        return self

    def to_dict(self):
        return {
            'filepath': self.filepath,
            'name': self.name,
            'icon': self.icon
        }

    def nuke_script(self):
        if self.filepath.endswith('.gizmo'):
            _, filename = os.path.split(self.filepath)
            return f"import nuke; nuke.createNode({filename!r})"

        elif self.filepath.endswith('.cat'):
            # we are creating a temp nk file so we can setup the knob on inference pointing to the
            # cat file, even when the node is read only due to the license being used.
            template = """import os
import tempfile
import nuke
_, nk = tempfile.mkstemp("cattery", {name!r})
with open(nk, "w") as fp:
    fp.write("Inference {{\\n modelFile {filepath}\\n name {name}\\n }}")
nuke.nodePaste(nk)
os.remove(nk)
del nk"""
            return template.format(name=self.name.replace(' ', '_'), filepath=self.filepath)
        return ''


class PackageInfo:
    def __init__(self):
        self.minimum_nuke_version_required = 13.1
        self.version = 1
        self.category = ''
        self.description = ''
        self.cats = []  # a package can involve many cats, i.e. large and small arch

    @classmethod
    def from_dict(cls, data):
        self = cls()
        self.minimum_nuke_version_required = data.get('minimum_nuke_version_required', 13.1)
        self.version = data.get('version', 1)
        self.category = data.get('category', '')
        self.description = data.get('description', '')
        cats = [CatInfo.from_dict(d) for d in data.get('cats', [])]
        self.cats = [x for x in cats if x is not None]  # filter invalid cats
        return self

    def to_dict(self):
        return {
            'minimum_nuke_version_required': self.minimum_nuke_version_required,
            'version': self.version,
            'category': self.category,
            'description': self.description,
            'cats': [cat.to_dict() for cat in self.cats],
        }

    @classmethod
    def from_json(cls, filepath):
        with open(filepath) as fp:
            data = json.load(fp)
        return cls.from_dict(data)

    def to_json(self, filepath):
        with open(filepath, 'w') as fp:
            json.dump(self.to_dict(), fp, indent=4)


ICONS = {
    'menu': 'CatteryMenu.png',
    'depth estimation': 'CatteryDepth.png',
    'optical flow': 'CatteryOpticalFlow.png',
    'upscaling': 'CatteryUpScaling.png',
    'denoising': 'CatteryDeNoising.png',
    'segmentation': 'CatterySegmentation.png',
    'stylisation': 'CatteryStylisation.png',
    'other': 'CatteryOther.png',
    'default': 'CatteryDefault.png',
}
# aliases
ICONS['stylization'] = ICONS['stylisation']
ICONS['restoration'] = ICONS['denoising']
ICONS['motion estimation'] = ICONS['optical flow']
ICONS['super resolution'] = ICONS['upscaling']


def normalise_path_for_nuke(filepath):
    """
    Nuke uses forward slash on all platforms, including Windows (which is odd and
    unconventional), this method encapsulates that.
    """
    return filepath.replace('\\', '/')


def find_repositories():
    for path in (pp for pp in nuke.pluginPath() if os.path.exists(pp)):
        for filename in (name for name in os.listdir(path) if 'cattery' == name.lower()):
            yield os.path.abspath(os.path.join(path, filename))


def discover_packages(repository, target_version):
    result = list()
    for root, dirs, files in os.walk(repository):
        if 'cat.json' not in files:
            continue
        filepath = os.path.join(root, 'cat.json')
        package = PackageInfo.from_json(filepath)
        if package.minimum_nuke_version_required <= target_version and len(package.cats) > 0:
            for cat in package.cats:
                cat.filepath = normalise_path_for_nuke(os.path.join(root, cat.filepath))
                icon_filepath = normalise_path_for_nuke(os.path.join(root, cat.icon))
                cat.icon = icon_filepath if cat.icon else ICONS['default']
            result.append(package)
    return result


def register_cats():
    nuke_version = float(f"{nuke.NUKE_VERSION_MAJOR}.{nuke.NUKE_VERSION_MINOR}")
    for repository in find_repositories():
        for package in discover_packages(repository, nuke_version):
            for cat in package.cats:
                if not cat.filepath.endswith('.gizmo'):
                    continue
                directory, _ = os.path.split(cat.filepath)
                if directory not in nuke.pluginPath():
                    nuke.pluginAddPath(directory, addToSysPath=False)


def populate_menu(menu):
    register_cats()
    nuke_version = float(f"{nuke.NUKE_VERSION_MAJOR}.{nuke.NUKE_VERSION_MINOR}")

    packages_by_category = dict()
    for repository in find_repositories():
        for package in discover_packages(repository, nuke_version):
            category = package.category if package.category else '_'
            if category not in packages_by_category:
                packages_by_category[category] = list()
            packages_by_category[category].append(package)

    for category in sorted(packages_by_category.keys()):
        submenu = menu
        if category != '_':
            icon = ICONS.get(category.lower(), ICONS['other'])
            submenu = menu.menu(category) if menu.menu(category) else menu.addMenu(category, icon)

        cats = [c for p in packages_by_category[category] for c in p.cats]
        cats.sort(key=lambda k: k.name)
        for cat in cats:
            command_name = cat.name
            submenu.addCommand(command_name, cat.nuke_script(), icon=cat.icon)


def create_menu():
    name = 'Cattery'
    toolbar = nuke.menu('Nodes')
    m = toolbar.menu(name)
    if not m:
        m = toolbar.addMenu(name, ICONS['menu'])
    m.clearMenu()

    url = 'https://cattery.foundry.com'
    m.addCommand('Go to Cattery', f"import webbrowser; webbrowser.open(\"{url}\")")
    m.addSeparator()

    populate_menu(m)

    m.addSeparator()
    m.addCommand('Update', 'from nukescripts import cattery; cattery.create_menu()')


# register/discover cattery models on first import
register_cats()
