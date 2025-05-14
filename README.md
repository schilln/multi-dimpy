# Overview
Everyone knows you can't add apples and oranges.<br>
Most people also know you can't add meters and seconds.<br>
But sometimes people do—accidentally, when it's hidden in code or in matrix computations.

Models and algorithms with dimensional inconsistencies might still yield decent results, but they don't make physical sense, and a change of units results in a change to the output, when units shouldn't make a difference.

Software packages for managing dimensions already exist, but they lack the ability to do **dimensioned linear algebra**—they mostly just work with scalar values.
So as a first go and a proof-of-concept, this package wraps NumPy and tracks physical dimensions of $n$-dimensional arrays using theory developed in the book *Multidimensional Analysis* (see citation below).

(Hart, G. W. (1995). Multidimensional Analysis: Algebras and Systems for Science and Engineering. Springer-Verlag.)

# Contributing

In case it isn't clear, this package is in its very early stages.
- To get started contributing, see the sections below.
- To get acquainted with with dimensioned linear algebra, take a look at *Multidimensional Analysis* (cited in the [Overview](#overview)).
Hopefully soon we'll have a document or two describing the theory in brief. (Perhaps you could write one!)
- Feel free to join the [Discussion](https://github.com/schilln/multi-dimpy/discussions)! (If there is any...)

## Development environment setup

1. Create a fork of the repository.
1. Set up dependencies using Poetry.
    1. Follow the Poetry's installation instructions [here](https://python-poetry.org/docs/).
    1. Make sure Poetry's executable is added to your `$PATH`.<br>
        (Poetry should describe how to do this in the terminal output following successful installation.
        Running `poetry --version` should verify it's been installed and added to your `$PATH` correctly.)
    1. Install multi-DimPy's dependencies and development dependencies using `poetry install`.
1. Install pre-commit hooks using `poetry run pre-commit install`.<br>
    (You may need to restart your editor for pre-commit hooks to get the correct `$PATH` with Poetry's executable.)

Now your environment should be ready to go!

To run tools like `ruff ...` or `pytest ...`, you'll instead use `poetry run ruff ...` and `poetry run pytest ...`, etc.

## Making contributions

To start making commits, create a branch from your fork's `main` branch.<br>
To get your changes onto the `main` branch of multi-DimPy:

1. Pull the latest development on `multi-dimpy/main` to your `main` branch.
1. Merge any changes in `main` into your branch.
1. Make sure all tests pass (using `poetry run pytest`).
1. Push your branch to your fork.
1. Make a pull request from your branch into `multi-dimpy/main`, and make sure all checks pass so that the changes can be approved and merged into `main`.

## Other notes

### Spell checking
The directory `.cspell` is for managing custom dictionaries used by the VS Code extension [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker).
It's not required for development, but it (probably) won't hurt.
To use the extension with these dictionaries, assuming you've opened the root directory of your fork's clone as a [VS Code Workspace](https://code.visualstudio.com/docs/editing/workspaces/workspaces), you can add the following to `.vscode/settings.json`:

```
{
    ...
    "cSpell.customDictionaries": {
        "Python": {
            "path": "${workspaceFolder}/.cspell/python-dictionary.txt",
            "addWords": true,
            "scope": "workspace"
        },
        "DimPy": {
            "path": "${workspaceFolder}/.cspell/dimpy-dictionary.txt",
            "addWords": true,
            "scope": "workspace"
        },
    },
    ...
}
```
