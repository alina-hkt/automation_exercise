# Automation Exercise Tests

[![Playwright Tests with Allure](https://github.com/alina-hkt/automation_exercise/actions/workflows/playwright.yml/badge.svg)](https://github.com/alina-hkt/automation_exercise/actions/workflows/playwright.yml)
[![Allure Report](https://img.shields.io/badge/Allure_Report-Live-green?logo=allure&logoColor=white)](https://alina-hkt.github.io/automation_exercise/)

Tests for the site [Automation Exercise](http://automationexercise.com)

## Code Quality & Linting

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting.

To check code quality:
```powershell
ruff check .
```

## Tech Stack

- 🐍 **Language:** Python 3.12
- 🧪 **Test Framework:** Pytest
- 🌐 **Browser & API Automation:** Playwright
- 📊 **Reporting:** Allure Report
- ✨ **Linting & Formatting:** Ruff
- 🐳 **Containerization:** Docker
- 🔄 **CI/CD:** GitHub Actions

## How to Run

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running

### Steps

1. Clone the repository.
```powershell
git clone https://github.com/alina-hkt/automation_exercise.git
```

2. Navigate to the project folder.
```powershell
cd automation_exercise
```
3. Create a .env file in the root directory with valid credentials of an existing user.
```powershell
@"
BASE_URL=http://automationexercise.com
TEST_USER_EMAIL=test@example.com
TEST_USER_PASSWORD=TestPassword123
NAME=TestUser
"@ | Out-File -FilePath .env -Encoding utf8 -NoNewline
```

4. Build the Docker image.
```powershell
docker build -t allure-tests .
```

5. Run tests.
```powershell
.\run-docker.ps1
```