# Python and FastMCP

**Python projects use `uv` for dependencies and running, `pytest` for tests and FastMCP for MCP servers. Every HTTPS client trusts the OS certificate store. Python never serves a UI: a UI is TypeScript and React, and a Python backend behind it only checks tokens.**

## Why

`uv` is fast, locks exactly, and runs tools without installing them (`uvx`). FastMCP is the shortest way to an MCP server with OAuth hooks. Keeping every UI in TypeScript means one way to build pages and one place for sign-in; Python joins where its libraries are needed, behind the app.

## How

- **Project:** `pyproject.toml` with a build backend, a `src/` layout, `uv.lock` committed; `uv sync`, `uv run pytest -q`.
- **Formatting and linting:** Ruff, with the shared `ruff.toml` (`uv add --dev ruff`; `uv run ruff format`, `uv run ruff check`), see [Formatting and linting](../code/formatting.md).
- **HTTPS:** a `truststore.SSLContext` per client, see [HTTPS clients](../code/https-clients.md).
- **MCP servers:** FastMCP; when the login is a form checked by a service, [mcp-login-oauth](mcp-login-oauth.md) as the OAuth server.
- **A Python backend behind a Next.js app** checks JWTs from the app's Better Auth (`/api/auth/jwks`, issuer, audience, expiry) and takes the user id from them; for an MCP endpoint in Python, FastMCP's `JWTVerifier` does it. See [Sign-in](../architecture/sign-in.md).
- **Config** from environment variables, read in one module.

## Rules out

- A web UI in Python.
- A Python backend that signs users in or trusts a forwarded user id.
- `pip install` into a global environment; unpinned dependencies.
- certifi's bundle for HTTPS.

## Reference

mcp-login-oauth (package layout, `uv`, `pytest`); passageway (`truststore`); trilium-mcp, invoiceninja-mcp and paperless-ngx-mcp (FastMCP with mcp-login-oauth).
