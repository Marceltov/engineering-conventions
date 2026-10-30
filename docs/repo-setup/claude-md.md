# CLAUDE.md

**Every repository has a `CLAUDE.md` at its root: what the project is in one line, the commands, the architecture in a few bullets, and the rules a session must follow without being told again.**

## Why

Every session, local or in the cloud, starts by reading it. What isn't there gets rediscovered, guessed or broken: the test command, the boundary between frontend and backend, the one function every read goes through, which files must change together.

## How

```markdown
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

<project>: <what it is, in one line>.

## Commands
- the dev, build, typecheck, format, lint and test commands; how to run one test
- code generation and what CI checks about it
- docs preview and release

## Architecture
- the surfaces and the layer they share; where the boundaries are and what enforces them
- the one function a rule lives in (privacy, spoilers)
- where migrations live

## Rules
- What <project> stands for is `docs/values.md`: changes are judged against it, and a review names the point it touches.
- Follows Marceltov/engineering-conventions; the rules here win where they differ.
- Files that must change together (config, `.env.example`, `compose.yaml`, the configuration docs).
- Language of code and UI.
- Architectural decisions go to `docs/adr/NNNN-*.md` (MADR).
```

- **Short and specific.** A rule names the file or function it concerns. General advice that any project would have belongs here, in the conventions, not in each `CLAUDE.md`.
- **Exceptions are named**: a repository with Dependabot auto-merge says that this is the one case where a merge happens without the user saying so.
- **Environment variables** are prefixed with the app's name (`FREUNDEBUCH_*`), except the shared ones (`PUBLIC_URL`, `DATA_DIR`, `PORT`, `TZ`); `CLAUDE.md` lists the files that must stay in step with them.
- Generated blocks that tools write into agent files (Next.js's `nextjs-agent-rules` in `AGENTS.md`) are not committed.

## Rules out

- A repository without `CLAUDE.md`.
- A `CLAUDE.md` that repeats the README or general advice instead of this project's commands and rules.
- Rules that live only in a chat or a pull request comment.

## Reference

freundebuch's `CLAUDE.md`.
