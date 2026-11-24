"""The shared CodeQL workflow leaves out test code and nothing else.

Reads the `paths-ignore` list from .github/workflows/codeql.yml and checks it against sample paths of the stacks in
use: every test file must match, every file that ships must not. Run: uv run --with pyyaml scripts/check_codeql_paths.py
"""

import sys
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parent.parent

LEFT_OUT = [
    "tests/test_client.py",
    "tests/conftest.py",
    "backend/tests/test_api.py",
    "pkg/test_mapping.py",
    "pkg/mapping_test.py",
    "conftest.py",
    "web/__tests__/page.tsx",
    "web/app/page.test.tsx",
    "web/lib/copy.spec.ts",
    "web/lib/format.test.js",
    "src/test/java/org/example/AppTest.java",
    "internal/store/store_test.go",
]
SCANNED = [
    "ing_fints/plugin.py",
    "trade_republic/client.py",
    "app/main.py",
    "backend/app/services/testing.py",
    "pkg/contest.py",
    "pkg/latest_rates.py",
    "web/app/page.tsx",
    "web/lib/test-data-builder.ts",
    "web/lib/spec.ts",
    "src/main/java/org/example/App.java",
    "internal/store/store.go",
    ".github/workflows/ci.yml",
]


def ignored(path: str, patterns: list[str]) -> bool:
    return any(PurePosixPath(path).full_match(pattern) for pattern in patterns)


def main() -> int:
    workflow = yaml.safe_load((ROOT / ".github/workflows/codeql.yml").read_text())
    init = next(s for s in workflow["jobs"]["analyze"]["steps"] if s.get("uses", "").startswith("github/codeql-action/init"))
    patterns = yaml.safe_load(init["with"]["config"])["paths-ignore"]
    wrong = [f"scanned although test code: {p}" for p in LEFT_OUT if not ignored(p, patterns)]
    wrong += [f"left out although it ships: {p}" for p in SCANNED if ignored(p, patterns)]
    print("\n".join(wrong) or f"codeql paths-ignore: {len(LEFT_OUT)} test paths left out, {len(SCANNED)} shipped paths scanned")
    return 1 if wrong else 0


if __name__ == "__main__":
    sys.exit(main())
