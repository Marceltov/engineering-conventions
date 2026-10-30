---
hide:
  - toc
---

# Where engineering-conventions is going

engineering-conventions started on 2026-10-30, when the standing rules for Marcel's repositories moved out of a private wiki into a public repository (the wiki's pages were retired the same day), so that every session and every contributor can read them. It is becoming the one place a new repository is set up from, and the plugin every Claude session loads.

This page says what is planned and why, inside the [values](values.md), and what has shipped. Each step links its issue and the value it serves. Planned steps have no dates, only now, next or later; shipped steps carry the day they shipped.

## The idea behind all of it

Write each rule down once, with its reason and its limit, where every person and every session can read it, and let each repository decide where it differs.

<!-- roadmap -->

## Parked

- **One package for the roadmap timeline**: the hook and its CSS are copied into each repository today ([Values and roadmap pages](repo-setup/values-and-roadmap.md)). A shared MkDocs plugin would keep them in step, once more than a handful of sites use them.
- **A generated ADR menu**: the _Decisions_ section of a docs site is kept by hand ([Documentation site](repo-setup/docs-site.md)); a plugin could build it from `docs/adr/`.

## Decided against

- **Homelab and personal conventions here**: how Marcel's own servers, accounts and tools are set up stays in his private wiki, because this repository is public. See [V3](values.md#v3-public-so-nothing-private).

## Keep it true

The timeline is rendered from [`docs/roadmap.yml`](https://github.com/Marceltov/engineering-conventions/blob/main/docs/roadmap.yml); on GitHub, read that file. Finish a step in the pull request that finishes it: set `status: done`, replace `when` with a `date`, add the link to its pull request, and move it to the top of the shipped entries. Change the file in the pull request that changes the plan.
