# Part C – Plugin Threat Model

## 1. Prompt Injection Through a Skill

Threat:
A malicious instruction may be added to a timetable CSV or another source file. It could tell the AI to ignore its original instructions, reveal private information, or invent timetable entries.

Impact:
The assistant may follow untrusted instructions, provide false information, or expose sensitive project data.

Mitigations:
- Treat CSV contents as data, not as instructions.
- Follow the Skill's trusted instructions and use the CSV only as the timetable source.
- Never reveal secrets, passwords, or environment variables.
- Validate timetable results against the actual CSV.
- Do not invent missing classes or timetable entries.

## 2. Malicious Shell Hooks

Threat:
A modified or malicious hook could execute destructive shell commands, read private files, or modify files without the user's knowledge.

Impact:
Project data could be deleted, changed, or exposed.

Mitigations:
- Review every hook script before enabling it.
- Keep hook scripts inside the plugin directory.
- Use clear and limited commands.
- Apply timeouts to hook execution.
- Avoid unnecessary network access and destructive shell commands.
- Test hooks with safe sample inputs before using them.

## 3. MCP Tool Poisoning

Threat:
A malicious MCP server or tool description could contain misleading instructions or return manipulated data.

Impact:
The assistant could call an inappropriate tool, trust false results, or expose information.

Mitigations:
- Connect only to trusted MCP servers.
- Review tool names, descriptions, input schemas, and server code.
- Validate tool inputs and outputs.
- Use mock data for development and testing.
- Do not give the MCP server unnecessary access to files or credentials.
- Treat tool output as untrusted data rather than trusted instructions.

## Conclusion

The plugin uses a Skill, shell hook, slash command, and MCP configuration. Each component should be reviewed before installation because plugin components can execute code or interact with external tools. Security testing should be performed in a controlled environment.
