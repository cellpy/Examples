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

Then open examples under the matching top-level folder (`v1/` or `v2/`).
Some examples may download small sample data files the first time you run
them (network required).

Smoke-test the install:

```shell
python v2/scripts/load_example_data.py
```

## What's in this repo

Versioned example content lives under **`v1/`** and **`v2/`** (pick the one
that matches your conda env). Shared assets stay at the repo root.

### `v1/` / `v2/` (versioned)

Each contains:

- `jupyter-notebooks/` — classic Jupyter tutorials
- `marimo-notebooks/` — Marimo notebooks
- `scripts/` — plain Python example scripts
- `other/cellpy batch utility/` — batch processing notebook + sample raw data
- `other/cellpy project template/` — cookiecutter project template

```shell
jupyter lab
# open e.g. v2/jupyter-notebooks/ in the file browser

marimo edit v2/marimo-notebooks/
python v2/scripts/load_example_data.py
```

### Shared (repo root)

| Path | Purpose |
|------|---------|
| `example_data/` | Sample data files used by the notebooks |
| `environments/` | Conda env YAMLs for cellpy 1.x / 2.x |
| `dev/` | Maintainer helpers (local editable cellpy, etc.) |


See also [environments/README.md](environments/README.md) and
[dev/README.md](dev/README.md).

## For developers

If you prefer [uv](https://docs.astral.sh/uv/) instead of conda:

```shell
uv sync
```

That installs a released `cellpy` from PyPI (locked in `uv.lock`). No local
`cellpy` checkout is required.

### Tests

Smoke tests live under `tests/`. With the uv env (cellpy 2.x):

```shell
uv sync --group dev
uv run pytest tests/test_scripts.py -q
MPLBACKEND=Agg uv run pytest tests/test_notebooks.py -q -m notebook
```

GitHub Actions runs the same for cellpy 2.x, plus a cellpy 1.x job for
`v1/scripts` (see `.github/workflows/examples-tests.yml`).

### Notebooks and git

Jupyter notebooks stay as `.ipynb` so GitHub can render them. A
[pre-commit](https://pre-commit.com/) hook runs
[nbstripout](https://github.com/kynan/nbstripout) so outputs and execution
counts are stripped before commit (cleaner diffs; run notebooks locally as
usual).

One-time setup after clone:

```shell
uv sync --group dev
uv run pre-commit install
```

Strip all notebooks already in the tree (optional):

```shell
uv run pre-commit run nbstripout --all-files
```

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
