"""Allow running the package via `python -m pmo`."""

from pmo.cli import main

if __name__ == "__main__":
    raise SystemExit(main())