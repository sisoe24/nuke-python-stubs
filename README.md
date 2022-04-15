# 1. Nuke python stubs file

A quick and dirty script to create Nuke Python file stubs to aid auto-complete in text editors.

- [1. Nuke python stubs file](#1-nuke-python-stubs-file)
  - [1.1. Description](#11-description)
  - [1.2. Usage](#12-usage)
  - [1.3. Type guess](#13-type-guess)
    - [1.3.1. Unguessed/Wrong types](#131-unguessedwrong-types)
    - [1.3.2. Workaround to wrong/unguessed types](#132-workaround-to-wrongunguessed-types)
  - [1.4. CLI Options](#14-cli-options)
  - [1.5. Acknowledgment](#15-acknowledgment)
  - [1.6. Screenshot](#16-screenshot)

## 1.1. Description

A stubs file generator for Nuke13/Python3. Files will include:

- Classes.
- Built-in methods.
- Constant.
- Arguments types.
- Return statements.

## 1.2. Usage

The stubs files are part of the package, but it is also possible to generate them:

```bash
alias nukepy='path/to/nuke13/interpreter'
nukepy nuke_stubs_generator.py -h
nukepy nuke_stubs_generator.py
nukepy nuke_stubs_generator.py -o path/to/dir
```

The script will also include the internal modules found inside the application folder. You can ignore them by supplying the `--exclude-internals` argument.

## 1.3. Type guess

The script tries to guess the data type of the function arguments and return statements, and, for the most part, it seems to be pretty accurate with very few exceptions:

- The type `Any` for arguments means: **it could be any we don't know** and not: **any type is valid**.
- The type  `Number` for arguments means: **it could be a float or an int we don't know** and not: **any number type is valid**.
- Optional arguments are signed as `x:type=None` for guessed types and `x=None` for the unguessed.
- Return statements are signed similarly to arguments:
  - `Any` means **it could be any**.
  - `Number` means **it could be a float or an int**.

> If arguments do not have type annotation, it probably means that it was not possible to parse the function documentation. Also, please note that some of the documentation is not accurate.

### 1.3.1. Unguessed/Wrong types

Because the code tries, for the most part, to stay away from writing single case conditions, some types/returns are wrong or unguessed.
The wrong types are likely due to the parser identifying valid keywords inside the documentation that belong to a descriptive string.

Example:

A function documentation return description: `-> switch to next view in settings Views list` will cause the parser to identify `list` as a match.

> The script generates an `unguessed_log.log` file with what wasn't able to guess.

### 1.3.2. Workaround to wrong/unguessed types

You can define special conditions to deal with the unguessed types inside the `manual_changes.json` file.
There is already a working file that you can use as an example.

## 1.4. CLI Options

```bash
usage: nuke_stubs_generator.py [-h] [-v] [--exclude-internals]
                               [--no-return-annotation] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbosity       Increase output verbosity
  --exclude-internals   Exclude internal modules: nukescripts, nuke_internal
  -x, --no-type-guess   Compile stubs without guessing some of the types.
  -o OUTPUT, --output OUTPUT
                        Output to a specific directory
```

## 1.5. Acknowledgment

Pycharm Stub generator inspired the creation of this script.

## 1.6. Screenshot

[Nuke Tools](https://marketplace.visualstudio.com/items?itemName=virgilsisoe.nuke-tools) for Visual Studio Code will include the stubs files by default.

![auto_complete_vscode](/images/auto_complete.gif)
