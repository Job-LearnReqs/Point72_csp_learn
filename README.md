# Point72 CSP Learn

This repo is set up to give you an isolated Ubuntu dev environment for learning `csp`.

## Open In A Dev Container

1. Install Docker Desktop or another Docker engine.
2. Open this folder in VS Code.
3. Run `Dev Containers: Reopen in Container`.
4. Wait for `.devcontainer/postCreate.sh` to finish creating `.venv` and installing dependencies.

## What The Container Includes

- Ubuntu 24.04
- Python 3
- A workspace-local virtual environment at `.venv`
- Build tools that match the Linux dependency list from the upstream `csp` repo
- `csp` and `ipykernel` preinstalled in the virtual environment
- `linux/amd64` container settings so Apple Silicon hosts use the published Linux x86_64 `csp` wheels instead of attempting an `arm64` source build

## Run The Local Samples

Once the container is ready, run:

```bash
python samples/sum_constants.py
python samples/spread.py
```

## Useful Commands

```bash
python -c "import csp; print(csp.__version__)"
python -m pip list | rg '^csp|^pyarrow|^pandas'
```

## Next Learning Steps

- Start with [samples/sum_constants.py](samples/sum_constants.py)
- Then run [samples/spread.py](samples/spread.py)
- After that, browse the official `Point72/csp` example catalog for more advanced graphs and adapters
