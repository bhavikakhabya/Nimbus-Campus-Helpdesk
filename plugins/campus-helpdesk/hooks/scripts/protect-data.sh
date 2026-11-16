#!/bin/bash
# Deny Claude Code Write/Edit tool calls targeting the protected data directory.
python3 -c '
import json, os, sys
try:
    payload = json.load(sys.stdin)
except Exception:
    print("Block: unable to validate tool input; refusing protected write.", file=sys.stderr)
    sys.exit(2)
tool_input = payload.get("tool_input") or {}
path = tool_input.get("file_path") or tool_input.get("path") or ""
project = os.path.realpath(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd()))
protected = os.path.realpath(os.path.join(project, "data"))
target = os.path.realpath(path) if path else ""
if target and (target == protected or target.startswith(protected + os.sep)):
    print("Block: data/ is protected; edit it manually after reviewing the change.", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
'
