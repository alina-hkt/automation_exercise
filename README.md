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

### 1. Clone the repository.
```powershell
git clone https://github.com/alina-hkt/automation_exercise.git
```

### 2. Navigate to the project folder.
```powershell
cd automation_exercise
```

### 3. Build the Docker image.
```powershell
docker build -t allure-tests .
```

### 4. Run tests.
```powershell
.\run-docker.ps1
```