## Purpose
This repository is a minimal `pytest` + `playwright` test template for Python QE pipelines. The project currently contains only a `README.md` and license; use this file to guide AI coding agents about where to look, what to expect, and how to be productive.

## Quick Context
- Repo root: contains `README.md` and `LICENSE`.
- Expect test code to live in `tests/`, configuration in `conftest.py`, and dependencies in `requirements.txt` or `pyproject.toml` (these are not present yet).

## What to do first (discovery)
- Read `README.md` to capture any human-authored intent or setup notes.
- List repository files and folders. If `tests/`, `conftest.py`, or CI workflows exist, open them before making changes.
- If key files are missing, create minimal, conventional placeholders rather than large unrequested scaffolding (e.g., add `tests/test_example.py` and `requirements.txt` only if asked).

## Development & Test Workflow (assumptions)
- Preferred test runner: `pytest`. Run tests locally with `pytest -q`.
- Typical dependency install: create a venv and `pip install -r requirements.txt` (or `pip install .` if package metadata exists).
- Playwright-specific step: run `playwright install` after installing `playwright` to download browser binaries.

Commands (Windows cmd.exe):
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install
pytest -q
```

If these files are missing, ask the repo owner before adding them.

## Conventions for this repo
- Tests: put tests under `tests/` and name files `test_*.py`.
- Fixtures: put shared fixtures in `conftest.py` at the repo root or `tests/` folder.
- Small, focused tests are preferred for this template; avoid adding heavy infra changes unless requested.

## Integration points & external dependencies
- Playwright (Python package) — requires browser binaries via `playwright install`.
- CI (likely GitHub Actions) — workflow files live under `.github/workflows/` if present. Search for `workflow` filenames to understand CI steps.
- If tests need secrets (browserstack, cloud runners), use environment variables; do not hardcode keys.

## How AI agents should propose changes
- Make minimal, incremental edits and include unit tests for any behavioral change.
- When adding project-level files (e.g., `pyproject.toml`, `requirements.txt`, CI workflow), include a short PR description explaining why the file is required.
- If the repository is empty of expected test files, create a single, minimal example test and document how to run it.

## Troubleshooting pointers
- Empty test outputs: ensure Playwright browsers are installed with `playwright install`.
- Failing imports: check `PYTHONPATH` and confirm dependencies in `requirements.txt` or `pyproject.toml`.

## Where to look next
- `README.md` (already present) — synthesize any instructions into the template.
- `tests/`, `conftest.py`, `requirements.txt`, `pyproject.toml`, `.github/workflows/` — open these if/when they appear.

## Questions for the maintainer
- Do you want this repo to include a working example test and dependency manifest? If yes, should browsers be checked into CI or installed at runtime?

---
If you want, I can: add a minimal `tests/test_example.py` and a `requirements.txt` for Playwright+pytest; or update this file to reference an existing CI workflow if you point me to one.
