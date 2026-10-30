# Where engineering-conventions is going

engineering-conventions started on 2026-10-30, when the standing rules for Marcel's repositories moved out of a private wiki into a public repository, so that every session and every contributor can read them. It is becoming the one place a new repository is set up from, and the plugin every Claude session loads.

This page says what is planned and why, inside the [values](values.md). Each item links to its issue and the value it serves. There are no dates. An item leaves the page when it ships (the release notes have it) or is dropped (the reason is in its issue).

## The idea behind all of it

Write each rule down once, with its reason and its limit, where every person and every session can read it, and let each repository decide where it differs.

## Now

- **Every repository points at the conventions** ([#1](https://github.com/Marceltov/engineering-conventions/issues/1)): one line in each `CLAUDE.md`, so a session without the plugin still finds them. Serves [V2](values.md#v2-the-repository-wins).

## Next

- **Code style** ([#2](https://github.com/Marceltov/engineering-conventions/issues/2)): functions, naming, comments and tests, each confirmed by Marcel before it lands. Serves [V1](values.md#v1-every-rule-has-a-reason-and-a-limit).

## Later

- **Conventions from single repositories** ([#3](https://github.com/Marceltov/engineering-conventions/issues/3)): branch and commit naming, CI as the gate and others that live in one project's `CLAUDE.md` today. Serves [V4](values.md#v4-each-rule-is-done-somewhere).

## Parked

Nothing yet.

## Decided against

- **Homelab and personal conventions here**: how Marcel's own servers, accounts and tools are set up stays in his private wiki, because this repository is public. See [V3](values.md#v3-public-so-nothing-private).
