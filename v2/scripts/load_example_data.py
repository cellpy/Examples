"""Load a local example cellpy file and print a short summary.

Uses the vendored fixture under ``example_data/`` (no network, no mdbtools).
From the repo root, with an examples conda env active:

    python v2/scripts/load_example_data.py
"""

from importlib.metadata import version
from pathlib import Path

import cellpy

FIXTURE = Path(__file__).resolve().parents[2] / "example_data" / "data" / "20180418_sf033_4_cc.cellpy"


def main() -> None:
    print(f"cellpy {version('cellpy')}")
    assert FIXTURE.is_file(), FIXTURE
    cell = cellpy.get(FIXTURE)
    cycles = list(cell.get_cycle_numbers())
    print(f"cycles: {len(cycles)} (first: {cycles[:5]})")
    summary = cell.data.summary
    if summary is not None and not summary.empty:
        print(summary.head())


if __name__ == "__main__":
    main()
