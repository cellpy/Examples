# cellpy Examples

Notebooks and scripts that show how to load, plot, and analyse battery
cycling data with [cellpy](https://cellpy.readthedocs.io). Aimed at people
who already have some Python, but you do not need to develop cellpy itself
to use this repo.

## Quick start

You need a working [conda](https://docs.conda.io/) install (Miniconda,
Anaconda, or Mambaforge) and Python 3.13+.

From the root of this repository (cellpy 2.x — recommended):

```shell
conda env create -f environments/cellpy_v2.yml
conda activate cellpy_examples_v2
```

For the latest cellpy 1.x instead, use `environments/cellpy_v1.yml` and
activate `cellpy_examples_v1`. See [environments/README.md](environments/README.md).

To refresh an environment later (after we update the YAML):

```shell
conda env update -f environments/cellpy_v2.yml --prune
```

Then open notebooks or run a script (see below). Some examples may download
small sample data files the first time you run them (network required).

Smoke-test the install:

```shell
python scripts/load_example_data.py
```

## What's in this repo

### `marimo-notebooks/`

[Marimo](https://marimo.io/) notebooks — reactive apps you edit and run in the
browser. From the activated env:

```shell
marimo edit marimo-notebooks/
# or run a specific notebook without editing:
# marimo run marimo-notebooks/some_notebook.py
```

### `jupyter-notebooks/`

Classic Jupyter notebooks. From the activated env:

```shell
jupyter lab
# or: jupyter notebook
```

Open files under `jupyter-notebooks/` in the file browser.

### `scripts/`

Plain Python example scripts. With the env active:

```shell
python scripts/load_example_data.py
```

### `environments/`

Conda environment YAML files for cellpy 1.x and 2.x. See
[environments/README.md](environments/README.md).

### `dev/`

Maintainer helpers (not example content). See [dev/README.md](dev/README.md).

## For developers

If you prefer [uv](https://docs.astral.sh/uv/) instead of conda:

```shell
uv sync
```

That installs a released `cellpy` from PyPI (locked in `uv.lock`). No local
`cellpy` checkout is required.

### Local editable cellpy

To run examples against a local editable `cellpy` clone (branch/checkout
changes show up immediately):

```shell
# default path: ../cellpy (sibling of this repo)
dev/dev_sync.sh

# or an explicit path
dev/dev_sync.sh /path/to/cellpy
# CELLPY_ROOT=/path/to/cellpy dev/dev_sync.sh
```

That syncs from the lock, then runs `uv pip install -e <cellpy>`. No
`[tool.uv.sources]` path is committed (those would break clones with a
different layout, and would rewrite `uv.lock`).

`uv run` auto-syncs and would put PyPI `cellpy` back. After `dev_sync.sh`,
either:

- `export UV_NO_SYNC=1` (script also writes a gitignored `.envrc` for direnv), or
- activate the venv: `source .venv/bin/activate`, or
- `uv run --no-sync ...`

Switch branch in the `cellpy` repo as usual — the editable install tracks that
tree. Re-run `dev/dev_sync.sh` after a plain `uv sync` / `uv add`.

Back to locked PyPI `cellpy`:

```shell
dev/dev_sync.sh --pypi
```
