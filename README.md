# Examples

Contains examples of use of cellpy and cellpy-core.

## Setup (everyone)

```shell
uv sync
```

Installs a released `cellpy` from PyPI (locked in `uv.lock`). No local `cellpy`
checkout is required.

## Local cellpy development (optional)

To run examples against a local editable `cellpy` clone (branch/checkout changes
show up immediately):

```shell
# default path: ../cellpy (sibling of this repo)
scripts/dev_sync.sh

# or an explicit path
scripts/dev_sync.sh /path/to/cellpy
# CELLPY_ROOT=/path/to/cellpy scripts/dev_sync.sh
```

That syncs from the lock, then runs `uv pip install -e <cellpy>`. No
`[tool.uv.sources]` path is committed (those would break clones with a different
layout, and would rewrite `uv.lock`).

`uv run` auto-syncs and would put PyPI `cellpy` back. After `dev_sync.sh`, either:

- `export UV_NO_SYNC=1` (script also writes a gitignored `.envrc` for direnv), or
- activate the venv: `source .venv/bin/activate`, or
- `uv run --no-sync ...`

Switch branch in the `cellpy` repo as usual — the editable install tracks that
tree. Re-run `scripts/dev_sync.sh` after a plain `uv sync` / `uv add`.

Back to locked PyPI `cellpy`:

```shell
scripts/dev_sync.sh --pypi
```
