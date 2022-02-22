# 1. Nuke python stubs file

A quick and dirty script to create Nuke Python file stubs to aid auto complete in text editors.

- [1. Nuke python stubs file](#1-nuke-python-stubs-file)
  - [1.1. Description](#11-description)
  - [1.2. Usage](#12-usage)
  - [1.3. Type guess](#13-type-guess)
    - [1.3.1. Unguessed/Wrong types](#131-unguessedwrong-types)
    - [1.3.2. Workaround to wrong/unguessed types](#132-workaround-to-wrongunguessed-types)
  - [1.4. CLI Options](#14-cli-options)
  - [1.5. Acknowledgement](#15-acknowledgement)
  - [1.6. Screenshot](#16-screenshot)

## 1.1. Description

A stubs file generator for Nuke13/Python3. Files will include:

- Classes.
- Built-in methods.
- Constant.
- Arguments types.
- Return statements.

## 1.2. Usage

Stubs file are included with the package, but it also possible to generated them:

```bash
alias nukepy='path/to/nuke13/interpreter'
nukepy nuke_stubs_generator.py -h
nukepy nuke_stubs_generator.py
nukepy nuke_stubs_generator.py -o path/to/dir
```

The script will also include the internal modules found inside the application folder. They can ignored by supplying the `--exclude-internals` argument.

## 1.3. Type guess

The script tries to guess the data type of the function arguments and return statements and for the most part it seems to be pretty accurate with very few exceptions:

- When the keyword `Any` is used for arguments, it means: **it could be any we don't know** and not: **any type is valid**.
- When the keyword `Number` is used, it means: **it could be a float or an int** and not: **any number type is valid**.
- Optional arguments are denoted by: `x:type=None`. If the type was not guessed: `x=None`.
- Return statements are denoted similar to arguments. If the parses wasn't able to guess the return, will return `Any` as **it could be any**.

> If arguments has no type annotation, it probably means that wasn't possible to parse the documentation. Also please note that some of the documentations is not accurate.

### 1.3.1. Unguessed/Wrong types

The script tries, for the most part, to stay away from writing single case conditions, so some types/returns are wrong or unguessed.
The wrong types are likely due the parser identifying some keywords in the documentation and making a guess based on that.

Example:

If documentation returns: `-> switch to next view in settings Views list`, the parser will search for potential keywords and is going to assume that `list` is a match.

> The script generated a `unguessed_log.log` file with what wasn't able to correctly guess.

### 1.3.2. Workaround to wrong/unguessed types

The `manual_changes.json` file, allows to create some manual modifications that are going to be applied when the stubs are generated. A file example is provided.

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
                        Output to specific directory
```

## 1.5. Acknowledgement

This method is inspired by PyCharm stub generator.

## 1.6. Screenshot

[Nuke Tools](https://marketplace.visualstudio.com/items?itemName=virgilsisoe.nuke-tools) for Visual Studio Code, will include the files by default.

![auto_complete_vscode](/images/auto_complete.gif)
