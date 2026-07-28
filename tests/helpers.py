"""Small helpers shared by Examples tests."""

from __future__ import annotations

from importlib.metadata import version
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def cellpy_major() -> int:
    return int(version("cellpy").split(".", maxsplit=1)[0])
