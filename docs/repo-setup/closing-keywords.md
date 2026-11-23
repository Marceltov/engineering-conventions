# Closing keywords stay in their repository

**A closing keyword (`close`, `fix`, `resolve` and their forms) in a pull request description or a commit message points only at an issue of the same repository. Work in another repository is listed under a heading that is not a keyword, such as "Upstream:" or "Sent upstream:".** Decided 2026-11-22.

## Why

GitHub closes the issue or pull request named after a closing keyword when the pull request carrying it is merged into the default branch, or when a commit carrying it is pushed there. This works across repositories, wherever the person merging may close the target. On 2026-11-22 a description listed our upstream contributions as "Upstream fixes: owner/repo#2, …". The heading read as a command: merging it closed our open pull request in someone else's repository, and it stayed closed for an hour and a half until someone noticed by chance. The maintainer gets a "closed" notification that reads as if the work were done or withdrawn.

GitHub's own list of what a pull request will close (`closingIssuesReferences`, the sidebar's linked issues) leaves out targets in other repositories, so reading it before a merge does not catch this.

## How

- **Same repository:** `Closes #123` as before.
- **Another repository:** name it without a keyword in front:

  ```markdown
  Sent upstream: owner/repo#2 (depot positions dropped), owner/repo#3 (product ID as a secret).
  Refs owner/repo#4.
  ```

- The keywords are `close`, `closes`, `closed`, `fix`, `fixes`, `fixed`, `resolve`, `resolves`, `resolved`, in any case and with or without a colon.
- Commit messages follow the same rule: a keyword there closes on push to the default branch, with no pull request to review.
- If it happened anyway: reopen the target at once and say on it, in one line, that the closing was a mistake.

## Rules out

- A closing keyword followed by `owner/repo#n` or a link to another repository's issue or pull request, in a pull request description or a commit message.
- Headings such as "Fixes upstream:" or "Upstream fixes:" in front of references.

## Reference

Applied in the pull request descriptions of a private repository since 2026-11-22, after the incident above; a check that refuses such a description is planned there.
