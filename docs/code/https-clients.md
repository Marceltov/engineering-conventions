# HTTPS clients trust the OS certificate store

**Every piece of code that calls something over HTTPS verifies TLS against the operating system's trust store, not against a bundle shipped with the language: through [truststore](https://pypi.org/project/truststore/) in Python, not certifi's bundle; with `--use-system-ca` in Node, not Node's compiled-in list.** Decided 2026-10-30 for Python, 2026-11-10 for Node.

## Why

httpx and requests verify against certifi by default. A server whose certificate chains to a CA that the operating system trusts but certifi doesn't (a corporate root in the macOS Keychain, an internal CA in the Windows store or `/etc/ssl`) fails with `CERTIFICATE_VERIFY_FAILED: self-signed certificate in certificate chain`, while browsers and curl reach it. The workarounds are worse: a hand-exported PEM in `SSL_CERT_FILE` goes stale, and turning verification off turns it off.

Node has the same gap: `fetch` and `https` verify against the CA list compiled into the Node binary, so a webhook or an ntfy server behind an internal CA fails with `UNABLE_TO_GET_ISSUER_CERT_LOCALLY` although `curl` in the same container reaches it.

## How

### Python

One context per client, and `truststore` is a direct dependency of the package that makes the call:

```python
import ssl, truststore

ctx = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

httpx.Client(..., verify=ctx)  # httpx
urllib.request.urlopen(request, context=ctx)  # urllib
```

- **Every client**, not only the ones for internal servers: model downloads, public APIs and Wikipedia too, so nobody has to guess later which call meets a corporate proxy.
- **Turning checking off stays an explicit switch** (`VERIFY_TLS=false` → `verify=False`), never the default and never the fix.
- **One test per project** shows each client is built with a `truststore.SSLContext` (with httpx: `client._transport._pool._ssl_context`) and that the off switch still turns checking off.
- Prefer the explicit context per client over `truststore.inject_into_ssl()`, which patches `ssl` for the whole process and every library in it.

### Node

Node reads the system store when it is started with `--use-system-ca` (Node 22.15 or newer), for every `fetch` and `https` call of the process. A server's image sets it where the process starts, and makes the system store something an operator can extend:

```dockerfile
RUN apk add --no-cache ca-certificates
CMD ["node", "--use-system-ca", "server.js"]
```

```sh
# docker-entrypoint.sh, while still root: CAs mounted into /usr/local/share/ca-certificates join the store.
if [ "$(id -u)" = 0 ] && ls /usr/local/share/ca-certificates/*.crt >/dev/null 2>&1; then
  update-ca-certificates >/dev/null 2>&1
fi
```

- **An extra CA is mounted, not built in:** `./my-root-ca.crt:/usr/local/share/ca-certificates/my-root-ca.crt:ro` in the compose file; the docs page on notifications or webhooks says how.
- **The flag on the command, not in `NODE_OPTIONS`** of the server's `.env`, where an unchanged copy could lose it.
- **One check per project:** the CI smoke test reads the image's command (`docker inspect --format '{{json .Config.Cmd}}'`) for `--use-system-ca`. The running process can't be asked: Next.js renames its process title.



- Relying on certifi's bundle, or shipping a PEM file and pointing `SSL_CERT_FILE` at it.
- `verify=False` as a default or as the fix for a certificate error.
- `truststore.inject_into_ssl()` in library code.
- In Node: `NODE_TLS_REJECT_UNAUTHORIZED=0`, or `NODE_EXTRA_CA_CERTS` pointing at a PEM file shipped with the code.

## Reference

passageway (Marceltov/passageway#66): its Confluence, Trilium and Wikipedia connectors, the OpenAI embedder and the model download. noticebox (noticebox/noticebox#58): its ntfy and webhook calls, the image's entrypoint and the smoke test.
