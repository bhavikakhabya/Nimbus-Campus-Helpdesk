# Part A — Verification Log

Claim: 1
Verdict: True
Evidence: MCP uses JSON-RPC 2.0 and defines
tools, resources and prompts.
Source: https://modelcontextprotocol.io/specification/2025-03-26
Verification: Checked JSON-RPC and server features sections.


Claim: 2
Verdict: False

Evidence:
The claimed specification date is invalid because
February does not have 30 days. The official MCP
specification describes tools, resources and prompts,
but does not require a Persistent Memory Primitive.

Source:
https://modelcontextprotocol.io/specification/2025-03-26


Claim: 3
Verdict: True

Evidence:
A Skill is a folder containing a SKILL.md file.
Its YAML frontmatter requires name and description.
Agents use progressive disclosure by loading metadata
first and the full instructions when the Skill is activated.

Source:
https://agentskills.io/specification

Accessed: 16 November 2026


Claim: 4
Verdict: False

Evidence:
The Agent Skills specification requires a SKILL.md
file with YAML frontmatter containing name and
description. It does not require skill.config.yaml
or a mandatory runtime field such as python3.14.

Source:
https://agentskills.io/specification

Accessed: 16 November 2026


Claim: 5
Verdict: True

Evidence:
Git supports multiple linked working trees attached
to one repository. They share repository data,
including the object database, while maintaining
separate working directories and per-worktree files
such as HEAD and index.

Source:
https://git-scm.com/docs/git-worktree

Accessed: 16 November 2026


Claim: 6
Verdict: False

Evidence:
The official Git worktree documentation does not
include a sync command or a --all option for syncing
and rebasing every linked worktree. Git provides
separate commands such as add, list, remove and prune.

Source:
https://git-scm.com/docs/git-worktree

Accessed: 16 November 2026


Claim: 7
Verdict: True

Evidence:
Claude Code plugins can bundle multiple extension
components, including slash commands, subagents,
Skills, hooks and MCP server configurations into
one installable plugin.

Source:
https://code.claude.com/docs/en/plugins

Accessed: 16 November 2026


Claim: 8
Verdict: False

Evidence:
RFC 9999 is about the RATS Conceptual Message
Wrapper, not MCP Transport Security. Although it
describes signing mechanisms for CMW messages, it
does not mandate Ed25519 signatures for every
stdio MCP server.

Source:
https://www.rfc-editor.org/rfc/rfc9999.html

Accessed: 16 November 2026


Claim: 9
Verdict: False

Evidence:
Git normally prevents the same branch from being
checked out in multiple worktrees at the same time.
The --force option can override this restriction,
but Git does not allow it by default.

Source:
https://git-scm.com/docs/git-worktree

Accessed: 16 November 2026


Claim: 10
Verdict: Unverified

Evidence:
The exact research paper attributed to Hendricks
and Oyelaran (2024), including the claimed 40%
accuracy drop and the term "skill collapse", could
not be independently verified. No reliable matching
publication record was located in the searches
performed. Therefore, the claim remains Unverified.

Search locations:
https://scholar.google.com/
https://search.crossref.org/
https://arxiv.org/

Accessed: 16 November 2026


## Package Verification: @nimbus/mcp-skill-bridge

Date: 16 November 2026

Command executed:

npm view @nimbus/mcp-skill-bridge@2.3.0 version

Result:
- npm returned E404 Not Found.
- The public npm registry did not return the requested package/version.
- Package status: Not found on the public npm registry; global non-existence is not established.
- No installation was performed.
- The project uses the official Python MCP SDK package `mcp` instead.

This result is recorded as verification evidence, not as proof that the package cannot exist in a private registry.
