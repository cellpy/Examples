"""Smoke-test versioned example scripts against the matching cellpy major."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
from helpers import REPO_ROOT, cellpy_major

SCRIPTS = {
    1: REPO_ROOT / "v1" / "scripts" / "load_example_data.py",
    2: REPO_ROOT / "v2" / "scripts" / "load_example_data.py",
}


def _load_module(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("major", sorted(SCRIPTS))
def test_load_example_data_script(major: int) -> None:
    if cellpy_major() != major:
        pytest.skip(f"installed cellpy is {cellpy_major()}.x; need {major}.x")

    script = SCRIPTS[major]
    assert script.is_file(), script
    module = _load_module(script)
    module.main()
