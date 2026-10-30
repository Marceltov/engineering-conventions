# Documentation site

**Every project has a documentation site: Markdown in `docs/`, built with Material for MkDocs, published to GitHub Pages from `main`, with its own design. The README stays short (what it is, how to install, a link to the site); how to use it lives in `docs/`, once.** Decided 2026-10-30.

## Why

Docs split between a long README and a site drift apart. One place, built with `--strict`, catches broken links before they ship, and the site gives the values page, the roadmap and the ADRs a home that people actually read.

## How

- **`mkdocs.yml`** at the root: `site_name`, `site_description`, `site_url: https://marceltov.github.io/<repo>/`, `repo_url`, `edit_uri: edit/main/docs/`, the license in `copyright`.
- **Theme:** `material`, fonts Atkinson Hyperlegible Next (text) and Atkinson Hyperlegible Mono (code), a light and a dark palette with a toggle, and the features `navigation.instant`, `navigation.footer`, `navigation.top`, `toc.follow`, `search.suggest`, `search.highlight`, `content.code.copy`, `content.action.edit`. Its own colours and icon are required, see _Design_ below.
- **Markdown extensions:** `admonition`, `attr_list`, `md_in_html`, `tables`, `toc` with permalinks, `pymdownx.details`, `highlight`, `inlinehilite`, `superfences` (with a `mermaid` fence where diagrams are used), `tabbed`.
- **Nav, in this order:** Home, What \<project\> stands for, Where \<project\> is going, the user guides, reference, internals or development, and the ADRs under _Design decisions_.
- **Pinned:** `mkdocs-material==9.7.7` with `mkdocs<2`. MkDocs 2.0 drops the plugin and theme system, and Material 9 doesn't work with it.
- **Preview:** `uvx --with mkdocs-material==9.7.7 --with 'mkdocs<2' mkdocs serve`. Add `site/` to `.gitignore`.
- **Publish:** `.github/workflows/pages.yml` builds with `mkdocs build --strict` on every pull request that touches `docs/**` or `mkdocs.yml`, and on `main` deploys with `actions/upload-pages-artifact` and `actions/deploy-pages` (permissions `pages: write`, `id-token: write`). Once per repository: _Settings → Pages → Source: GitHub Actions_.

## Design

**Each project's site has its own identity, drawn from what the project is about, not Material's default indigo.** A reader should know which project they are in from the colour and the icon alone. Designed with the process of Anthropic's [frontend-design skill](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md): ground the design in the subject, plan tokens first, check the plan against generic defaults, then build and check screenshots.

- **A small palette in `docs/stylesheets/extra.css`**, as CSS variables with a project prefix (`--pw-*`, `--ml-*`): an accent for links and the active page, a second colour for hover and focus, an ink for text and a mist for code, tables and the search field, each defined for light and dark. Material's `primary` and `accent` are `custom`.
- **White pages and a hairline header**: the header is the page colour with a 1px line, not a coloured bar. Dark mode has its own hue (`--md-hue`) and backgrounds from the same family, not plain grey.
- **Its own icon** as `docs/assets/icon.svg` (or `docs/logo.svg`), used as `logo` and `favicon`: a simple mark from the subject (passageway's archway, mcp-login-oauth's keyhole, freundebuch's orbit), checked on both the light and the dark header.
- **A home page that opens with what the project does**: a short heading that says it, one paragraph, and one or two buttons to the first step. No feature grid, no stats.
- **Atkinson Hyperlegible** for text and code on every site, a touch larger and looser (`font-size: 0.82rem; line-height: 1.65`).
- **One bold thing per site**, everything else quiet: no gradients, card grids, shadows or animations as decoration.
- **Check it before merging**: build, serve and take screenshots in light mode, dark mode and at phone width.
- **Diagrams** follow [Diagrams](diagrams.md).

??? example "`.github/workflows/pages.yml`"

    ```yaml
    name: Publish docs

    on:
      push:
        branches: [main]
        paths: ["docs/**", mkdocs.yml, .github/workflows/pages.yml]
      pull_request:
        paths: ["docs/**", mkdocs.yml, .github/workflows/pages.yml]
      workflow_dispatch:

    permissions:
      contents: read
      pages: write
      id-token: write

    concurrency:
      group: pages-${{ github.ref }}
      cancel-in-progress: true

    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - uses: astral-sh/setup-uv@v6
          # mkdocs<2: Material 9 isn't compatible with MkDocs 2.0.
          - run: uvx --with mkdocs-material==9.7.7 --with 'mkdocs<2' mkdocs build --strict
          - uses: actions/upload-pages-artifact@v3
            with:
              path: site

      deploy:
        if: github.event_name != 'pull_request'
        needs: build
        runs-on: ubuntu-latest
        environment:
          name: github-pages
          url: ${{ steps.deployment.outputs.page_url }}
        steps:
          - id: deployment
            uses: actions/deploy-pages@v4
    ```

Claude cloud sessions can't push workflow files (their GitHub connection lacks the `workflow` scope), so a session puts the workflow in the pull request description and a person adds it.

## Rules out

- Usage docs in the README as well as on the site.
- A docs build without `--strict`.
- Unpinned MkDocs or Material.
- Material's default palette and icon, or one project's palette copied to another.
- Decoration that carries no information: gradients, card grids, shadows, entrance animations.
- Merging a design change without screenshots in light and dark mode.

## Reference

passageway (palette, archway logo, hero, header links for agents); freundebuch (its own colours and orbit icon); mcp-login-oauth (brass keyhole); this repository.
