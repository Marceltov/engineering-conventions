# Values and roadmap pages

**Every project has two pages in its docs: a values page, what it stands for, and a roadmap page, what is planned.** The values page is the yardstick every change is judged against; the roadmap says where the project is going, inside those values. Decided 2026-10-29.

## Why

Without written values, every review argues from taste, and a project drifts toward whatever was easiest to build. A values point that says what it rules out settles a review in one line ("this breaks V2"). The roadmap keeps plans next to the reasons for them, each one tied to the value it serves.

## The values page

Title "What \<project\> stands for", right after Home in the docs nav (`docs/values.md`).

- **Intro (two paragraphs):** what the project is and that this page says what it will stay, whoever runs it and whatever it grows into; then who it is for (someone deciding whether to trust it) and that it is the yardstick: a contribution, from a person or an AI, is judged against these points, and a review names the one it touches.
- **Three groups**, points numbered across them (V1, V2, …):
    - **Lines never crossed**: two or three points. "When a feature would be easier, or would sell better, by bending one of them, the feature changes or is not built."
    - **What you can rely on**: why someone can trust it (what is kept, how they leave, where it runs, how it is paid for).
    - **Principles that follow**: the design rules that come out of the above.
- **Each point:** a heading `Vn. Title`, prose (the statement, then what it means in practice), a bold **Rules out:** line listing concretely what it excludes, and an **ADRs:** line linking the decisions behind it. No examples sections, no "we will / we won't" lists.
- **Closing section "Changing this page":** points keep their numbers so reviews and issues citing them stay right; a change needs the maintainer's approval and says why in its pull request; weakening a line never crossed is a change to what the project is.
- **`CLAUDE.md`** gets one rule: changes are judged against `docs/values.md`, and a review names the point it touches.
- Write points so they leave room for what is planned.

## The roadmap page

Title "Where \<project\> is going", right after the values page (`docs/roadmap.md`). Written by hand.

- **Intro:** where the project comes from and what it is becoming, in two or three sentences; then that the page says what is planned and why, inside the values, each item linked to its issue and the value it serves, **no dates**, and that an item leaves the page when it ships (the release notes have it) or is dropped (the reason in its issue).
- **The idea behind all of it:** one paragraph, the thread every item follows.
- **Sections, in this order:** **Now**, **Next**, **Later**, **Parked** (considered and wanted, but not needed yet), **Decided against** (with the reason, often a value it would break).
- **Each item:** a bold name, its issue link, one sentence of what and why, and the value point it serves (`[V3](values.md#v3-…)`). Every item has an issue; create one when it doesn't.
- Check that every link to a value point matches the anchor MkDocs generates for that heading.

## Rules out

- A project without a values page, or a values point without a **Rules out:** line.
- Renumbering values points.
- Roadmap items without an issue, or with dates.

## Reference

notefeed's values page ([docs.notefeed.me/values](https://docs.notefeed.me/values/)); freundebuch's values and roadmap pages; mcp-login-oauth's values and roadmap.
