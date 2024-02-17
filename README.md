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

You can use the stub files inside the repository, but if you want to generate them, copy the `nukestubsgen.py` file inside the Nuke Script Editor and run it.

> When generating the stubs, it is preferable to use Nuke Studio, as doing it inside Nuke will cause the Hiero stubs to be incomplete.

Once done, you can find the stubs inside `~/.nuke/nuke-python-stubs/stubs`.

### 1.2.2. Use the stubs

Using the stubs will vary based on your text editor since most of them have their way of adding stubs to the environment.

Alternatively, you can use Visual Studio Code [NukeTools](https://marketplace.visualstudio.com/items?itemName=virgilsisoe.nuke-tools) and call the `Nuke Tools: Add Python Stubs` command.

## 1.3. Type guess

The script tries to guess the data type by parsing the function signature/documentation. This method is not 100% precise, and some types are unknown or wrong.

- The type `Any` means **it could be any we don't know** and not: **any type is valid**.
- The type  `int|float` means **it could be a float or an int we don't know** and not: **any number type is valid**.

> If arguments do not have any type annotation, it probably means that it was not possible to parse the function documentation.

The wrong types are likely due to the parser identifying valid keywords inside the documentation, which uses them to make a guess.

Example:

In the string: `-> switch to next view in settings Views list`, the parser will identify `list` as a match.

> You can also disable the guess filter by setting `StubsRuntimeSettings.guess` to `False`.

As a workaround, there is a post-fix mechanism which allows you to "manually" point to the wrong value and substitute it with a new one. You can look at the `NUKE_POST_FIXES` dictionary for more information.

## 1.4. Contributing

Although the script is a mess, you can still contribute by adding post-fixes information when you find wrong values.

If you would like to add some code, you need `pre-commit` installed in your repo.

For convenience, place the repo inside `~/.nuke` since the stubs are created inside `~/.nuke/nuke-python-stubs/stubs`. This way, `git` catches any change in the stubs files. Once you generate the stubs, run `pre-commit run -a` to apply the pre-commit hooks to each file to see the "real" difference of your new commits.

## 1.5. Acknowledgment

Pycharm Stub generator inspired the creation of this script.

## 1.6. Screenshot

[Nuke Tools](https://marketplace.visualstudio.com/items?itemName=virgilsisoe.nuke-tools) for Visual Studio Code will include the stubs files by default.

![Alt text](images/auto_complete.gif)
