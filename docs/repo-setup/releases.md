# Releases

**A release is a version tag `vX.Y.Z` on `main`. CI builds and tags the image (`X.Y.Z`, `X.Y`, `latest`) and makes the GitHub release from the pull requests merged since the last tag.** The GitHub release is the only place its notes live: they are not mirrored anywhere, and a page that shows releases reads them from GitHub. Decided 2026-11-13.

## Why

A tag is a single, reviewable act: what is released is exactly what is on `main` at that commit, and the release notes come from the pull requests that already describe each change. Nothing is published from a laptop.

Release notes live in one place. Every repository already has a feed of its releases that needs no GitHub account (`https://github.com/<owner>/<repo>/releases.atom`). On 2026-11-13 the rule was briefly that every tool mirrors its releases to its own notefeed feed, as notefeed, passageway, freundebuch and the Trilium projects did. Rolling it out showed the cost: a feed, a license and two secrets per tool for a second copy of notes that are public on GitHub anyway. It was dropped the same day. The website reads the releases from GitHub instead.

## How

- Tag `main` with a headline: `git tag -a vX.Y.Z -m "A GitHub connector" && git push origin vX.Y.Z`.
- **Every release starts with a one-line headline**: what the release brings, in a few words, for the people who use it ("A GitHub connector", "Share from an iPhone"). It is the tag message's first line and the first line of the release notes; pages that list releases show it. Not the version, not "Release X.Y.Z", not an image name or a merge commit.
- The release workflow checks that the tag matches the version in the project (`package.json`, `pyproject.toml`) before it builds.
- The image gets three tags: the exact version, the minor line and `latest`.
- **A Python library goes to PyPI** from the same tag, through [Trusted Publishing](https://docs.pypi.org/trusted-publishers/): the workflow publishes with a short-lived token bound to the repository, the workflow file and an environment named `pypi`, so no API token is stored anywhere. The workflow checks that the tag matches `pyproject.toml`, runs the tests, runs `uv build`, publishes with `pypa/gh-action-pypi-publish` and attaches the same files to the GitHub release.
- The release carries an SBOM (CycloneDX, the dependencies and the image) and the image an SBOM and a build provenance: [Security setup](security.md).
- The release notes list the merged pull requests.
- `CLAUDE.md` names the release command.

### Showing releases elsewhere

- **A page that lists releases reads them from GitHub at build time** (`GET /repos/<owner>/<repo>/releases`, with the workflow's `GITHUB_TOKEN`), shows the version, the headline, the date and a link to the release, and builds on a schedule so a new release appears within a day. marcelbruckner.de's Projekte page is the first (MarcelBruckner-Business/marcelbruckner#36).
- **Readers who want to follow a tool** get its `releases.atom` link.
- **notefeed is the exception, as its own product:** it posts its releases and a news post to notefeed.me's reserved feeds to use what it sells. That is notefeed's decision, not a rule for other tools.

## Rules out

- Publishing an image or a package from a local machine.
- A PyPI API token in the repository's secrets.
- A release whose tag doesn't match the version in the project.
- Hand-written release notes that repeat the pull requests.
- A release without a headline, or whose first line is the version, an image name or a merge commit.
- Copying release notes to another place (a feed, a blog post, a changelog file) instead of linking to or reading the GitHub release.

## Reference

freundebuch and notefeed (image releases); [mcp-login-oauth](https://mcp-login-oauth.marceltov.de/) (PyPI through Trusted Publishing).

notefeed's own feeds: `.github/workflows/ci.yml` and `scripts/release-news.sh` in notefeed/notefeed.
