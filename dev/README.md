# `dev/` — maintainer helpers

Not example content. Conda environment YAML files live in
[`../environments/`](../environments/).

| File | Purpose |
|------|---------|
| `dev_sync.sh` | Optional: overlay a local editable `cellpy` checkout (uv users) |

## Notebooks and git

Repo root `.pre-commit-config.yaml` runs **ruff** (check `--fix` + format on
`.py` / `.ipynb`) then **nbstripout**. After clone:

```shell
uv sync --group dev
uv run pre-commit install
```

## Tests

Full matrix (scripts, jupyter, batch, cookiecutter) for the installed cellpy
major; other major is skipped. See main README.

```shell
uv sync --group dev
MPLBACKEND=Agg uv run pytest tests/ -q
```

## Ruff

Formats/lints `.py` and `.ipynb` (`extend-include` in `pyproject.toml`):

```shell
uv run ruff format .
uv run ruff check --fix .
```

## Local editable cellpy (developers)

See the “For developers” section in the [main README](../README.md).
