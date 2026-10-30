---
name: engineering-conventions
description: Marcel Bruckner's engineering conventions - architecture (MCP first, one domain layer, one gate for every read, sign-in), code (language, HTTPS clients, formatting and linting with Prettier and Ruff), working with Claude (the working rules every session gets), repository setup (CLAUDE.md, values and roadmap pages, ADRs, docs site, Dependabot, releases) and stacks (Next.js, SQLite, Better Auth, mcp-login-oauth, Python and FastMCP). Use before designing, building, setting up, reviewing or choosing a stack for code in one of his repositories, when starting a new repository, and when a review should name the convention a change touches.
---

# Engineering conventions

The conventions are Markdown pages in this plugin's `docs/` folder (`${CLAUDE_PLUGIN_ROOT}/docs/`), the same pages as the site at https://engineering-conventions.marceltov.de/. Read the pages; this file only says which ones and how to apply them.

## Which pages to read

| When you are about to …                                                                                            | Read                                                                                   |
| ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| start a new repository, or a repository lacks the basics                                                           | every page under `repo-setup/`, then the stack pages it uses                           |
| design a feature, a surface or a data flow                                                                         | `architecture/mcp-first.md`, `architecture/one-gate-for-every-read.md`                 |
| add or change sign-in, tokens, API keys or a backend that checks them                                              | `architecture/sign-in.md`, then `stacks/better-auth.md` or `stacks/mcp-login-oauth.md` |
| write code that calls something over HTTPS                                                                         | `code/https-clients.md`                                                                |
| write, format or lint code, or set up a formatter, linter or CI checks                                             | `code/formatting.md`                                                                   |
| write UI text, logs, identifiers or docs                                                                           | `code/language.md`                                                                     |
| work in a Next.js app                                                                                              | `stacks/nextjs.md`, `stacks/sqlite.md`                                                 |
| work in Python                                                                                                     | `stacks/python.md`                                                                     |
| record a decision                                                                                                  | `repo-setup/adrs.md`                                                                   |
| change CLAUDE.md, or the working rules every session gets                                                          | `repo-setup/claude-md.md`, `claude/session-rules.md`                                   |
| change docs, values or roadmap, or the docs site's design                                                          | `repo-setup/docs-site.md`, `repo-setup/values-and-roadmap.md`                          |
| explain an architecture, a sequence of calls, a flow or a decision with branches, or theme diagrams on a docs site | `repo-setup/diagrams.md`                                                               |
| touch dependencies or releases                                                                                     | `repo-setup/dependabot.md`, `repo-setup/releases.md`                                   |

`docs/index.md` lists every page. When none fits, read the index and pick by title.

## How to apply them

1. **The repository wins.** Its `CLAUDE.md`, its `docs/values.md` and its ADRs override these conventions where they differ. Follow them, and mention the difference once if it looks unintended.
2. **Each convention has a reason and a "Rules out" line.** Use the line to decide: if a change does something it rules out, change the plan or ask the user. Don't apply a convention where its reason doesn't hold; say why.
3. **Name the page in a review** ("conventions: one gate for every read"), as the repository's values are named ("this breaks V2").
4. **Don't apply silently what the user hasn't asked for.** A missing values page or Dependabot setup is worth one line to the user, not an unrequested pull request.
5. **When a convention is wrong or missing**, change it in Marceltov/engineering-conventions instead of working around it in one repository: the `add-convention` skill says how. A rule the user decides for every repository goes there too, not into a wiki or a single `CLAUDE.md`.
