# Nuke python stubs file

Create Nuke python file stubs to aid auto complete in text editors.

## Description

This method is inspired by PyCharm stub generator. Although less sophisticated, is tries to be more accurate on certain data types like returns and arguments types.

The stubs will include:
* Classes
* Built-in methods
* Constants
* Arguments types
* Return statements

The scripts works only under Python 3 but I've included the stubs inside the git repo if one does not have access to Nuke13.

## Usage

```bash
alias nukepy='path/to/nuke13/interpreter'
nukepy nuke_stubs_generator.py -h
nukepy nuke_stubs_generator.py
nukepy nuke_stubs_generator.py -o path/to/dir
```

The script will also include the internal modules found inside the application folder. You can ignore them by supplying the `--exclude-internals` argument.

## Type guess

The script tries to guess the data type of the function arguments and return statements and for the most part it seems to be pretty accurate with a very few exceptions. 

When the keyword `Any` is used, it means more: **it could be any we don't know** and not: **any type is valid**.

When the keyword `Number` is used, it means more: **it could be a float or an int** and not: **any number type is valid**.

### Arguments

If arguments have no type annotation it probably means that wasn't possible to parse the documentation. Also please note that some of the documentations are not accurate.

Optional arguments are denoted by: `x:type = None`. If the type was not guessed: `x=None`.

### Return statements

Return statements are denoted similar to arguments. If it wasn't possible the guess the return statement after parsing the documentation will return `Any` as "it could be any".

### Left-over types

The script tries, for the most part, to stay away from writing single case conditions so some of the types/returns are still wrong or unguessed. The script generated a unguessed_log.log file with what wasn't able to correctly guess.

If later, one would like to adjust those statements by hand manually, it could save them into the file _manual\_changes.json_. This will ensure that after each compile, the stubs modifications are kept intact. The file has already an example on how to add information. This would also encourage the reuse of this project repo instead of generating new ones.

## Options

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

## Screenshot

Visual Studio Code after adding the stubs to path.

![auto_complete_vscode](/images/auto_complete.gif)
