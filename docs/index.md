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
- [One data layer, the tenant in one place](architecture/data-layer.md): only the data layer talks to the database; a scope from the session applies the tenant, never each query.
- [Sign-in](architecture/sign-in.md): [Better Auth](stacks/better-auth.md) for apps with a web UI, [mcp-login-oauth](stacks/mcp-login-oauth.md) for form-login MCP servers, backends check tokens; an email allowlist decides who signs in; API tokens from the start, REST only.
- [Selling a hosted instance](architecture/payments.md): payments only with a configured provider, behind one interface with a fake beside it; webhooks become own events; access checked locally against `validUntil`; prices in the provider.

**Code**

- [Language and internationalization](code/language.md): code, logs and docs in English; every UI built for several languages, one copy module per language.
- [Accessibility](code/accessibility.md): WCAG 2.2 AA, never colour alone, colour-blind safe palettes, keyboard and screen readers, reduced motion.
- [Icons](code/icons.md): lucide through one icons module, always next to a word; Material's icons on docs sites; the project's mark drawn for it.
- [HTTPS clients trust the OS certificate store](code/https-clients.md): `truststore`, not certifi's bundle.
- [Formatting and linting](code/formatting.md): 160 columns everywhere; Prettier, and Ruff for Python, from shared config files; CI checks.
- [Shared code lives once](code/shared-code-lives-once.md): code needed in a second package moves into the shared package and both use it; never copied, never an underscore name imported across packages.
- [Tests keep their data in temporary directories](code/tests-temp-dirs.md): the test setup points the data directory at a temporary one for every test; nothing writes the app's real data directory.

**Repository setup**

- [CLAUDE.md](repo-setup/claude-md.md): commands, architecture and rules for every session.
- [Values and roadmap pages](repo-setup/values-and-roadmap.md): what a project stands for and where it is going.
- [Where a repository lives](repo-setup/where-a-repo-lives.md): a named product has its own org and image namespace; new projects start under the personal account.
- [Architecture decisions](repo-setup/adrs.md): MADR files in `docs/adr/`.
- [Documentation site](repo-setup/docs-site.md): Material for MkDocs on GitHub Pages, each site with its own design; short READMEs.
- [Docs live with the code](repo-setup/docs-live-with-the-code.md): setup, deployment and pitfalls in the repository, changed in the same pull request; a wiki keeps concepts and pointers.
- [Diagrams](repo-setup/diagrams.md): sequences, flows and structures as small Mermaid diagrams, in the site's palette, with a sentence of reading.
- [Charts](repo-setup/charts.md): numbers drawn as charts from the data the page holds, with the table kept as the table view.
- [Dependabot with auto-merge](repo-setup/dependabot.md): small bumps merge once CI is green.
- [Releases](repo-setup/releases.md): a version tag builds the image and the release.
- [Security setup](repo-setup/security.md): private reports, secret and code scanning, a daily audit, and an SBOM and provenance on every release; `SECURITY.md` says it.
- [Contributor licence agreement](repo-setup/cla.md): every non-permissive product repository takes the Apache ICLA by pull request comment, enforced by a workflow; permissive libraries need none.
- [Deploying with Docker Compose](repo-setup/deployment.md): the server runs the published image from `compose.yaml` and one `.env` file; nothing is built there.
- [Mail on a product's domain](repo-setup/mail.md): one catch-all mailbox people read, role addresses as aliases; the app sends from its own `noreply@` mailbox; SPF, DKIM, DMARC.
- [Operator pages](repo-setup/operator-pages.md): imprint, privacy, terms and pricing words as the operator's Markdown files named by settings; public texts in `stacks`, contracts in `legal`, the operator guide on the internal docs site.
- [Every secret in the password manager](repo-setup/secrets.md): every `.env` value, password and key of every machine in 1Password; losing one machine loses no access.
- [Resource usage and capacity dashboards](repo-setup/resource-monitoring.md): host and per-container usage with stall, a credential per writer, dashboards that pick hosts and products, every panel checked per value.
- [Alerts that reach a person](repo-setup/alerting.md): every rule fired once on its real path, thresholds from a measured baseline, messages that fit the channel.

**Working with Claude**

- [Working rules for Claude sessions](claude/session-rules.md): small tool output, narrow reads and searches, no unasked subagents, short replies; in every session from its start.
- [Publishing a plugin to the marketplace](claude/marketplace.md): pinned by commit, shipped by bumping `version`, and the plugin starts the marketplace's pin itself.

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
