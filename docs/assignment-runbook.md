# Assignment Runbook — follow in order

## Part B — Skill

1. Read `skills/timetable-helper/SKILL.md`.
2. Run the helper script:
   - `python3 skills/timetable-helper/scripts/timetable_lookup.py CSE-A Monday`
   - `python3 skills/timetable-helper/scripts/timetable_lookup.py CSE-A Friday --course Python`
   - `python3 skills/timetable-helper/scripts/timetable_lookup.py CSE-C Monday`
3. Use the six prompts in `skill-test-matrix.md` in the agent platform you are evaluating. Record actual trigger results and reasons.
4. Test both alternate descriptions in `description-experiments.md`. Do not invent trigger results; record what the platform actually did.

## Part C — Plugin

1. Review every file under `plugins/campus-helpdesk/`, especially `hooks/scripts/protect-data.sh`. Hooks execute local commands; understand them before enabling.
2. Install the MCP dependency as described in `mcp-server/README.md`.
3. Follow the current official Claude Code plugin documentation for marketplace add/install/list/uninstall syntax. Run the exact commands in your installed Claude Code version and paste the outputs into `plugin-evidence.md`. The local marketplace manifest is at `marketplace/.claude-plugin/marketplace.json`; if the CLI rejects the relative plugin source, use the documented local plugin-directory development workflow and explain the difference.
4. Complete `threat-model.md` with your own review.

## Part D — MCP

1. Start the server and test all two tools and the resource using MCP Inspector.
2. Capture screenshots in `screenshots/`.
3. In `mcp-protocol-trace.md`, record the actual initialize, tools/list, and tools/call exchanges from your client. Annotate the negotiated protocol version and capabilities as shown by your actual run. Do not paste a generic trace as if captured.
4. Demonstrate a bad input and record the actual client-visible error.
5. Search for `@nimbus/mcp-skill-bridge` and version `2.3` in authoritative package registries. If no authoritative package listing is found, say “not verified/found in the registries checked” rather than claiming universal nonexistence. Include registries, search date, and results.

## Part E — Worktrees

Follow `worktree-lab.md` from a clean Git repository. Use separate terminal windows or tabs for each worktree. Capture `git worktree list` and `git log --graph --oneline --decorate --all` outputs. The conflict should be deliberately created and manually reviewed.

## Part F — Reflection and prompt log

Fill `prompt-log-template.md` as you work. At least five entries must describe a real incorrect or unverifiable AI output you encountered and how you checked it. Write your own reflection in `reflection-template.md`; edit the starter draft to accurately represent your experience.
