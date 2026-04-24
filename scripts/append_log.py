#!/usr/bin/env python3
"""Append a structured entry to a wiki's log.md."""

import argparse
import datetime
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Append a structured entry to log.md")
    parser.add_argument("operation", help="Operation type (e.g. init, ingest, lint, query)")
    parser.add_argument("title", help="Short title for the log entry")
    parser.add_argument("body", nargs="?", default="", help="Free-form body text")
    args = parser.parse_args()

    log_path = Path("log.md")
    if not log_path.exists():
        print("error: log.md does not exist in the current directory", file=sys.stderr)
        sys.exit(1)

    operation = args.operation.replace("\n", " ").strip()
    title = args.title.replace("\n", " ").strip()
    date = datetime.date.today().isoformat()

    entry = f"\n## [{date}] {operation} | {title}\n\n"
    if args.body:
        entry += f"{args.body}\n"

    with open(log_path, "a") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
