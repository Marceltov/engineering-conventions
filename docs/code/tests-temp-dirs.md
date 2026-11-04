# Tests keep their data in temporary directories

**A test never writes to the app's real data directory (the default `DATA_DIR`, `/data` or wherever the app keeps its database, uploads and secrets). The test setup points it at a temporary directory of the test's own, for every test, including ones that don't think about it.** Decided 2026-11-04.

## Why

In freundebuch, tests that shared files didn't set `DATA_DIR` and fell back to the default `/data`. On a development machine that folder was writable and also held other apps' databases, so the tests passed there and left about 180 files behind. In CI `/data` wasn't writable: every share failed quietly and the tests broke only there (2026-11-04). A test that relies on the machine it runs on tests the machine, not the code.

## How

One setup file, loaded before every test file, makes a temporary directory, sets the data directory to it before each test and removes it at the end. A test that needs its own directory still sets one; a test that needs the default unsets it for itself.

Vitest (`vitest.config.*`: `test: { setupFiles: ["<path>/setup.ts"] }`):

```ts
import { mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterAll, beforeEach } from "vitest";

const dir = mkdtempSync(join(tmpdir(), "<app>-test-"));
process.env.DATA_DIR = dir;
beforeEach(() => {
  process.env.DATA_DIR = dir; // set again: a test that changed or deleted it doesn't leak into the next
});
afterAll(() => rmSync(dir, { recursive: true, force: true }));
```

pytest (`conftest.py` at the root of the tests):

```python
import pytest

@pytest.fixture(autouse=True)
def data_dir(tmp_path, monkeypatch):
    monkeypatch.setenv("DATA_DIR", str(tmp_path))
```

- **One test pins it:** with nothing set, the app's data directory is under the system's temp directory, not the default.
- The test of the default itself (`DATA_DIR` unset gives `/data`) clears the variable inside that test.
- The same goes for every other path the app writes by default: a log file, a cache, a socket.

## Rules out

- A test that reads or writes the default data directory, or any path outside a temporary directory.
- Leaving the data directory to each test file to remember.
- A test that passes only on a machine where the default path happens to be writable.

## Reference

freundebuch (Marceltov/freundebuch#133): `backend/testing/setup.ts` in Vitest's `setupFiles`, pinned by `backend/testing/setup.test.ts`.
