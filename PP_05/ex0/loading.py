##!/usr/bin/env python3
"""Load the declared reagents and compare pip vs Poetry."""

import os
import sys
from importlib import import_module
from importlib.metadata import PackageNotFoundError, version

# Must match requirements.txt and pyproject.toml
REAGENTS = ["pandas", "numpy", "matplotlib"]


def detect_environment() -> str:
    """Return a short description of the active environment."""
    in_venv = sys.prefix != sys.base_prefix
    env_path = sys.prefix

    if not in_venv:
        return "global interpreter (WARNING: laboratory is not sealed!)"
    if os.environ.get("POETRY_ACTIVE") or "pypoetry" in env_path:
        return f"Poetry-managed virtual environment ({env_path})"
    return f"pip / venv virtual environment ({env_path})"


def load_reagent(name: str) -> bool:
    """Import a reagent and print its installed version."""
    try:
        import_module(name)
        print(f"  [OK]      {name:<12} version {version(name)}")
        return True
    except (ImportError, PackageNotFoundError):
        print(f"  [MISSING] {name:<12} not installed in this environment")
        return False


def show_comparison() -> None:
    """Print the difference between pip and Poetry."""
    rows = [
        ("Aspect", "pip", "Poetry"),
        ("Dependency file", "requirements.txt", "pyproject.toml"),
        ("Lock file", "none (manual pip freeze)", "poetry.lock (automatic)"),
        ("Virtual env", "manual (python -m venv)", "automatic"),
        ("Dep. resolution", "installs what you list", "resolves full tree"),
        ("Install", "pip install -r requirements.txt", "poetry install"),
        ("Run", "python loading.py", "poetry run python loading.py"),
    ]
    widths = [max(len(row[i]) for row in rows) for i in range(3)]

    print("\nPip vs Poetry:")
    for index, row in enumerate(rows):
        line = " | ".join(cell.ljust(widths[i]) for i, cell in enumerate(row))
        print("  " + line)
        if index == 0:
            print("  " + "-+-".join("-" * w for w in widths))


def main() -> int:
    print("LOADING PROGRAMS...")
    print(f"Environment: {detect_environment()}\n")

    print("Checking reagents:")
    results = [load_reagent(name) for name in REAGENTS]

    if not all(results):
        print("\nSome reagents are missing. Install them with either:")
        print("  pip:    python -m venv venv && source venv/bin/activate")
        print("          pip install -r requirements.txt")
        print("  Poetry: poetry install && poetry run python loading.py")
        return 1

    show_comparison()
    print("\nAll reagents loaded. The laboratory is reproducible.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
