# Releases

**A release is a version tag `vX.Y.Z` on `main`. CI builds and tags the image (`X.Y.Z`, `X.Y`, `latest`) and makes the GitHub release from the pull requests merged since the last tag.**

## Why

A tag is a single, reviewable act: what is released is exactly what is on `main` at that commit, and the release notes come from the pull requests that already describe each change. Nothing is published from a laptop.

## How

- Tag `main`: `git tag -a vX.Y.Z -m "vX.Y.Z" && git push origin vX.Y.Z`.
- The release workflow checks that the tag matches the version in the project (`package.json`, `pyproject.toml`) before it builds.
- The image gets three tags: the exact version, the minor line and `latest`.
- **A Python library goes to PyPI** from the same tag, through [Trusted Publishing](https://docs.pypi.org/trusted-publishers/): the workflow publishes with a short-lived token bound to the repository, the workflow file and an environment named `pypi`, so no API token is stored anywhere. The workflow checks that the tag matches `pyproject.toml`, runs the tests, runs `uv build`, publishes with `pypa/gh-action-pypi-publish` and attaches the same files to the GitHub release.
- The release notes list the merged pull requests; a project may also post them elsewhere (notefeed posts its releases to a feed).
- `CLAUDE.md` names the release command.

## Rules out

- Publishing an image or a package from a local machine.
- A PyPI API token in the repository's secrets.
- A release whose tag doesn't match the version in the project.
- Hand-written release notes that repeat the pull requests.

## Reference

freundebuch and notefeed (image releases); [mcp-login-oauth](https://mcp-login-oauth.marceltov.de/) (PyPI through Trusted Publishing).
