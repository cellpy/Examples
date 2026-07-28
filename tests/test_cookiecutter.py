"""Smoke-test cookiecutter project templates under v1/ and v2/."""

from __future__ import annotations

from pathlib import Path

import pytest
from helpers import REPO_ROOT, cellpy_major

TEMPLATES = {
    1: REPO_ROOT / "v1" / "other" / "cellpy project template" / "cellpy_cookie_NAME",
    2: REPO_ROOT / "v2" / "other" / "cellpy project template" / "cellpy_cookie_NAME",
}


@pytest.mark.parametrize("major", sorted(TEMPLATES))
def test_cookiecutter_template_generates(major: int, tmp_path: Path) -> None:
    if cellpy_major() != major:
        pytest.skip(f"installed cellpy is {cellpy_major()}.x; need {major}.x")

    template = TEMPLATES[major]
    assert template.is_dir(), template

    from cookiecutter.main import cookiecutter

    # Fixed date so folder name is deterministic (avoids jinja2_time in CI).
    cookiecutter(
        str(template),
        no_input=True,
        output_dir=str(tmp_path),
        extra_context={
            "project_name": "cellpy_examples_smoke",
            "session_id": "smoke_001",
            "author_name": "CI",
            "date": "2026-07-28",
            "experiment_folder_name": "2026_07_28_smoke_001",
            "notebook_name": "smoke_001",
        },
    )

    generated = tmp_path / "2026_07_28_smoke_001"
    assert generated.is_dir(), list(tmp_path.iterdir())
    notebooks = list(generated.glob("*.ipynb"))
    assert notebooks, f"no notebooks in {generated}"
