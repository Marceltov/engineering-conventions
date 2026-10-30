# mcp-login-oauth

**A FastMCP server whose login is a form checked by the service behind it (a Trilium password, a Paperless or InvoiceNinja login) uses [mcp-login-oauth](https://marceltov.github.io/mcp-login-oauth/) as its OAuth server, never a hand-written copy.**

## Why

Four MCP servers carried drifting copies of the same OAuth code: only one slowed down password guessing, none let a public client revoke. One library fixes that once, with an encrypted store that survives restarts, single-use codes also across a restart, revocation for public clients, tokens bound to a resource and protection against guessing. Better Auth can't take its place here: the grant carries the service's own credentials, minted at login.

## How

- `LoginOAuthProvider` with a `check_login` callback that checks the form against the service and returns the grant; tools read the grant from the access token.
- Pin the git tag: `uv add "mcp-login-oauth @ git+https://github.com/Marceltov/mcp-login-oauth@vX.Y.Z"`.
- Its own store (`build_store`) next to the server's data; the secret comes from the server's env var.
- It is Python only. Anything in TypeScript signs in with [Better Auth](better-auth.md), including its MCP endpoint; the library's [TypeScript page](https://marceltov.github.io/mcp-login-oauth/typescript/) says how.

## Rules out

- A copy of OAuth server code in an MCP server.
- Using mcp-login-oauth for a web app's user accounts or sessions.
- An unpinned install.

## Reference

trilium-mcp, invoiceninja-mcp, paperless-ngx-mcp and the recall engine in trilium-llm-wiki.
