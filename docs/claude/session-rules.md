# Working rules for Claude sessions

**Every Claude session, in every repository, keeps its context small: quiet tool output, narrow reads and searches, no subagents unless asked, short replies. The plugin puts these rules into every session at its start, and again after `/clear`, compaction and resume.** Decided 2026-10-04, in Marceltov/claude-marketplace's ADR 0008; part of these conventions since 2026-10-30.

## Why

Context is what a session thinks with, and it fills up with whatever the session reads: a 2,000-line test log, a whole file read to find one function, a sweep over directories that have nothing to do with the task. A full context forgets the start of the task, gets compacted and costs more. These rules belong to no single task, so a skill, which loads only when its description matches, would skip exactly the turns where they matter; they go in at session start instead.

## How

The rules, as the hook gives them to each session ([`hooks/session-start.md`](https://github.com/Marceltov/engineering-conventions/blob/main/hooks/session-start.md)):

- **Small tool output:** quiet flags (`pytest -q`, `vitest --reporter=dot`), long output through `tail -n 40` or a targeted `grep`. While iterating, run only the tests that cover the change; run the full suite once before shipping.
- **Narrow reads:** read a file by range when you know where to look; don't re-read a file you've read or just edited.
- **Narrow searches:** from the most likely path outward; don't sweep unrelated directories.
- **No subagents unless asked.** A search-only agent runs on the smallest model (`model: haiku`).
- **No brainstorming** for small, clearly specified changes.
- **A small `CLAUDE.md`**: commands and rules only, task-specific detail in a project skill (see [CLAUDE.md](../repo-setup/claude-md.md)).
- **`/clear` between tasks:** when a task is done (shipped, merged or answered) and the next request is unrelated, say so.
- **Short replies:** what changed and what's left. No preamble, no recap of the diff.

The hook runs on `startup|clear|compact|resume`, so the rules come back after `/clear` and after compaction. The hook file is sent with every session: keep it short, and change it together with this page.

## Rules out

- Dumping full logs, test runs or whole files into the context when a range, a quiet flag or a `grep` would do.
- Subagents the user didn't ask for.
- Replies that recap the diff or open with preamble.
- Rules for every session kept in a skill, which only loads when its description matches, or in a user-level `~/.claude/CLAUDE.md`, which isn't versioned or shared.

## Reference

Marceltov/claude-marketplace's `rules` plugin (ADR 0008), which this page and the hook replace.
