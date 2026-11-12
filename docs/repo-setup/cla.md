# Contributor licence agreement

**A public product repository whose licence the maintainer may change, or which is also sold or run under other terms, merges an outside pull request only after its author has accepted a contributor licence agreement: the Apache Individual CLA, with the maintainer as the party, accepted by a comment on the pull request and enforced by a workflow.** Decided 2026-11-03.

## Why

As long as one person wrote every line, they can relicense the code or sell it under other terms at will. The first outside contribution under a plain open-source licence ends that: from then on every contributor holds the copyright to their part, and changing the licence needs each of them. passageway is licensed for noncommercial use and sold to companies separately, so it needs to be able to license every line (passageway #97, 2026-11-03). notefeed and Gamepanion are AGPL-3.0 with hosted instances that sell; taking the agreement before the first outside contribution keeps the option to change their licence later and costs nothing now.

A Developer Certificate of Origin (`Signed-off-by`) is not enough: it says the contributor may submit the code, not that the maintainer may relicense it.

## How

- **`CLA.md`** at the root: the Apache Software Foundation's Individual Contributor License Agreement V2.2, with "the Foundation" replaced by "the Maintainer" (named, with what they own), the nonprofit clause removed, and a paragraph on how to accept. A short preamble says why the project needs it and that contributors keep every right to use their own work.
- **`CONTRIBUTING.md`** says it in one sentence: a pull request from outside is merged only after its author accepts the agreement, with a link.
- **Accepting is a comment** on the first pull request: `I have read the CLA and I agree to it.` That comment, under the author's GitHub account, is the signature; nothing else is collected. Once covers every later contribution.
- **`.github/workflows/cla.yml`** runs [contributor-assistant/github-action](https://github.com/contributor-assistant/github-action) on `pull_request_target` and `issue_comment`. It records signatures in `signatures.json` on a branch of its own (`cla-signatures`), since branch protection keeps it from writing to `main`, and allowlists the maintainer, Claude (the co-author on commits made with it) and Dependabot:

  ```yaml
  on:
    issue_comment:
      types: [created]
    pull_request_target:
      types: [opened, closed, synchronize]
  permissions:
    actions: write
    contents: write
    pull-requests: write
    statuses: write
  jobs:
    cla:
      if: github.event_name == 'pull_request_target' || github.event.issue.pull_request
      runs-on: ubuntu-latest
      steps:
        - uses: contributor-assistant/github-action@v2.6.1
          env:
            GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          with:
            path-to-document: https://github.com/<owner>/<repo>/blob/main/CLA.md
            path-to-signatures: signatures.json
            branch: cla-signatures
            allowlist: <maintainer>,claude,dependabot[bot]
            custom-pr-sign-comment: I have read the CLA and I agree to it.
  ```

  Its status check is required on `main`, so an unsigned pull request can't be merged.

- **The `cla-signatures` branch holds only `signatures.json`** and is created with the workflow, before any pull request runs it: the action does not create the branch, and the first check fails without it. It is an orphan branch, not a copy of `main`, so nothing on it can go stale; it is never merged. The signatures stay in the project's own repository, so they move with it (another organization, a new maintainer), and the workflow's own token can write them. Create it once:

  ```sh
  R=repos/<owner>/<repo>
  blob=$(gh api $R/git/blobs -f content=$'{\n   "signedContributors": []\n}' -f encoding=utf-8 --jq .sha)
  tree=$(gh api $R/git/trees -f "tree[][path]=signatures.json" -f "tree[][mode]=100644" \
    -f "tree[][type]=blob" -f "tree[][sha]=$blob" --jq .sha)
  commit=$(gh api $R/git/commits -f message="CLA signatures" -f tree=$tree --jq .sha)
  gh api $R/git/refs -f ref=refs/heads/cla-signatures -f sha=$commit
  ```

- **Libraries under MIT or a similar permissive licence need none:** anyone, the maintainer included, may already use them under any terms. A repository with permissive parts beside the product (an SDK, protocols) says in `CONTRIBUTING.md` that those parts, or a plugin in one's own repository, need no agreement.

## Rules out

- Merging an outside pull request into such a repository before its author accepted the agreement.
- A DCO or a licence header in place of the agreement.
- Collecting anything beyond the comment: names, addresses or signatures on paper.
- An agreement written from scratch where the Apache one fits.
- A `cla-signatures` branch made from `main`, or the signatures kept anywhere but the project's own repository (a shared repository needs a personal access token in every organization and ties one project's records to the others).

## Reference

passageway: `CLA.md`, `CONTRIBUTING.md` and `.github/workflows/cla.yml` (passageway #97). notefeed and Gamepanion follow (Marceltov/engineering-conventions#21). notefeed's `cla-signatures` branch is the first that holds only `signatures.json` (2026-11-12, found when notefeed#351 was the first pull request its check ran on).
