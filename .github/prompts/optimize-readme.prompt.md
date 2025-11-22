---
agent: agent
---
Goal: Update and optimize README.md using the actual repository contents so the README clearly explains the project's purpose, setup, test workflow, and troubleshooting with minimal, repo-specific edits.

Tasks:
1. Inspect the repository root and these locations if present: README.md, LICENSE, tests/, conftest.py, requirements.txt, pyproject.toml, .github/workflows/, and .github/copilot-instructions.md. Use those files to ground recommendations and the new README content.
2. Identify missing or unclear README sections (purpose, prerequisites, installation, Playwright browser install, running tests, CI notes, contributing, troubleshooting, contact/maintainer questions).
3. Produce a single, ready-to-commit replacement README.md that:
  - States project purpose and quick summary.
  - Lists prerequisites and exact commands to set up a virtualenv and install dependencies (include pip install -r requirements.txt or alternative if pyproject.toml present).
  - Includes Playwright-specific step: `playwright install` and notes about CI/browser binaries.
  - Shows exact commands to run tests locally on Windows and Unix (pytest -q, and example Playwright run).
  - Mentions where tests and fixtures live (tests/, conftest.py) and repository conventions.
  - Adds brief troubleshooting tips (empty test output => run playwright install, failing imports => check requirements.txt and PYTHONPATH).
  - Keeps changes minimal and avoids adding files not requested.
4. Output format (strict):
  - Full README.md content only (ready to write to README.md).
  - After the README content, provide a short PR description (1-2 sentences) and a bulleted list of files changed.
  - Provide up to 3 questions for the maintainer (if any clarifications needed).
5. Constraints:
  - Do not create or modify other files unless the maintainer requests it.
  - Do not include secrets or hardcoded credentials.
  - Keep the README concise and actionable.

Success Criteria:
- README explains how to set up the environment, install Playwright browsers, run tests, and troubleshoot common failures.
- The output is a single README.md replacement plus a brief PR description and changed-files list.

Notes:
- Prefer concrete commands for Windows (cmd.exe) and POSIX shells.
- If the repo lacks dependency files, mention that and suggest adding requirements.txt; include a minimal example command to create it only as a suggestion (do not create it).
- Read .github/copilot-instructions.md (if present) and incorporate any repository-specific guidance into the README.