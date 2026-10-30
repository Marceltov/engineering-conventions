# HTTPS clients trust the OS certificate store

**Every piece of code that calls something over HTTPS verifies TLS against the operating system's trust store, through [truststore](https://pypi.org/project/truststore/) in Python, not against certifi's bundle.** Decided 2026-10-30.

## Why

httpx and requests verify against certifi by default. A server whose certificate chains to a CA that the operating system trusts but certifi doesn't (a corporate root in the macOS Keychain, an internal CA in the Windows store or `/etc/ssl`) fails with `CERTIFICATE_VERIFY_FAILED: self-signed certificate in certificate chain`, while browsers and curl reach it. The workarounds are worse: a hand-exported PEM in `SSL_CERT_FILE` goes stale, and turning verification off turns it off.

## How

One context per client, and `truststore` is a direct dependency of the package that makes the call:

```python
import ssl, truststore
ctx = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

httpx.Client(..., verify=ctx)                      # httpx
urllib.request.urlopen(request, context=ctx)       # urllib
```

- **Every client**, not only the ones for internal servers: model downloads, public APIs and Wikipedia too, so nobody has to guess later which call meets a corporate proxy.
- **Turning checking off stays an explicit switch** (`VERIFY_TLS=false` → `verify=False`), never the default and never the fix.
- **One test per project** shows each client is built with a `truststore.SSLContext` (with httpx: `client._transport._pool._ssl_context`) and that the off switch still turns checking off.
- Prefer the explicit context per client over `truststore.inject_into_ssl()`, which patches `ssl` for the whole process and every library in it.

## Rules out

- Relying on certifi's bundle, or shipping a PEM file and pointing `SSL_CERT_FILE` at it.
- `verify=False` as a default or as the fix for a certificate error.
- `truststore.inject_into_ssl()` in library code.

## Reference

passageway (Marceltov/passageway#66): its Confluence, Trilium and Wikipedia connectors, the OpenAI embedder and the model download. mcp-login-oauth's Python package uses it for calls to OIDC providers (ADR 0004).
