# Part A — Claim Audit (15 Marks)

**Assignment:** Building and Auditing an AI-Agent Toolchain  
**Project:** Nimbus Campus Helpdesk  
**Research date used in this draft:** 16 November 2026  

> **Important:** This is a research draft based on the cited primary/official documentation. Before submission, open each URL yourself, confirm it still supports the wording, and update the access date to the date you personally checked it. Claim 10 is deliberately marked **Unverified**: a failed literature search is not proof that a paper does not exist.

## Required summary table

| Claim No. | Verdict | Correction | Source URL | Date Accessed |
|---:|---|---|---|---|
| 1 | **True** | MCP uses JSON-RPC 2.0 and defines tools, resources and prompts as server features/primitives. | https://modelcontextprotocol.io/specification/2025-03-26 | 16 Nov 2026 — re-check personally |
| 2 | **False** | `2025-02-30` is not a valid calendar date, and the MCP specification does not define a mandatory “Persistent Memory Primitive”. | https://modelcontextprotocol.io/specification/2025-03-26 | 16 Nov 2026 — re-check personally |
| 3 | **True** | An Agent Skill is a directory with a `SKILL.md`; `name` and `description` are required frontmatter fields. Discovery loads metadata first, with instructions and supporting files available when relevant. | https://agentskills.io/specification | 16 Nov 2026 — re-check personally |
| 4 | **False** | A mandatory `skill.config.yaml` and `runtime: python3.14` field are not part of the Agent Skills format. The required manifest is `SKILL.md`; scripts and references are optional supporting files. | https://agentskills.io/specification | 16 Nov 2026 — re-check personally |
| 5 | **True** | Git supports multiple linked working trees attached to one repository. They have separate working directories while sharing repository data such as the object database. | https://git-scm.com/docs/git-worktree | 16 Nov 2026 — re-check personally |
| 6 | **False** | `git worktree sync --all` is not a documented Git worktree subcommand. The documented commands include `add`, `list`, `remove`, `prune`, `repair`, `lock`, `unlock` and `move`; updating branches requires normal Git fetch/merge/rebase operations. | https://git-scm.com/docs/git-worktree | 16 Nov 2026 — re-check personally |
| 7 | **True (Claude Code context)** | Claude Code plugins can package slash commands, agents, Skills, hooks and MCP server configuration. This statement should be scoped to Claude Code's plugin system, not generalized to every plugin ecosystem. | https://code.claude.com/docs/en/plugins | 16 Nov 2026 — re-check personally |
| 8 | **False** | RFC 9999 is titled “Remote ATtestation procedureS (RATS) Conceptual Message Wrapper (CMW)”; it is not an MCP transport-security RFC and does not establish the stated Ed25519 signing requirement for stdio MCP servers. | https://www.rfc-editor.org/rfc/rfc9999.html | 16 Nov 2026 — re-check personally |
| 9 | **False** | Git normally refuses to check out a branch already checked out in another worktree. `git worktree add --force` can override the safeguard, but it is not the default behaviour. | https://git-scm.com/docs/git-worktree | 16 Nov 2026 — re-check personally |
| 10 | **Unverified** | The briefing gives no paper title, venue, DOI or stable identifier. The claimed authors, “skill collapse” term and 40% figure must not be treated as established without locating and checking the original paper. Record the exact databases and queries you searched; do not convert “not found” into “False”. | https://scholar.google.com/ ; https://search.crossref.org/ ; https://arxiv.org/search/ | 16 Nov 2026 — record your own searches |

## Reasoning (2–3 sentences per claim)

### Claim 1 — True
MCP messages use JSON-RPC 2.0, and the server-side feature model includes tools, resources and prompts. These features serve different purposes: tools are callable operations, resources provide context/data, and prompts provide reusable prompt templates. See the MCP specification's architecture and server feature sections.

### Claim 2 — False
The stated revision date, 2025-02-30, is invalid because February 2025 did not have a 30th day. More importantly, the MCP specification does not require a “Persistent Memory Primitive”; a server may implement its own state or storage, but that is not the mandatory primitive described in the claim.

### Claim 3 — True
The Agent Skills format describes a Skill as a directory containing at least a `SKILL.md` file with YAML frontmatter. The required metadata includes `name` and `description`, allowing an agent to identify a Skill before loading its detailed instructions and optional supporting resources.

### Claim 4 — False
The Agent Skills specification does not require a separate `skill.config.yaml` file or a `runtime` field. A Skill may include scripts and reference documents, but those are supporting resources rather than mandatory runtime declarations.

### Claim 5 — True
Git worktrees let a repository have more than one working directory attached to it, so separate branches can be worked on in parallel. The worktrees share the repository's underlying Git object storage and common repository metadata, while each has its own checked-out files and working state.

### Claim 6 — False
The official `git worktree` manual does not list `sync` as a subcommand, and it does not describe an operation that automatically pulls and rebases every worktree. A developer must fetch and integrate upstream changes using ordinary Git commands in the relevant worktree.

### Claim 7 — True, with scope
Claude Code's plugin system supports bundling components such as commands, agents, Skills, hooks and MCP server configuration for distribution. The claim is accurate for Claude Code, but the exact contents and manifest format are platform-specific and should not be assumed for all plugin systems.

### Claim 8 — False
The RFC Editor identifies RFC 9999 as a RATS Conceptual Message Wrapper document, not “MCP Transport Security”. Its subject does not establish a rule requiring every stdio MCP server to be signed with an Ed25519 key before launch, so the citation does not support the CTO's claim.

### Claim 9 — False
Git's worktree documentation explicitly says that adding a branch already checked out in another worktree is refused by default. The `--force` option can override that protection, which is why the statement that Git permits it by default is incorrect.

### Claim 10 — Unverified
The briefing does not provide enough bibliographic information to identify the alleged Hendricks and Oyelaran paper reliably. Search scholarly indexes and preprint repositories using the author names, the phrase “skill collapse”, and the exact “12 Skills”/“40 percent” claim; if no primary paper can be confirmed, retain the Unverified verdict and describe the searches performed.

## Official / primary references

1. Model Context Protocol specification: https://modelcontextprotocol.io/specification/2025-03-26
2. Agent Skills specification: https://agentskills.io/specification
3. Git worktree manual: https://git-scm.com/docs/git-worktree
4. Claude Code plugins documentation: https://code.claude.com/docs/en/plugins
5. RFC 9999, RFC Editor: https://www.rfc-editor.org/rfc/rfc9999.html
6. Literature discovery (not proof by itself): https://scholar.google.com/ ; https://search.crossref.org/ ; https://arxiv.org/search/

## Student verification checklist

- [ ] Open every official URL and check the exact relevant section.
- [ ] Replace the draft access dates with the date you personally accessed each source.
- [ ] For Claim 10, write down the exact search terms and databases actually used.
- [ ] Keep a screenshot or note of evidence for each verdict.
- [ ] Make sure the report table and this explanation agree exactly.
