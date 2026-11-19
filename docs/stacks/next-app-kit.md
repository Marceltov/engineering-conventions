# next-app-kit

**Every Next.js app takes sign-in, API tokens, MCP, REST and migrations from [next-app-kit](https://github.com/Marceltov/next-app-kit); it never copies them.** The app keeps its domain, its pages and its words; the kit holds the infrastructure under them. Decided 2026-11-19.

## Why

noticebox, freundebuch and Gamepanion each carried their own copy of the same infrastructure: Better Auth with the allowlist and an emailed code, API tokens, the MCP endpoint and its OAuth server, the REST route table with its OpenAPI document, the migrations runner and a test sign-in. The copies drifted: a fix to an origin check, a refused token or a hashed code reached the other apps only if someone carried it over. A new app (upload) was about to start as the fifth copy. [Shared code lives once](../code/shared-code-lives-once.md) says the same inside one repository; across the apps, the shared package is a library of its own. On 2026-11-19 the most complete copy, noticebox's, was extracted into next-app-kit and released as `v0.1.0`.

## How

- **Install it from a release,** not from npm: each GitHub release of next-app-kit attaches the package as `npm pack` makes it; the app depends on that asset's URL, and the lockfile pins its hash (`npm install https://github.com/Marceltov/next-app-kit/releases/download/vX.Y.Z/next-app-kit-X.Y.Z.tgz`).
- **One entry point per part:** `next-app-kit/signin` ([Sign-in](../architecture/sign-in.md), [Better Auth](better-auth.md)), `/tokens`, `/mcp` (tools with `guidance`, [MCP first](../architecture/mcp-first.md)), `/rest`, `/multipart`, `/migrations`, `/next` (the route handlers; the only part that imports Next.js) and `/testing` (the test sign-in, `callTool`).
- **The app passes what is its own:** its settings prefix (every setting is `<PREFIX>_*`), its API token prefix, its tools and the REST operations that mirror them, the sign-in mail's texts and its `log` function. Its migration list stays in `backend/db/migrations.ts` ([SQLite](sqlite.md)) and runs through the kit's `migrate`.
- **Route files are one line each,** over the app's runtime, opened at the first request (the kit's README lists them; `examples/minimal` in the kit is the copy-in source, the consent page included).
- **Pages stay the app's:** the kit ships no UI. The sign-in, token and consent pages are written in the app's design against Better Auth's client.
- **Peers move together:** Better Auth and its plugins, the MCP SDK, Next.js, better-sqlite3, kysely, zod and nodemailer are exact peers of the kit. They are upgraded in the kit first, in one release, then in the apps.
- **A fix or a missing piece goes into the kit,** as a pull request there and a release, then a version bump in the apps. What the kit can't do yet is an issue on the kit, not a local patch.
- **Apps on an older copy** have an issue each that names the modules that move; until they move, a fix made in the kit is ported to them by hand.

## Rules out

- A copy of the kit's sign-in, token, MCP, REST, multipart or migrations-runner code in an app, or a new app that starts from another app's copy.
- Patching the kit's code inside an app (a fork in `node_modules`, a vendored file, a wrapper that changes its behaviour) instead of changing the kit.
- An app upgrading one of the kit's peers on its own.
- App domain, pages or words in the kit.

## Reference

next-app-kit `v0.1.0` (extracted from noticebox; its ADR 0001 says what changed on the way: `next` became `guidance`, passkeys, settings by prefix); its `examples/minimal`. upload is the first app to be built on it; noticebox, freundebuch and Gamepanion each have an issue to move onto it.
