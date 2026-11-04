# Shared code lives once

**When the same code is needed in a second package of a repository, it moves into the repository's shared package and both use it; it is never copied.** Decided 2026-11-03.

## Why

A helper that is copied three times is fixed in one of them. passageway's connectors each carried their own `_list` and `_int` for reading settings, and the HTTP clients of four packages repeated the same rules (the system trust store, a user agent, a size cap, "a server error fails the whole call"). Adding two more connectors would have made five copies, with the next fix landing in only some of them. The second copy is the moment to share: the code is still small, the call sites are still few, and the tests of the first copy already describe the behaviour.

## How

- **Share at the second use,** not the third. Look for the copy before writing a new helper: grep the repository for the function or the pattern.
- **Put it in the repository's shared package** (a library of the monorepo, an SDK, a `common` module), with the tests of the copy it replaces, and document it where the package is documented.
- **Keep the shared package light.** Standard-library helpers go in plainly. Code that needs a dependency goes behind an optional extra (`package[web]`), so a package that does not need it does not carry it.
- **Move the older copies in the same change,** or open an issue per package that names what is left. A shared helper next to its own copies is a third copy.
- **Say what is not shared, and why.** Code that looks alike but differs where it matters (authentication, retries, redirects) stays separate until the shared version can take the difference without a flag per caller.
- **A private name imported across packages is a copy in disguise.** Importing another package's `_helper` is the sign to move it to the shared package.

## Rules out

- A function copied into a second package.
- Importing an underscore name from another package.
- A shared package that gains a dependency for everyone to serve one caller.
- A shared helper with a flag per caller for each way the callers differ.

## Reference

passageway (Marceltov/passageway#110): the SDK's `settings` helpers and its `web` client behind `passageway-sdk[web]` (#111), the older connectors moved onto them (#112), and the llms.txt and sitemap connectors written against them (#108, #109).
