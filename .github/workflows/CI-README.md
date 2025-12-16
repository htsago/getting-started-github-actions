# CI Workflow Documentation

This document explains the Continuous Integration (CI) workflow defined in `.github/workflows/ci.yml`. The workflow is automatically triggered on every `push` to the `master` branch and runs two main jobs: linting and testing.

## Key Keywords and Structure

### `on:`
Specifies when the workflow should run.

- `push`: Triggers the workflow on every Git push.
- `branches: [ master ]`: Restricts execution to pushes made to the `master` branch.

Only changes pushed to the `master` branch will trigger this CI workflow.

### `jobs:`
A workflow consists of one or more jobs. This configuration defines two jobs (see [ci.yml](ci.yml)).
#### 1. `lint`
- Purpose: Validate code quality using a linter.
- `runs-on: ubuntu-latest`: Specifies that the job runs on the latest stable Ubuntu virtual machine provided by GitHub Actions.
- Steps:
  - Checkout code: Fetches the repository code using the `actions/checkout@v4` action.
  - Set up Python 3.11: Installs Python 3.11 via `actions/setup-python@v5`.
  - Install dependencies: Upgrades `pip` and installs dependencies listed in `requirements.txt`.
  - Run linter: Executes the `ruff` linter across the entire project with the command `ruff check .`.

This step ensures code adheres to style guidelines and detects potential issues early.

#### 2. `test`
- Purpose: Run the automated test suite.
- `runs-on: ubuntu-latest`: Uses the same Ubuntu environment as the `lint` job.
- Steps:
  - Checkout code: Same as above.
  - Set up Python 3.11: Same as above.
  - Install dependencies: Same dependency installation process.
  - Run tests: Executes tests using `pytest` with the command `PYTHONPATH=. pytest tests/`, ensuring the project root is included in the Python module search path.

This step verifies that code changes do not introduce regressions or break existing functionality.

## Summary
This CI configuration ensures that every change merged into `master`:
- Complies with code quality standards (via `ruff`),
- Passes all automated tests (via `pytest`).

Maintaining this workflow helps enforce consistency, reliability, and correctness throughout the development lifecycle.