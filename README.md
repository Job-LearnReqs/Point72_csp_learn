# Point72 CSP Learn

This repo is set up to give you an isolated Ubuntu dev environment for learning `csp`.

## Open In A Dev Container

1. Install Docker Desktop or another Docker engine.
2. Open this folder in VS Code.
3. In your host shell, export your OpenAI key before starting the container:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

4. If this is your first time opening the repo, run `Dev Containers: Reopen in Container`. If the container already exists, run `Dev Containers: Rebuild Container`.
5. Wait for `.devcontainer/postCreate.sh` to finish creating `.venv` and installing dependencies.

The dev container forwards `OPENAI_API_KEY` from your host environment into the container, so terminals opened inside the container can use it. After the container starts, verify with:

```bash
python -c "import os; print('OPENAI_API_KEY is set' if os.getenv('OPENAI_API_KEY') else 'OPENAI_API_KEY is missing')"
```

If you exported the key after the container was already running, use `Dev Containers: Rebuild Container` so the updated host environment is picked up.

The image also installs the OpenAI Codex CLI during the container build, so `codex` is available in the container terminal right away. After the rebuild, verify with:

```bash
codex --version
```

You can then start Codex with either:

```bash
codex
codex --login
```

## What The Container Includes

- Ubuntu 24.04
- Python 3
- Node.js 22
- A workspace-local virtual environment at `.venv`
- Build tools that match the Linux dependency list from the upstream `csp` repo
- `csp` and `ipykernel` preinstalled in the virtual environment
- OpenAI Codex CLI installed globally as `codex`
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
codex --version
python -m pip list | rg '^csp|^pyarrow|^pandas'
```

## Next Learning Steps

- Start with [samples/sum_constants.py](samples/sum_constants.py)
- Then run [samples/spread.py](samples/spread.py)
- After that, browse the official `Point72/csp` example catalog for more advanced graphs and adapters
