"""Command-line interface for PMO Control Tower."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def _parse_status_date(value: str) -> date:
    """Parse YYYY-MM-DD status date string."""
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"Invalid --status-date '{value}'. Expected format: YYYY-MM-DD (e.g. 2025-05-15)."
        ) from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pmo",
        description="PMO Control Tower data processing CLI.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser(
        "run",
        help="Run the PMO processing pipeline for a given status date.",
    )
    run_parser.add_argument(
        "--status-date",
        required=True,
        type=_parse_status_date,
        help="Reporting status date in YYYY-MM-DD format (e.g. 2025-05-15).",
    )
    run_parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path("data"),
        help="Base data directory (default: data).",
    )
    return parser


def run_pipeline(status_date: date, data_dir: Path) -> int:
    """Placeholder pipeline runner; modules will be wired in as they are built."""
    print(f"PMO Control Tower | status_date={status_date.isoformat()} | data_dir={data_dir}")
    print("Pipeline stub ready: ingest -> validate -> evm / risk_register / montecarlo / cashflow")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "run":
        return run_pipeline(status_date=args.status_date, data_dir=args.data_dir)
    return 1