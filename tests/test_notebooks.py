"""Execute selected Jupyter notebooks."""

from __future__ import annotations

from pathlib import Path

import pytest

from helpers import REPO_ROOT, cellpy_major

# Start small: one tutorial notebook for cellpy 2.x. Expand later.
NOTEBOOKS_V2 = [
    REPO_ROOT / "v2" / "jupyter-notebooks" / "01_loading_data.ipynb",
]


@pytest.mark.notebook
@pytest.mark.parametrize(
    "notebook",
    NOTEBOOKS_V2,
    ids=lambda p: str(p.relative_to(REPO_ROOT)),
)
def test_notebook_executes(notebook: Path) -> None:
    if cellpy_major() != 2:
        pytest.skip(f"installed cellpy is {cellpy_major()}.x; need 2.x")

    from nbclient import NotebookClient
    from nbformat import read

    assert notebook.is_file(), notebook
    with notebook.open(encoding="utf-8") as fh:
        nb = read(fh, as_version=4)

    # cwd = notebook directory so ../../example_data resolves.
    client = NotebookClient(
        nb,
        timeout=600,
        kernel_name="python3",
        resources={"metadata": {"path": str(notebook.parent)}},
    )
    client.execute()
