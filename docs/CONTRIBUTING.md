# Contributing

This document provides instructions for contributing actual code to this project.\
For a crash course in dimensioned linear algebra, see [`Theory`](theory/README.md).

## Development environment setup

1. Create a fork of the repository.
1. Set up dependencies using Poetry.
    1. Follow Poetry's [installation instructions](https://python-poetry.org/docs/).
    1. Make sure Poetry's executable is added to your `$PATH`.\
        (Poetry should describe how to do this in the terminal output following successful installation.
        Running `poetry --version` should verify it's been installed and added to your `$PATH` correctly.)
    1. Install multi-DimPy's dependencies and development dependencies using `poetry install`.
1. Install pre-commit hooks using `poetry run pre-commit install`.\
    (You may need to restart your editor for pre-commit hooks to get the correct `$PATH` with Poetry's executable.)

Now your environment should be ready to go!

To run tools like `ruff ...` or `pytest ...`, you'll instead use `poetry run ruff ...` and `poetry run pytest ...`, etc.

## Making contributions

To start making commits, create a branch from your fork's `main` branch.\
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

```json
{
    // ...
    "cSpell.customDictionaries": {
        "DimPy": {
            "path": "${workspaceFolder}/.cspell/dimpy-dictionary.txt",
            "addWords": true,
            "scope": "workspace"
        },
        "LaTeX": {
            "path": "${workspaceFolder}/.cspell/latex-dictionary.txt",
            "addWords": true,
            "scope": "workspace"
        },
        "Python": {
            "path": "${workspaceFolder}/.cspell/python-dictionary.txt",
            "addWords": true,
            "scope": "workspace"
        },
    },
    // ...
}
```
