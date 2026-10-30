# Next.js app

**An app is one Next.js app in one Docker image: the pages, the REST API and the MCP endpoint in the same process, over a framework-free domain layer and SQLite. TypeScript strict, Tailwind for styling, Vitest for unit tests, Playwright for end-to-end tests.**

## Why

One process and one image is what self-hosting on one server needs: nothing else to run, nothing to keep in step between services. Next.js serves the pages and the route handlers for `/api/v1`, `/mcp` and the sign-in from the same code, so the [one domain layer](../architecture/mcp-first.md) stays one.

## How

- **Layout:** `app/` (pages and route handlers), `components/`, `backend/` (domain, framework-free, imported through `backend/index.ts`), `docs/`, `e2e/`.
- **Pinned exactly:** `next`, `eslint-config-next` and the MCP SDK carry exact versions, not ranges; they move together through one Dependabot group. Next.js has breaking changes between minors: check `node_modules/next/dist/docs/` before relying on a remembered API.
- **Scripts:** `dev`, `build`, `start`, `lint` (ESLint with the boundary rule and `eslint-config-prettier`), `format` and `format:check` (Prettier, [Formatting and linting](../code/formatting.md)), `typecheck` (`next typegen && tsc --noEmit`), `test` (Vitest), `test:e2e` (Playwright), `generate` (OpenAPI from the route table, committed).
- **End-to-end tests run against `next dev`**, with a test-only sign-in route that exists only under an env flag and is compiled out of production builds.
- **Styling:** Tailwind through `@tailwindcss/postcss`; icons from `lucide-react`.
- **Validation:** `zod` at every boundary (route input, tool input, config).
- **Logs:** `pino`, structured, English, never a token, a form or a person's details.
- **Image:** multi-stage Dockerfile, `output: "standalone"`, a distroless Node runtime, a `HEALTHCHECK` on `/health`, data in `DATA_DIR` on one volume. The Node major lives in `.nvmrc` and the Dockerfile and moves by hand, in both at once.
- **Config:** env vars `<APP>_*` except `PUBLIC_URL`, `DATA_DIR`, `PORT`, `TZ`; `backend/config.ts`, `.env.example`, `compose.yaml` and the configuration docs change together.
- **Sign-in:** Better Auth, see [Sign-in](../architecture/sign-in.md).

## Rules out

- A second service (a sidecar API, a separate MCP server) for what one app can serve.
- Version ranges on `next` or the MCP SDK.
- Business logic in `app/` or `components/`.
- A test-only route reachable in a production build.

## Reference

freundebuch (Next.js, SQLite, Tailwind, Vitest, Playwright, distroless image); questlog follows it (ADR 0001).
