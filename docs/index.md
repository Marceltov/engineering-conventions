---
hide:
  - toc
---

<div class="ec-hero" markdown>
<img class="ec-hero__mark" src="assets/icon.svg" alt="">

# How Marcel Bruckner builds software

<p class="ec-hero__lead">The standing rules for every repository: how an app is shaped, how code is written, how a repository is set up and which stacks it uses. Each says why it exists and what it rules out, and names a repository where it is done.</p>

[Read the conventions](#the-conventions){ .md-button .md-button--primary }
[Use them in Claude Code](plugin.md){ .md-button }

</div>

They are written for people and for Claude alike: the same pages ship as a [Claude Code plugin](plugin.md), so a session loads the ones that apply before it designs, builds, sets up or reviews code.

!!! note "The repository wins"
    A repository's own `CLAUDE.md`, values page and ADRs override these conventions where they differ. A repository that follows them says so in its `CLAUDE.md`: "Follows Marceltov/engineering-conventions; the rules here win where they differ."

## The conventions

**Architecture**

- [MCP first, one domain layer](architecture/mcp-first.md): MCP, REST and the web pages call the same framework-free domain layer; every tool result carries `next`.
- [One gate for every read](architecture/one-gate-for-every-read.md): privacy, scoping or spoilers are one function every read goes through.
- [Sign-in](architecture/sign-in.md): [Better Auth](stacks/better-auth.md) for apps with a web UI, [mcp-login-oauth](stacks/mcp-login-oauth.md) for form-login MCP servers, backends check tokens.

**Code**

- [Language and internationalization](code/language.md): code, logs and docs in English; every UI built for several languages, one copy module per language.
- [Accessibility](code/accessibility.md): WCAG 2.2 AA, never colour alone, colour-blind safe palettes, keyboard and screen readers, reduced motion.
- [HTTPS clients trust the OS certificate store](code/https-clients.md): `truststore`, not certifi's bundle.
- [Formatting and linting](code/formatting.md): 160 columns everywhere; Prettier, and Ruff for Python, from shared config files; CI checks.

**Repository setup**

- [CLAUDE.md](repo-setup/claude-md.md): commands, architecture and rules for every session.
- [Values and roadmap pages](repo-setup/values-and-roadmap.md): what a project stands for and where it is going.
- [Architecture decisions](repo-setup/adrs.md): MADR files in `docs/adr/`.
- [Documentation site](repo-setup/docs-site.md): Material for MkDocs on GitHub Pages, each site with its own design; short READMEs.
- [Diagrams](repo-setup/diagrams.md): sequences, flows and structures as small Mermaid diagrams, in the site's palette, with a sentence of reading.
- [Dependabot with auto-merge](repo-setup/dependabot.md): small bumps merge once CI is green.
- [Releases](repo-setup/releases.md): a version tag builds the image and the release.
- [Deploying with Docker Compose](repo-setup/deployment.md): the server runs the published image from `compose.yaml` and one `.env` file; nothing is built there.

**Working with Claude**

- [Working rules for Claude sessions](claude/session-rules.md): small tool output, narrow reads and searches, no unasked subagents, short replies; in every session from its start.

**Stacks**

- [Next.js app](stacks/nextjs.md), [SQLite](stacks/sqlite.md), [Better Auth](stacks/better-auth.md), [mcp-login-oauth](stacks/mcp-login-oauth.md), [Python and FastMCP](stacks/python.md).

## How a page reads

Every convention has the same shape, so it can be used in a review:

1. **The rule**, in bold, in one or two sentences.
2. **Why**: the problem it solves, often an incident or a decision with its date.
3. **How**: what to do, concretely enough to follow without asking.
4. **Rules out:** what a change must not do. This is the line a review cites.
5. **Reference**: a repository where it is done right.

What these conventions stand for, and how they change, is on [What engineering-conventions stands for](values.md).
