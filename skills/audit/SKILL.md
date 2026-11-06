---
name: audit
description: Audit a repository against every one of Marcel Bruckner's engineering conventions - one row per convention page (follows, partly, not, doesn't apply) with the evidence and what would close each gap, then one issue per gap the user wants fixed. Use when the user asks to audit, check or review a repository against the conventions ("does this repo follow the conventions?", "conventions audit", "what's missing here?"), or when an issue asks for such an audit.
---

# Audit a repository against the conventions

The conventions are the pages in this plugin's `docs/` folder (two levels up from this skill), listed in `docs/index.md`. An audit checks the repository at hand against every page and writes down, for each, whether the repository follows it. It changes nothing in the repository.

## 1. Set up

- **The repository:** the working directory, unless the user names another one. Note its kind: an app with a web UI, an MCP server, a library, a docs site, an infrastructure repository. The kind decides which pages apply.
- **The repository wins:** read its `CLAUDE.md`, its `docs/values.md` (if any) and its ADRs first. A difference they decide on purpose counts as _doesn't apply_, with the ADR or line as the reason, not as a gap.
- **The pages:** take the list from `docs/index.md`, every section. Skip the pages about Claude itself (`claude/`) unless the user asks for them.

## 2. Check each page

For every page, read its rule (the bold first paragraph) and its **Rules out** lines. Each line is a check: find evidence that the repository does or does not do what it rules out.

Look first for things you can confirm in seconds. Only read code where a page is about how the code is shaped.

| Evidence            | Where to look                                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------------------------- |
| a file exists       | `CLAUDE.md`, `SECURITY.md`, `.github/dependabot.yml`, `compose.yaml`, `.env.example`, `docs/adr/`, `mkdocs.yml` |
| a tool is set up    | `package.json` scripts, `pyproject.toml`, `ruff.toml`, `.prettierrc`, `.editorconfig`                           |
| CI enforces it      | `.github/workflows/*.yml`: formatting and lint checks, release on a tag, a scheduled audit, image build         |
| the code follows it | a targeted `grep` (`fetch(`, `new Database(`, route handlers, tool registrations), then a read of what it finds |
| the remote has it   | `gh api repos/<owner>/<name>` for settings (private reporting, secret scanning), `gh release list`              |

Keep output small: `grep -l`, `ls`, `head`. Don't read the whole codebase. Where a check can't be settled without running the app or asking the user, mark it _unclear_ and say what would settle it.

For each page, give one of:

- **follows**: every Rules out line holds.
- **partly**: some do; name the ones that don't.
- **not**: the rule isn't followed at all.
- **doesn't apply**: the page's reason doesn't hold for this repository (a docs-only repository has no sign-in), or its own rules decide otherwise. Always give the reason.

## 3. Report

One table, one row per page, in the order of `docs/index.md`:

```markdown
| Convention                                                                  | Result | Evidence                                               | To close the gap                                         |
| --------------------------------------------------------------------------- | ------ | ------------------------------------------------------ | -------------------------------------------------------- |
| [Formatting](https://engineering-conventions.marceltov.de/code/formatting/) | partly | Prettier configured; 58 files unformatted, no CI check | `npx prettier@3 --write .`, add `prettier --check` to CI |
```

- Link each page to the site (`https://engineering-conventions.marceltov.de/<section>/<page>/`), so the report works without the plugin.
- Evidence is a file and line, a command and its output in a few words, or a missing file. Not a guess.
- Under the table: the plugin version the audit used (`.claude-plugin/plugin.json`) and the date, so a later audit can be compared.

Where the audit was asked for in an issue, post the report there as a comment (`gh issue comment`). Otherwise give it in the reply.

## 4. Issues for the gaps

Ask the user which gaps to fix, then open one issue per gap in the audited repository (or one issue for several small ones that are fixed together). Each issue names the convention page, quotes the Rules out line it breaks, and says what would close it. Never change the repository or open a pull request as part of the audit.

## When a convention looks wrong

If a page's rule doesn't fit a repository for a reason the page doesn't cover, it isn't a gap in the repository. Say so in the report, and offer to change the convention with the `add-convention` skill.
