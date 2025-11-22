# pytest-playwright-template
Python Template QE Pipeline
## Overview

Minimal pytest + Playwright template for Python QE pipelines. Use this repo as a starting point for browser-based tests with Playwright and pytest.

## Quickstart

1. Create and activate a virtual environment:
    - Windows (cmd.exe):
      ```
      python -m venv .venv
      .venv\Scripts\activate
      ```
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
    If `requirements.txt` is not present, add one containing at least `playwright` and `pytest`.

3. Install Playwright browser binaries:
    ```
    playwright install
    ```

4. Run tests:
    ```
    pytest -q
    ```

## Recommended project layout

- README.md
- LICENSE
- requirements.txt (or pyproject.toml)
- conftest.py
- tests/
  - test_*.py

Put shared fixtures in `conftest.py` and test files under `tests/` named `test_*.py`.

## Example (if you need a minimal test)

Create `tests/test_example.py` with a small, focused test that uses Playwright fixtures. Keep examples minimal and explicit about required setup (e.g., playwright browsers installed).

## Notes & troubleshooting

- If tests show no browser or fail to launch, run `playwright install`.
- Ensure your venv is active and dependencies are installed.
- Use environment variables for secrets; never hardcode keys in tests or CI.

## Contribution & intent

This repository is intended as a lightweight template. If you'd like, I can add a minimal `tests/test_example.py` and a `requirements.txt` that includes `pytest` and `playwright`. If you want CI integration (GitHub Actions), I can propose a small workflow that installs dependencies and runs `playwright install` before `pytest`.
