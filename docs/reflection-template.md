# Part F — Reflection

## What I Learned

This assignment helped me understand how Skills, plugins, MCP servers, and Git worktrees support different parts of an AI-agent development workflow.

A Skill provides reusable instructions and reference material that guide an agent through a particular task. In my project, the timetable-helper Skill explains how timetable information should be checked and why missing classes must never be invented. A plugin packages related capabilities, such as Skills, commands, hooks, and MCP configuration. MCP allows an AI application to communicate with external tools and resources through a standard protocol. I implemented timetable and fee-status tools and a hostel-rules resource using mock data.

The MCP Inspector session was especially useful because I could see the server initialization, tool discovery, resource listing, and actual tool calls. It helped me understand JSON-RPC communication beyond just reading code.

Git worktrees taught me how multiple branches can have separate working directories while sharing repository history. I created three worktrees for Skill testing, MCP development, and hook-path work. I also deliberately created and resolved merge conflicts. This showed me why inspecting conflict markers and reviewing the final file is important.

I learned that AI-generated answers should not automatically be trusted. Technical claims, commands, package names, and security requirements need verification through official documentation or actual tests. I also learned that prompt injection and unsafe shell hooks can create risks if an agent is given excessive permissions.

One limitation was that Claude Code CLI was not installed in my environment. Therefore, I could test the hook script manually and inspect the plugin configuration, but I could not claim a live plugin installation or automatic Skill activation.

Overall, this assignment improved my understanding of agent architecture, tool integration, verification, security, and collaborative Git workflows. My biggest takeaway is that AI can assist development, but testing, evidence, and human review remain essential.
