# Documentation site

**Every project has a documentation site: Markdown in `docs/`, built with Material for MkDocs, published to GitHub Pages from `main`. The README stays short (what it is, how to install, a link to the site); how to use it lives in `docs/`, once.** Decided 2026-10-30.

## Why

Docs split between a long README and a site drift apart. One place, built with `--strict`, catches broken links before they ship, and the site gives the values page, the roadmap and the ADRs a home that people actually read.

## How

- **`mkdocs.yml`** at the root: `site_name`, `site_description`, `site_url: https://marceltov.github.io/<repo>/`, `repo_url`, `edit_uri: edit/main/docs/`, the license in `copyright`.
- **Theme:** `material`, fonts Atkinson Hyperlegible Next (text) and Atkinson Hyperlegible Mono (code), a light and a dark palette with a toggle, and the features `navigation.instant`, `navigation.footer`, `navigation.top`, `toc.follow`, `search.suggest`, `search.highlight`, `content.code.copy`, `content.action.edit`. A project may add its own colours in `docs/stylesheets/extra.css`.
- **Markdown extensions:** `admonition`, `attr_list`, `md_in_html`, `tables`, `toc` with permalinks, `pymdownx.details`, `highlight`, `inlinehilite`, `superfences` (with a `mermaid` fence where diagrams are used), `tabbed`.
- **Nav, in this order:** Home, What \<project\> stands for, Where \<project\> is going, the user guides, reference, internals or development, and the ADRs under _Design decisions_.
- **Pinned:** `mkdocs-material==9.7.7` with `mkdocs<2`. MkDocs 2.0 drops the plugin and theme system, and Material 9 doesn't work with it.
- **Preview:** `uvx --with mkdocs-material==9.7.7 --with 'mkdocs<2' mkdocs serve`. Add `site/` to `.gitignore`.
- **Publish:** `.github/workflows/pages.yml` builds with `mkdocs build --strict` on every pull request that touches `docs/**` or `mkdocs.yml`, and on `main` deploys with `actions/upload-pages-artifact` and `actions/deploy-pages` (permissions `pages: write`, `id-token: write`). Once per repository: _Settings → Pages → Source: GitHub Actions_.

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

## Reference

freundebuch (the reference setup, with its own colours); mcp-login-oauth; this repository.
