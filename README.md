# Python CI Example

A simple Python project demonstrating Continuous Integration (CI) with GitHub Actions.

## Overview

This project contains a basic Python function that adds two numbers together, along with unit tests and a CI workflow that automatically runs tests and code quality checks on every push and pull request.

## Project Structure

- `add.py` - A simple addition function with error handling
- `test_add.py` - Unit tests using pytest
- `.github/workflows/ci.yml` - GitHub Actions CI workflow

## Features

- **Automated Testing**: Tests run automatically on every push and pull request
- **Code Quality Checks**: Linting with flake8 to ensure code quality
- **Error Handling**: The addition function validates input types and handles errors gracefully

## Running Tests Locally

```bash
# Install dependencies
pip install pytest flake8

# Run tests
pytest

# Run linting
flake8 . --count --show-source --statistics
```

## Seeing CI in Action

This repository demonstrates CI workflows with two scenarios:

1. **Passing Tests**: The `main` branch contains working code that passes all tests
2. **Failing Tests**: The `break-test` branch intentionally introduces a bug to demonstrate CI failure

To see the CI system in action:

1. Click the **"Actions"** tab at the top of this GitHub repository
2. Look for workflow runs labeled **"Break add function"** (from the break-test branch) - these will show failed tests
3. Look for workflow runs labeled **"fixed"** (from the main branch) - these will show passing tests

The CI workflow automatically runs on every push and pull request, providing immediate feedback on code quality and test results.

<br>
