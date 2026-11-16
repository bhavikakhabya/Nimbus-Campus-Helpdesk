"""Nimbus Campus Helpdesk MCP server. Uses fictional local mock data only."""
import csv
import json
import os
from pathlib import Path
from mcp.server.fastmcp import FastMCP

ROOT = Path(os.environ.get("NIMBUS_PROJECT_ROOT", Path(__file__).resolve().parents[1])).resolve()
DATA = ROOT / "data"
server = FastMCP("nimbus-campus-helpdesk")


def load_timetable():
    path = DATA / "timetable.csv"
    with path.open("r", newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


@server.tool()
def get_timetable(batch: str, day: str) -> dict:
    """Return classes listed in the mock timetable for an exact batch and weekday. Never infer missing classes."""
    if not isinstance(batch, str) or not batch.strip():
        raise ValueError("batch must be a non-empty string, for example CSE-A")
    if not isinstance(day, str) or day.strip().casefold() not in {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}:
        raise ValueError("day must be a weekday name")
    rows = load_timetable()
    matches = [row for row in rows if row["batch"].strip().casefold() == batch.strip().casefold()
               and row["day"].strip().casefold() == day.strip().casefold()]
    return {"batch": batch, "day": day, "count": len(matches), "classes": matches,
            "data_notice": "Fictional assignment sample data; not an official university timetable."}


@server.tool()
def get_fee_status(student_id: str) -> dict:
    """Return a fictional fee-status record for a mock student ID (STU1001-STU1003); do not use real student data."""
    if not isinstance(student_id, str) or not student_id.strip():
        raise ValueError("student_id must be a non-empty string")
    path = DATA / "fee_status.json"
    records = json.loads(path.read_text(encoding="utf-8"))
    key = student_id.strip().upper()
    if key not in records:
        raise ValueError("Unknown mock student ID. Try STU1001, STU1002, or STU1003.")
    return {"student_id": key, **records[key]}


@server.resource("hostel://rules")
def hostel_rules() -> str:
    """Read the fictional hostel rules document supplied with this assignment."""
    return (DATA / "hostel-rules.md").read_text(encoding="utf-8")


if __name__ == "__main__":
    # stdio is the default transport for this assignment.
    server.run()
