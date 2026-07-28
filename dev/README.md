# `dev/` — maintainer helpers

Not example content. Conda environment YAML files live in
[`../environments/`](../environments/).

| File | Purpose |
|------|---------|
| `dev_sync.sh` | Optional: overlay a local editable `cellpy` checkout (uv users) |

## Notebooks and git

Repo root has `.pre-commit-config.yaml` (`nbstripout`). After clone:

```shell
uv sync --group dev
uv run pre-commit install
```

## Tests

```shell
uv sync --group dev
uv run pytest tests/test_scripts.py -q
MPLBACKEND=Agg uv run pytest tests/test_notebooks.py -q -m notebook
```

## Local editable cellpy (developers)

See the “For developers” section in the [main README](../README.md).
