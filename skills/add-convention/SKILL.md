---
name: add-convention
description: Add, change or retire one of Marcel Bruckner's engineering conventions in the Marceltov/engineering-conventions repository - a page in the same shape as the others, listed in the menu, the index and the reading skill's table, with a plugin version bump and a pull request. Use when the user says a rule should hold for every repository ("from now on every repo…", "make this a coding convention", "add this to the conventions / guidelines"), when a decision made in one repository is meant for all of them, or when a convention turns out wrong or out of date.
---

# Add a convention

The conventions live in one place: the Markdown pages in `docs/` of [Marceltov/engineering-conventions](https://github.com/Marceltov/engineering-conventions), published as the site and read by the `engineering-conventions` skill. A new standing rule goes there as a pull request, not into a wiki, a memory file or one repository's `CLAUDE.md`.

Its values (`docs/values.md`) are the yardstick here; name the point a change touches.

## Before writing

1. **Is it a standing rule?** It applies to every repository of its kind, and the user decided it (or asked for it). A fix that matters to one repository belongs in that repository's `CLAUDE.md` or an ADR. When unsure, ask.
2. **Does a page already cover it?** Read `docs/index.md` and grep `docs/`. Extend that page instead of adding a second one; when the new rule contradicts it, the page changes and the pull request says why (V5).
3. **Public, so nothing private (V3).** No hostnames, internal URLs, secrets, account details, personal notes or homelab specifics. Rewrite the rule in general terms; leave out what can't be.
4. **Done somewhere (V4).** Name the repository, and if possible the pull request, where it is applied. If nothing applies it yet, apply it first in the repository at hand, or add it to the roadmap as a planned step instead of a page.

## Writing the page

Get the repository: a clone of `https://github.com/Marceltov/engineering-conventions` (or the GitHub tools), on a new branch from `main`. Pick the section by what the rule is about: `architecture/`, `code/`, `repo-setup/` or `stacks/`.

Every page has the shape in `docs/index.md` (_How a page reads_):

```markdown
# <Title, as in the menu>

**<The rule, in one or two sentences.>** Decided <YYYY-MM-DD>.

## Why

<The problem it solves: the incident or the decision, with its date.>

## How

<What to do, concretely enough to follow without asking: settings, commands, a code sample.>

## Rules out

- <What a change must not do; this is the line a review cites.>

## Reference

<The repository (and pull request) where it is done.>
```

- **A diagram** when the rule has a shape (a flow, a sequence, a structure): see `docs/repo-setup/diagrams.md`.
- **Versions only where the pin is the rule (V6).**
- English, short sentences, no filler.

## Wiring it in

1. `mkdocs.yml`: the page in `nav`, under its section, with the same title as its heading.
2. `docs/index.md`: one line under its section, with the rule in a few words.
3. `skills/engineering-conventions/SKILL.md`: a row in the table, or the page added to a row, saying when to read it.
4. `.claude-plugin/plugin.json`: bump `version` (patch for a wording change, minor for a new or changed rule), so installed plugins update (V5).
5. `docs/roadmap.yml`: if the page finishes a planned step, set it `done` with the date and the pull request link.
6. Build: `uvx --with mkdocs-material==9.7.7 --with 'mkdocs<2' mkdocs build --strict`.
7. Open a pull request that says what the rule is, why, and where it is applied. Merging is the maintainer's call.

## Changing or retiring a convention

- **Changing:** edit the page, keep its _Rules out_ honest, and say in the pull request what changed and why. Repositories that now differ get an issue each, when you can reach them.
- **Retiring:** remove the page and its entries in `nav`, the index and the skill table; say why in the pull request. If it was replaced, link the replacement.

## After the pull request

- Repositories that should follow the new rule: offer to open an issue in each, rather than changing them unasked.
- The repository at hand: apply the rule there only if the user asked for it.
