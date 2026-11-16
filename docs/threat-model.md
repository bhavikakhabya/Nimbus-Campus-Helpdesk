# Part C — Third-party Plugin Threat Model

| Threat | Example | Impact | Concrete mitigation |
|---|---|---|---|
| Prompt injection through Skill text | Skill tells the agent to ignore system/developer instructions, reveal secrets, or trust untrusted timetable content. | Agent may follow malicious instructions or disclose data. | Review Skill files before installation; treat retrieved/user-provided text as data; keep least-privilege access; test adversarial prompts; remove suspicious instructions. |
| Malicious hooks running shell commands | Hook executes a destructive shell command during a tool event. | File deletion, credential theft, or arbitrary local code execution. | Inspect every hook and script; allow only trusted sources; run with least privilege; avoid secrets in environment; use a disposable test repo; disable hooks if not needed. |
| Tool poisoning through MCP descriptions | Tool description contains misleading instructions or asks the model to exfiltrate data. | Model may call tools incorrectly or disclose sensitive information. | Read tool names/descriptions/schemas and server source; pin trusted package versions; restrict tools to mock data; validate arguments server-side; review calls and outputs. |

## Additional controls

- Install only from a source you can inspect and trust.
- Check manifest, marketplace source, hook commands, MCP command/args, and environment variables before enabling.
- Use mock data and a disposable repository for experiments.
- Keep credentials out of sample files and logs.
- Require human review before writes, merges, payments, or other consequential actions.
