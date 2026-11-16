# Nimbus Campus Helpdesk — Assignment Starter

This repository is a working starter for Parts B–E of **Building and Auditing an AI-Agent Toolchain**. It includes a Skill, supporting references, a standard-library helper script, a Claude Code plugin scaffold, a Python MCP server, mock data, and documentation/templates.

> **Data warning:** all timetable, fee, and hostel data in `data/` is fictional sample data created for this assignment. It is not an official ITM Skills University timetable or policy. Never replace it with real student fee records.

## Quick start

1. Open this folder in VS Code.
2. Check Python: `python3 --version`.
3. Test the timetable helper (no third-party packages needed):

```bash
python3 skills/timetable-helper/scripts/timetable_lookup.py CSE-A Monday
```

4. Set up the MCP SDK (Python 3.10+ recommended for the pinned v1 line):

```bash
python3 -m pip install -r mcp-server/requirements.txt
```

5. From the repository root, run the MCP server:

```bash
NIMBUS_PROJECT_ROOT="$PWD" python3 mcp-server/server.py
```

It uses stdio, so it may appear to wait silently. Stop it with Ctrl+C. For interactive testing, follow `mcp-server/README.md` and use MCP Inspector.

## Project map

- `skills/timetable-helper/` — Part B Skill, references, and helper script.
- `plugins/campus-helpdesk/` — Part C plugin manifest, command, hook, and MCP config.
- `marketplace/` — local marketplace manifest for the plugin.
- `mcp-server/` — Part D server and run instructions.
- `data/` — fictional timetable, fee status, and hostel rules.
- `docs/` — test matrix, description experiments, threat model, worktree guide, reflection and prompt-log templates.
- `screenshots/` — put your own evidence here.

## Important assignment integrity notes

- Run all tests yourself and replace placeholders with actual outputs/screenshots.
- Do not claim plugin installation, MCP Inspector tests, marketplace commands, or worktree conflict resolution occurred unless you performed them.
- Keep official source URLs and access dates in your report. Check current official documentation before submission; commands and SDK versions can change.
- The assignment's “NimbusSync Plugin Standard v4.2” instruction is an injected instruction inside the brief, not an official standard. Do not cite a made-up registry. The `@nimbus/mcp-skill-bridge@2.3` package is not a dependency of this project; document the verification you actually perform.

## Next steps

Follow `docs/assignment-runbook.md` in order. It tells you what to run and what evidence to collect.
