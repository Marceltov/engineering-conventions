# mcp-login-oauth

**An MCP server whose login is a form checked by the service behind it (a Trilium password, a Paperless or InvoiceNinja login), or a sign-in at one OpenID Connect provider, uses [mcp-login-oauth](https://marceltov.github.io/mcp-login-oauth/) as its OAuth server, never a hand-written copy.**

## Why

Four MCP servers carried drifting copies of the same OAuth code: only one slowed down password guessing, none let a public client revoke. One library fixes that once, with an encrypted store that survives restarts, single-use codes also across a restart, revocation for public clients, tokens bound to a resource and protection against guessing. Better Auth can't take its place here: the grant carries the service's own credentials, minted at login.

## How

- **Python** (FastMCP): `LoginOAuthProvider` with a `check_login` callback that checks the form against the service and returns the grant; pin the git tag (`@vX.Y.Z`).
- **TypeScript:** `createLoginOAuth` with a `form` or `oidc` login; install the release tarball of a `ts-vX.Y.Z` tag.
- **Its own store file** (`oauth.sqlite` or the Python file store) next to the server's data; the secret comes from the server's env var.
- **Not for apps with a web UI and their own users**: those use [Better Auth](better-auth.md).

## Rules out

- A copy of OAuth server code in an MCP server.
- Using mcp-login-oauth for a web app's user accounts or sessions.
- An unpinned install.

## Reference

trilium-mcp, invoiceninja-mcp, paperless-ngx-mcp and the recall engine in trilium-llm-wiki (Python); mcp-login-oauth's values V7 and ADR 0004.
