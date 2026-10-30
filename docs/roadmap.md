---
hide:
  - toc
---

# Where engineering-conventions is going

engineering-conventions started on 2026-10-30, when the standing rules for Marcel's repositories moved out of a private wiki into a public repository, so that every session and every contributor can read them. It is becoming the one place a new repository is set up from, and the plugin every Claude session loads.

This page says what is planned and why, inside the [values](values.md), and what has shipped. Each step links its issue and the value it serves. Planned steps have no dates, only now, next or later; shipped steps carry the day they shipped.

## The idea behind all of it

Write each rule down once, with its reason and its limit, where every person and every session can read it, and let each repository decide where it differs.

<!-- roadmap -->

## Parked

Nothing yet.

## Decided against

- **Homelab and personal conventions here**: how Marcel's own servers, accounts and tools are set up stays in his private wiki, because this repository is public. See [V3](values.md#v3-public-so-nothing-private).

## Keep it true

The timeline is rendered from [`docs/roadmap.yml`](https://github.com/Marceltov/engineering-conventions/blob/main/docs/roadmap.yml); on GitHub, read that file. Finish a step in the pull request that finishes it: set `status: done`, replace `when` with a `date`, add the link to its pull request, and move it to the top of the shipped entries. Change the file in the pull request that changes the plan.
