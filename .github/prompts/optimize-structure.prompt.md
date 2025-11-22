---
agent: agent
---
Define the task to achieve, including specific requirements, constraints, and success criteria.

Add an additional prompt that instructs the agent to optimize repository structure and test layout with a focus on pytest + Playwright best practices.

New prompt to add:

You are optimizing the repository structure and test suite for a Python project using pytest and Playwright. Produce a minimal, actionable plan and (if requested) code changes that follow these constraints and success criteria.

Requirements & focus areas:
- Recommended repository layout (tests/, tests/integration/, tests/unit/, conftest.py, fixtures/, .github/workflows/).
- Minimal example test(s) demonstrating pytest-playwright usage and a browser fixture; keep examples small and runnable.
- conftest.py best practices: scope selection, fixture composition, browser lifecycle, use of pytest-playwright fixtures or custom wrappers, avoiding shared mutable state.
- Dependency manifest: minimal requirements.txt or pyproject.toml entries (pytest, playwright, pytest-playwright, pytest-xdist optional).
- CI recommendations: steps to create venv, install dependencies, run `playwright install` to fetch browser binaries, run pytest, cache pip and Playwright artifacts, matrix for Python versions.
- Test design best practices: clear test names, small single-assert tests, parametrization where appropriate, markers for slow/flaky tests, retries for flaky tests via pytest-rerunfailures or use CI-level retries, isolate tests to avoid order dependence.
- Flakiness mitigation: use robust selectors, explicit waits or built-in Playwright wait-for methods, avoid sleeps, capture screenshots and traces on failure.
- Performance & parallelism: guidance for pytest-xdist and Playwright context isolation per worker; warn about shared resources and recommend per-worker artifacts directories.
- Secrets & environment: use environment variables for credentials; do not hardcode secrets in repo.
- Minimal changes policy: propose only the necessary files (one example test, conftest.py, requirements.txt, and a short CI workflow) unless user approves more.

Constraints:
- Keep changes minimal and focused; do not check in browser binaries.
- Prefer explicit, small examples instead of heavy scaffolding.
- Include short PR description for any file additions or edits.

Success criteria:
- Clear recommended layout and rationale.
- Small runnable example test(s) that pass locally after:
  1) creating a venv,
  2) installing requirements,
  3) running `playwright install`,
  4) running `pytest -q`.
- CI snippet that installs browsers and runs tests.
- Recommendations for avoiding flakiness and improving maintainability.

If the user asks you to apply changes, produce the exact file contents to add or edit and a brief PR description. If they ask only for guidance, provide the plan and prioritized next steps.