# 1. Nuke python stubs file

A quick and dirty script to create Nuke Python file stubs to support auto-complete in text editors.

- [1. Nuke python stubs file](#1-nuke-python-stubs-file)
  - [1.1. Description](#11-description)
  - [1.2. Usage](#12-usage)
    - [1.2.1. Generate the stubs](#121-generate-the-stubs)
    - [1.2.2. Use the stubs](#122-use-the-stubs)
  - [1.3. Type guess](#13-type-guess)
  - [1.4. Contributing](#14-contributing)
  - [1.5. Acknowledgment](#15-acknowledgment)
  - [1.6 TODO](#16-todo)
  - [1.6. Screenshot](#16-screenshot)

## 1.1. Description

A stub file generator for Nuke & Hiero Python 3. Besides including the public API, the script will generate stubs for:

- Classes.
- Built-in methods.
- Constant.
- Arguments types.
- Return statements.

## 1.2. Usage

### 1.2.1. Generate the stubs

You can use the stub files inside the [repository](https://github.com/sisoe24/nuke-python-stubs/releases), but if you want to generate them, copy the `nukestubsgen.py` file inside the Nuke Script Editor and run it.

> When generating the stubs, it is preferable to use Nuke Studio, as doing it inside Nuke will cause the Hiero stubs to be incomplete.

Once done, you can find the stubs inside `~/.nuke/nuke-python-stubs/stubs`.

### 1.2.2. Use the stubs

Using the stubs will vary based on your text editor since most of them have their way of adding stubs to the environment.

Alternatively, you can use Visual Studio Code [NukeTools](https://marketplace.visualstudio.com/items?itemName=virgilsisoe.nuke-tools) and call the `Nuke Tools: Add Python Stubs` command.

## 1.3. Type guess

The script tries to guess the data type by parsing the function signature/documentation. This method is not 100% precise, and some types are unknown or wrong.

- The type `Any` means it could be any we don't know and not any type is valid.
- The type  `int|float` means it could be a float or an int we don't know and not any number type is valid.
- No types means that is not possible to guess the type.

The wrong types are likely due to the parser identifying valid keywords inside the documentation, which uses them to make a guess.

Example:

In the return value from the docs: `-> switch to next view in settings Views list`, the parser will guess the type as `list` since it found the word `list` in the documentation and not because it knows the type.

> You can also disable the guess filter by setting `StubsRuntimeSettings.guess` to `False`.

As a workaround, there is a post-fix mechanism which allows you to "manually" point to the wrong value and substitute it with a new one. You can look at the `NUKE_POST_FIXES` dictionary for more information.

## 1.4. Contributing

In order to make the stubs as accurate as possible, feel free to open a new issue if you find any wrong values or missing information. Also, you can contribute by adding post-fixes information to the `*_POST_FIXES` dictionary.

TODO: Add a section on how to contribute to the project.

## 1.5. Acknowledgment

Pycharm Stub generator inspired the creation of this script.

## 1.6 TODO

- [ ] Make pre-commit on a pull request.
- [ ] Make it available via pip.
- [ ] Find duplicates

## 1.6. Screenshot

[Nuke Tools](https://marketplace.visualstudio.com/items?itemName=virgilsisoe.nuke-tools) for Visual Studio Code will include the stubs files by default.

![Alt text](images/auto_complete.gif)
