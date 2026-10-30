# Architecture decisions

**Every architectural decision is a Markdown file in `docs/adr/NNNN-<title>.md`, in the MADR format: the problem, the options, the choice and its consequences, good and bad.**

## Why

The reason behind a structure is what gets lost first. An ADR keeps it next to the code, so that a later change can see what it would undo, and a values point can link to the decision behind it.

## How

```markdown
---
status: proposed | accepted | superseded by [ADR NNNN](NNNN-….md)
date: YYYY-MM-DD
decision-makers: <who>
---

# <The decision, as a statement>

## Context and Problem Statement
## Decision Drivers
## Considered Options
## Decision Outcome
### Consequences
* Good, because …
* Bad, because …
```

- **The title states the decision** ("Sign-in with Better Auth, in its own SQLite file"), not the topic ("Authentication").
- **Numbered in order, never renumbered.** A changed decision gets a new ADR that supersedes the old one; the old one's status says so.
- **Write it before the code**, as a pull request of its own when the decision is open, and mark it accepted when it is decided.
- **Bad consequences are listed honestly**; they are what a later reader needs most.
- ADRs are part of the docs site, under _Design decisions_ in the nav.

## Rules out

- Decisions recorded only in a pull request, an issue or a chat.
- Editing an accepted ADR's decision instead of superseding it.
- An ADR without bad consequences.

## Reference

freundebuch's `docs/adr/` (17 decisions); mcp-login-oauth's ADR 0004 and questlog's ADR 0004, which supersedes its 0003.
