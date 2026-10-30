# Better Auth

**An app with a web UI and its own users signs in with [Better Auth](https://better-auth.com), set up stricter than its defaults: links, codes and tokens stored hashed, no session tokens as bearer tokens, telemetry off, and its tables in their own SQLite file.**

## Why

Better Auth is an open-source (MIT) library that runs in the app's process: accounts, sessions, magic links, email codes, passkeys, any OpenID Connect provider, and an OAuth server for MCP clients. It keeps sign-in code out of each app. Some of its defaults are weaker than these conventions, so each app sets them. The architecture is on [Sign-in](../architecture/sign-in.md).

## How

- **Database:** its own file, `DATA_DIR/auth.sqlite`, next to the app's data. The app's tables carry Better Auth's `user.id` as the user id; deleting a user deletes their data in an `after` hook.
- **Sign-in methods:** OpenID Connect providers from the app's own env vars (`<APP>_OIDC_<NAME>_ISSUER`, `_CLIENT_ID`, `_CLIENT_SECRET`, `_LABEL`), built-in providers for Google and Apple, `genericOAuth` for the rest; magic link and email code (`email-otp`) sent through the app's SMTP settings; passkeys (`@better-auth/passkey`), added while signed in.
- **MCP:** `@better-auth/mcp` with `@better-auth/cimd`; tokens bound to the MCP resource. Dynamic client registration only when a client needs it (claude.ai does).
- **Backends:** the `jwt` plugin; backends check its tokens against `/api/auth/jwks`.
- **Identity:** verified email by default, with `trustedProviders`; `disableImplicitLinking` when a second sign-in must be linked by hand.
- **Settings that differ from the defaults:**
    - `storeToken: "hashed"` for magic links and `storeOTP: "hashed"` for email codes;
    - no `bearer` and no `device-authorization` plugin: Better Auth stores session tokens in plain text, and without the `bearer` plugin a copied one is useless, because the cookie must carry a signature made with the secret;
    - an email holds only a code during an MCP or script sign-in;
    - telemetry stays off (nothing sets `telemetry.enabled` or `BETTER_AUTH_TELEMETRY`);
    - the secret comes from the app's own env var and is passed in.
- **A refused sign-in says why.** A provider that refuses a sign-in sends `error` (and optionally `error_description`) back to the callback, and Better Auth passes
  it on to `errorCallbackURL` as `?error=`. The sign-in page shows that code and the server logs it with the provider's name, so a misconfigured provider
  shows in the app's own logs, not only in the provider's.
- **Pages:** Better Auth ships none. The app builds its sign-in and consent pages in its own design, against Better Auth's client.

## Rules out

- Hand-written sign-in, session or OAuth code next to Better Auth.
- The `bearer` or `device-authorization` plugin.
- Plain-text magic links or codes; telemetry turned on.
- Better Auth's tables in the app's data file.
- A failed provider sign-in that ends on a generic error and leaves no line in the app's log.

## Reference

questlog ADR 0004 (sign-in with Better Auth, in its own SQLite file).
