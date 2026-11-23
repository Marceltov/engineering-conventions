# Working rules for Claude sessions

**Every Claude session, in every repository, keeps its context small: quiet tool output, narrow reads and searches, no subagents unless asked, short replies; and a check whether a process still runs never matches itself. The plugin puts these rules into every session at its start, and again after `/clear`, compaction and resume.** Decided 2026-10-04, in Marceltov/claude-marketplace's ADR 0008; part of these conventions since 2026-10-30. The process check added 2026-11-17.

## Why

Context is what a session thinks with, and it fills up with whatever the session reads: a 2,000-line test log, a whole file read to find one function, a sweep over directories that have nothing to do with the task. A full context forgets the start of the task, gets compacted and costs more. These rules belong to no single task, so a skill, which loads only when its description matches, would skip exactly the turns where they matter; they go in at session start instead.

A session often waits for a job on another machine with a loop like `until ssh host '! pgrep -f "backup.sh"'; do sleep 60; done`. `pgrep -f` matches full command lines, and the shell `ssh` starts on the remote side has the pattern in its own command line, so the check always finds a process and the loop never ends. On 2026-11-17 two such loops waited 11 hours on a backup host that had been idle since morning; it had happened before. The same holds for `bash -c`, `docker exec` and `ps | grep`.

## How

The rules, as the hook gives them to each session ([`hooks/session-start.md`](https://github.com/Marceltov/engineering-conventions/blob/main/hooks/session-start.md)):

- **Small tool output:** quiet flags (`pytest -q`, `vitest --reporter=dot`), long output through `tail -n 40` or a targeted `grep`. While iterating, run only the tests that cover the change; run the full suite once before shipping.
- **Narrow reads:** read a file by range when you know where to look; don't re-read a file you've read or just edited.
- **Narrow searches:** from the most likely path outward; don't sweep unrelated directories.
- **No subagents unless asked.** A search-only agent runs on the smallest model (`model: haiku`).
- **No brainstorming** for small, clearly specified changes.
- **A small `CLAUDE.md`**: commands and rules only, task-specific detail in a project skill (see [CLAUDE.md](../repo-setup/claude-md.md)).
- **`/clear` between tasks:** when a task is done (shipped, merged or answered) and the next request is unrelated, say so.
- **A process check that can't match itself:** "is it still running?" asks `systemctl is-active <unit>` or `pgrep -x <name>` (the process name, not the command line). When only the command line will do, bracket one letter (`pgrep -f '[b]ackup.sh'`): the regex still matches `backup.sh`, but not the literal `[b]ackup.sh` in the checking shell, and no other plain copy of the pattern may be in that same shell. Run the check once by hand against a host known to be idle before a loop waits on it.
- **Credentials:** before using one, search every vault this machine can reach (`op-find <word>`, names only). If several could fit, ask. If a login that should work fails, suspect the credential first and change no infrastructure because of it.
- **Short replies:** what changed and what's left. No preamble, no recap of the diff.

The hook runs on `startup|clear|compact|resume`, so the rules come back after `/clear` and after compaction. The hook file is sent with every session: keep it short, and change it together with this page.

## Rules out

- Dumping full logs, test runs or whole files into the context when a range, a quiet flag or a `grep` would do.
- Subagents the user didn't ask for.
- `pgrep -f`, `pkill -f` or `grep` on a plain pattern inside `ssh '…'`, `bash -c` or `docker exec`, and a wait loop whose check was never seen to report idle.
- Replies that recap the diff or open with preamble.
- Rules for every session kept in a skill, which only loads when its description matches, or in a user-level `~/.claude/CLAUDE.md`, which isn't versioned or shared.

## Reference

Marceltov/claude-marketplace's `rules` plugin (ADR 0008), which this page and the hook replace. The process check is applied in MarcelBruckner-Homelab/homelab's `CLAUDE.md` (2026-11-17).
