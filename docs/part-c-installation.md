# Part C – Plugin Installation and Verification

## Plugin
Name: campus-helpdesk
Marketplace: nimbus-campus-marketplace
Source: ./plugins/campus-helpdesk

## Prerequisites
- Claude Code installed and available in the terminal.
- The project folder contains .claude-plugin/marketplace.json.
- The plugin folder contains its manifest, Skill, command, hook, and MCP configuration.

## 1. Add the local marketplace
Run from the project root:

claude plugin marketplace add ./

Expected: Successfully added marketplace.

## 2. Install the plugin
claude plugin install campus-helpdesk@nimbus-campus-marketplace --scope local

The local scope enables the plugin only for the current repository.

## 3. Verify installation
claude plugin list

Also open a Claude Code session and run:

/plugin

Check that campus-helpdesk appears in the Installed tab. Check that its timetable command or Skill is available.

## 4. Test the plugin
- Try the timetable-check command with a valid batch and day.
- Confirm the timetable Skill uses the supplied CSV.
- Check the MCP server status using /mcp.
- Test the data-protection hook in a controlled environment.

## 5. Uninstall the plugin
claude plugin uninstall campus-helpdesk@nimbus-campus-marketplace --scope local

## 6. Remove the marketplace
claude plugin marketplace remove nimbus-campus-marketplace

## Verification status
The JSON files were validated using Python's JSON parser.
The protection hook passed three manual shell tests.
Claude Code was not installed in the development environment, so marketplace installation, plugin loading, slash-command activation, and live MCP connection were not verified.
