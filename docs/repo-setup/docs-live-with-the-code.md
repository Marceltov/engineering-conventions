# Docs live with the code

**How a repository's code, servers and stacks are set up, deployed and run, and what went wrong with them, is written in that repository (`README.md`, `docs/`) and changed in the same pull request as what it describes. A wiki keeps concepts, lessons that span repositories and a short page pointing to the repositories; it does not hold setup details.** Decided 2026-11-01.

## Why

The servers of the business were documented on wiki pages next to their repositories. On 2026-11-01 both servers were renamed and their deploy repositories merged; every wiki page about them was wrong the same day, because nothing ties a wiki page to the change that makes it wrong. Docs in the repository are in the diff: a review sees the code and its docs together, and git keeps when and why each line changed.

## How

- **In the repository:** what runs where and how the parts work together (a diagram in the README), how to deploy, how to set up something new, the settings and secrets it needs (their names, never their values), backups and restore, and a `docs/pitfalls.md` with each trap that cost time once and the code that now guards against it. Why it is built that way goes into [ADRs](adrs.md) or a decisions page.
- **In the wiki:** concepts (what a KMS is, how forward auth works), lessons that are true beyond one repository (a provider blocking a port, a library's quirk), and one page per area that says which repository holds what. Write it as a map, not a copy: "backups: `docs/backups.md` in the deploy repository", not the steps.
- **When moving pages out of a wiki:** compare with what the repository already says, add only what is missing, drop what is outdated, then cut the wiki page down to its concepts and the pointers. Keep the page itself, so links and searches still find it.
- **A pull request that changes how something is run updates its docs in the same pull request.** A reviewer asks for it like a missing test.

## Rules out

- Setup steps, commands, versions, host names or settings on a wiki page that a repository change can make wrong.
- The same instructions in two places; one of them is the copy that goes stale.
- A pull request that changes deployment, a stack or a server's setup without touching the docs that describe it.

## Reference

MarcelBruckner-Business/ansible#38: the wiki's pages about the business servers moved into the deploy repository (a diagram in the README, `docs/pitfalls.md`, running the key service); the wiki pages kept their concepts and became pointers.
