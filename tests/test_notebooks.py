"""Execute versioned Jupyter / batch notebooks against the matching cellpy major."""

from __future__ import annotations

from pathlib import Path

import pytest
from helpers import REPO_ROOT, cellpy_major


def _notebooks_for(major: int) -> list[Path]:
    root = REPO_ROOT / f"v{major}"
    notebooks = sorted((root / "jupyter-notebooks").glob("*.ipynb"))
    batch = root / "other" / "cellpy batch utility" / "cellpy_batch_processing.ipynb"
    if batch.is_file():
        notebooks.append(batch)
    return notebooks


NOTEBOOKS = [(major, path) for major in (1, 2) for path in _notebooks_for(major)]


@pytest.mark.notebook
@pytest.mark.parametrize(
    ("major", "notebook"),
    NOTEBOOKS,
    ids=[str(path.relative_to(REPO_ROOT)) for _, path in NOTEBOOKS],
)
def test_notebook_executes(major: int, notebook: Path) -> None:
    if cellpy_major() != major:
        pytest.skip(f"installed cellpy is {cellpy_major()}.x; need {major}.x")

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
