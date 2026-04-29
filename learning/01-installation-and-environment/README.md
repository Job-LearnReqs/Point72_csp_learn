# 01 Installation And Environment

## Read

- <https://github.com/Point72/csp/wiki/Installation>
- <https://github.com/Point72/csp/wiki/Build-CSP-from-Source>
- <https://github.com/Point72/csp/wiki/Local-Development-Setup>
- [`../../README.md`](../../README.md)
- [`../../.devcontainer/requirements.txt`](../../.devcontainer/requirements.txt)

## Concepts

- Installed package versus source build.
- Python wheel compatibility.
- Local virtual environment and dev container behavior.
- Runtime dependencies such as pandas and pyarrow.

## Practice Setup

Create `environment_check.py` that prints:

- Python version
- CSP version
- whether pandas imports
- whether pyarrow imports

Run:

```bash
python learning/01-installation-and-environment/environment_check.py
```

## Checkpoint

You can describe the difference between learning CSP from the installed package
and contributing to CSP from source.
