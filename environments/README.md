# Conda environments

Pick the cellpy major version you want, then create the env from the repo root:

```shell
# cellpy 2.x (recommended for new work)
conda env create -f environments/cellpy_v2.yml
conda activate cellpy_examples_v2

# cellpy 1.x (legacy examples / comparison)
conda env create -f environments/cellpy_v1.yml
conda activate cellpy_examples_v1
```

Update an existing env after we change a YAML:

```shell
conda env update -f environments/cellpy_v2.yml --prune
```

| File | Env name | cellpy |
|------|----------|--------|
| `cellpy_v2.yml` | `cellpy_examples_v2` | latest 2.x from PyPI |
| `cellpy_v1.yml` | `cellpy_examples_v1` | latest 1.x from PyPI |

`cellpy` is installed via pip inside the YAML so you get current PyPI releases
without waiting on conda-forge.
