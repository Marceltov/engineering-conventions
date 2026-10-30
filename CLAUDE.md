# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

engineering-conventions: Marcel Bruckner's engineering conventions, published as a documentation site (`docs/`, Material for MkDocs, GitHub Pages) and as a Claude Code plugin (`.claude-plugin/`, `skills/`, `hooks/`) that reads the same pages.

## Commands

- Docs: `uvx --with mkdocs-material==9.7.7 --with 'mkdocs<2' mkdocs serve` (`build --strict` in CI); published to GitHub Pages from `main`.

## Rules

- What engineering-conventions stands for is `docs/values.md`: changes are judged against it, and a review names the point it touches ("this breaks V3").
- The repository is public. Nothing private goes in: no hostnames, internal URLs, secrets, account details, personal notes or homelab specifics (V3).
- Every convention page has the shape in `docs/index.md` (_How a page reads_): the rule, why, how, **Rules out:**, a reference repository.
- A new page goes into `mkdocs.yml`'s `nav`, into `docs/index.md`'s list and into the skill's table in `skills/engineering-conventions/SKILL.md`.
- Bump `version` in `.claude-plugin/plugin.json` with every change to `docs/`, `skills/` or `hooks/`, so installed plugins update.
- Docs and identifiers are English. Never commit superpowers artifacts (`.superpowers/`, specs, plans).
