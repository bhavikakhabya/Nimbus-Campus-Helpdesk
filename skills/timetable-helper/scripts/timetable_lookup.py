#!/usr/bin/env python3
"""Look up mock campus timetable rows using only the supplied CSV."""
import argparse
import csv
from pathlib import Path


def default_csv_path():
    # This file is root/skills/timetable-helper/scripts/; parents[3] is repo root.
    return Path(__file__).resolve().parents[3] / "data" / "timetable.csv"


def main():
    parser = argparse.ArgumentParser(description="Look up classes in data/timetable.csv")
    parser.add_argument("batch", help="Batch name, for example CSE-A")
    parser.add_argument("day", help="Weekday, for example Monday")
    parser.add_argument("--course", help="Optional course-name filter")
    parser.add_argument("--csv", default=str(default_csv_path()), help="CSV path (optional)")
    args = parser.parse_args()
    path = Path(args.csv)
    if not path.is_file():
        parser.error("CSV file not found: {0}".format(path))
    with path.open("r", newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    matches = [r for r in rows if r.get("batch", "").strip().casefold() == args.batch.strip().casefold()
               and r.get("day", "").strip().casefold() == args.day.strip().casefold()]
    if args.course:
        matches = [r for r in matches if args.course.strip().casefold() in r.get("course", "").casefold()]
    if not matches:
        print("No matching classes found in the supplied CSV.")
        return 0
    for row in matches:
        print("{start_time}-{end_time} | {course} | {faculty} | {room}".format(**row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
