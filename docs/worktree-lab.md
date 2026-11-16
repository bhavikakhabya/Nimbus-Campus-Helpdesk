# Part E — Git Worktree Lab

Run these commands from the repository root. Start from a clean working tree and commit the current project first. Do not run all commands blindly; read each step.

## 1. Commit a baseline

```bash
git status
git add .
git commit -m "Create campus helpdesk assignment starter"
```

If Git asks for identity, configure your own name/email locally before committing.

## 2. Create three branches and linked worktrees

```bash
git branch feature/skill-tests
git branch feature/mcp-server
git branch bugfix/hook-path
mkdir -p ../Nimbus-worktrees
git worktree add ../Nimbus-worktrees/skill-tests feature/skill-tests
git worktree add ../Nimbus-worktrees/mcp-server feature/mcp-server
git worktree add ../Nimbus-worktrees/hook-path bugfix/hook-path
git worktree list
```

## 3. Make independent changes

In `../Nimbus-worktrees/skill-tests`, append a unique line to `docs/parallel-notes.md` and commit it. In `../Nimbus-worktrees/mcp-server`, append a different unique line to the same file and commit it. In `../Nimbus-worktrees/hook-path`, create `docs/hook-path-note.md` and commit it. Create the shared file in each branch if needed, with the same first line so the next step conflicts.

## 4. Deliberately create and resolve a conflict

A reliable method: on `feature/skill-tests`, edit the same line in `docs/parallel-notes.md` to `Decision: timetable tests validated.` and commit. On `feature/mcp-server`, edit that exact same line to `Decision: MCP server validated.` and commit. Then merge one branch into the other from the skill-tests worktree:

```bash
git merge feature/mcp-server
```

Git should report a conflict if both branches changed the same line differently. Open the conflicted file, inspect both changes, choose or combine the correct wording, remove conflict markers, then:

```bash
git add docs/parallel-notes.md
git commit -m "Resolve parallel worktree conflict"
git log --graph --oneline --decorate --all
```

If you do not get a conflict, stop and inspect the file histories; do not claim a conflict was resolved.

## 5. Conceptual answers

- **Why same branch is blocked:** Git normally prevents one branch from being checked out in multiple linked worktrees at the same time, avoiding simultaneous working-directory changes to the same branch reference.
- **Shared vs separate:** linked worktrees share the repository's Git object database and refs/metadata managed by the common repository, while each has its own working directory and index. Untracked files, build outputs, `node_modules`, and local environment files are not automatically shared; each worktree may need its own install/configuration.
- **Stale cleanup:** inspect `git worktree list`; confirm the directory is truly disposable; use `git worktree remove <path>` for a valid worktree, then `git worktree prune` only to clean stale administrative entries. Avoid deleting directories blindly.

## 6. Evaluate `/worktree-merge`

Search current official Claude Code documentation/command reference for this exact built-in command. Record the official URL and access date. If you cannot find it in official docs, label it Unverified/not documented rather than claiming it exists. Even when an agent assists with a merge, inspect the diff, tests, conflict resolution, and commit before accepting it.

## Evidence checklist

Save terminal screenshots or copied outputs for `git worktree list`, the conflict markers before resolution, the resolved file, and `git log --graph --oneline --decorate --all`.
