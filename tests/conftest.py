"""Shared fixtures for Examples smoke tests."""

from __future__ import annotations

import pytest

from helpers import REPO_ROOT, cellpy_major


@pytest.fixture(scope="session")
def repo_root():
    return REPO_ROOT


@pytest.fixture(scope="session")
def installed_cellpy_major() -> int:
    return cellpy_major()
