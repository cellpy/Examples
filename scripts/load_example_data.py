"""Load cellpy's bundled Arbin example and print a short summary.

Needs network the first time (downloads a small fixture). From the repo root,
with an examples conda env active:

    python scripts/load_example_data.py
"""

from importlib.metadata import version

from cellpy.utils import example_data


def main() -> None:
    print(f"cellpy {version('cellpy')}")
    cell = example_data.raw_file()
    cycles = list(cell.get_cycle_numbers())
    print(f"cycles: {len(cycles)} (first: {cycles[:5]})")
    summary = cell.data.summary
    if summary is not None and not summary.empty:
        print(summary.head())


if __name__ == "__main__":
    main()
