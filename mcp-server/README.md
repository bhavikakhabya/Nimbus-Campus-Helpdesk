# Nimbus Campus Helpdesk MCP Server

## Important

This server uses **fictional mock data only**. `data/timetable.csv`, `data/fee_status.json`, and `data/hostel-rules.md` are assignment samples, not official university records. Do not enter real student IDs or fee data.

## Requirements

- Python 3.10+ recommended for the v1 SDK line.
- Install dependencies in the same Python environment that launches the server:

```bash
python3 -m pip install -r mcp-server/requirements.txt
```

Run from the repository root:

```bash
NIMBUS_PROJECT_ROOT="$PWD" python3 mcp-server/server.py
```

The server communicates over stdio. Do not add ordinary `print()` debugging output to stdout; protocol messages use stdout. Send diagnostics to stderr.

## Exposed MCP features

- `get_timetable(batch, day)`: validates inputs and returns matching rows from the CSV.
- `get_fee_status(student_id)`: returns one of three fictional fee records.
- `hostel://rules`: reads the mock hostel rules Markdown document.

## Test with MCP Inspector

From the repository root, start the Inspector in another terminal:

```bash
npx -y @modelcontextprotocol/inspector
```

Use the Inspector's stdio connection option and configure the command as `python3`, with arguments `mcp-server/server.py`. Set `NIMBUS_PROJECT_ROOT` to the absolute path of this repository. Then test `get_timetable` with `CSE-A` / `Monday`, `get_fee_status` with `STU1002`, and open `hostel://rules`.

Capture your own Inspector screenshots or logs in `screenshots/`. Do not claim a test passed until you have run it locally.

## Failure case to demonstrate

Call `get_fee_status` with `STU9999`, or call `get_timetable` with an invalid day such as `Funday`. The server raises a validation error; record the actual error shown by your MCP client. Exact error wrapping can differ by SDK/client version.

## SDK version note

This starter pins the v1 API (`mcp>=1.28,<2`) because it uses `mcp.server.fastmcp.FastMCP`. The official Python SDK v2 has breaking API changes; do not remove the upper bound without migrating imports and re-testing. See the official SDK migration notes.
