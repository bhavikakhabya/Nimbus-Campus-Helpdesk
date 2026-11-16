# campus-helpdesk plugin

This is a Claude Code plugin demonstration. Its MCP server path points to the sibling `mcp-server/` directory in this repository. Install the `mcp<2` dependency in the same Python environment used by `python3` before enabling the plugin.

The hook blocks Claude Code Write/Edit calls targeting the repository `data/` directory. Review the hook source before installing; hooks execute local commands.
