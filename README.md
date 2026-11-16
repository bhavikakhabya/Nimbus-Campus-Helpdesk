# Nimbus Campus Helpdesk 🤖

### Building and Auditing an AI-Agent Toolchain

Nimbus Campus Helpdesk is an academic project developed as part of the **Building and Auditing an AI-Agent Toolchain** assignment. It demonstrates how AI-agent capabilities can be structured using Skills, Plugins, Model Context Protocol (MCP), and Git Worktrees.

The project provides a fictional campus helpdesk system that can retrieve timetable information, check mock fee-status records, and provide hostel rules through an MCP server.

> **Note:** This project uses fictional demonstration data. It is not connected to official university systems or student records.

---

## 🎯 Project Objectives

- Build a reusable AI Skill for timetable-related queries.
- Package related capabilities into a Claude Code plugin structure.
- Implement an MCP server using the official Python MCP SDK.
- Understand JSON-RPC communication and tool discovery.
- Test safety hooks and document potential security risks.
- Explore parallel development using Git Worktrees.
- Audit technical claims and verify AI-generated information.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | MCP server implementation |
| MCP Python SDK | Tool and resource integration |
| JSON-RPC 2.0 | Communication protocol |
| CSV | Mock timetable data |
| JSON | Mock fee-status data |
| Markdown | Skills and documentation |
| Bash | Safety hook implementation |
| Git & GitHub | Version control and collaboration |
| MCP Inspector | Server testing and protocol inspection |

## 📁 Project Structure

```text
Nimbus-Campus-Helpdesk/
│
├── .claude-plugin/
│   └── marketplace.json
│
├── data/
│   ├── timetable.csv
│   ├── fee_status.json
│   └── hostel-rules.md
│
├── docs/
│   ├── part-a-claim-audit.md
│   ├── part-c-installation.md
│   ├── part-c-threat-model.md
│   ├── part-d-jsonrpc-evidence.md
│   ├── part-d-test-results.md
│   ├── worktree-lab.md
│   ├── verification-log.md
│   └── ...
│
├── mcp-server/
│   ├── server.py
│   ├── requirements.txt
│   └── README.md
│
├── plugins/
│   └── campus-helpdesk/
│       ├── .claude-plugin/
│       ├── commands/
│       ├── hooks/
│       ├── skills/
│       └── .mcp.json
│
├── skills/
│   └── timetable-helper/
│       ├── SKILL.md
│       ├── references/
│       └── scripts/
│
├── screenshots/
├── README.md
└── .gitignore
```

## ✨ Main Components

### 1. Timetable Helper Skill

The `timetable-helper` Skill provides reusable instructions for timetable-related queries.

Features:
- Reads timetable information from CSV.
- Supports batch and weekday-based lookups.
- Includes CSV column documentation.
- Handles missing timetable entries safely.
- Prevents unsupported or invented class information.

### 2. Campus Helpdesk Plugin

The `campus-helpdesk` plugin demonstrates a modular plugin structure.

It includes:
- Timetable Helper Skill.
- `/timetable-check` custom command.
- PreToolUse safety hook.
- MCP server configuration.
- Plugin manifest and marketplace entry.

### 3. MCP Server

The Python MCP server exposes two tools and one resource.

**Tools**

| Tool | Description |
|---|---|
| `get_timetable(batch, day)` | Retrieves timetable entries for a batch and weekday. |
| `get_fee_status(student_id)` | Retrieves a mock fee-status record. |

**Resource**

| Resource URI | Description |
|---|---|
| `hostel://rules` | Provides the fictional hostel rules document. |

The server uses standard input/output (stdio) transport.

### 4. Git Worktree Lab

Three independent workstreams were created:

- `feature/skill-tests`
- `feature/mcp-server`
- `bugfix/hook-path`

The exercise demonstrates:
- Multiple linked working directories.
- Independent branch commits.
- Deliberate merge conflicts.
- Manual conflict resolution.
- Worktree cleanup and Git history inspection.

### 5. Claim Audit and Security

The documentation includes:
- Technical claim verification.
- Prompt-injection threat analysis.
- Malicious shell-hook risks.
- MCP tool-poisoning risks.
- Package verification.
- AI prompt and verification log.

## 🚀 Setup and Run

### Prerequisites

- Python 3.10 or later.
- pip.
- Git.
- Node.js and npm (for running MCP Inspector).

### 1. Clone the repository

```bash
git clone https://github.com/bhavikakhabya/Nimbus-Campus-Helpdesk.git
cd Nimbus-Campus-Helpdesk
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r mcp-server/requirements.txt
```

### 4. Run the MCP server

```bash
python mcp-server/server.py
```

The server uses stdio transport and waits for MCP client communication.

### 5. Test with MCP Inspector

In a separate terminal, run:

```bash
npx -y @modelcontextprotocol/inspector
```

Connect the Inspector to the Python MCP server using the appropriate local server configuration.

## 🧪 Testing and Evidence

The repository includes documentation and evidence for:

- Timetable helper script tests.
- Skill prompt test matrix.
- Hook safety-script tests.
- MCP tool and resource testing.
- JSON-RPC protocol communication.
- MCP Inspector protocol export.
- Git Worktree and merge-conflict experiments.
- Package verification results.

Refer to the `docs/` directory for detailed reports.

## ⚠️ Limitations

- All timetable, fee-status, and hostel information is fictional demonstration data.
- The project is not connected to a live university database.
- Claude Code CLI was unavailable in the development environment; therefore, live plugin installation and automatic Skill activation were not verified.
- The package `@nimbus/mcp-skill-bridge@2.3.0` returned E404 from the public npm registry during verification. This does not establish whether a private package exists.

## 📚 Learning Outcomes

Through this project, I explored:

- AI-agent Skills and progressive disclosure.
- Plugin architecture and configuration.
- MCP tools, resources, and JSON-RPC communication.
- Safety considerations in agent toolchains.
- Git branches, linked worktrees, and merge conflicts.
- Technical verification and responsible use of AI-generated information.

## 👩‍💻 Author

**Bhavika Khabya**

B.Tech – Computer Science  
ITM Skills University

## 📄 Academic Project

Developed for the assignment:

**Building and Auditing an AI-Agent Toolchain**

---

⭐ If you find this project useful for learning about AI-agent architecture and MCP integration, feel free to explore the repository.
