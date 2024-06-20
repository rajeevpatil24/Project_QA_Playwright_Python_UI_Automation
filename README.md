
# Automation Framework

This repository contains an automation framework for testing web applications using Playwright with Python. It includes test scripts, page objects, configuration files, and GitHub Actions setup for continuous integration.

## Repository Structure

```
automation-framework/
│
├── tests/
│   ├── test_login.py         # Test cases for login functionality which consists of positive & negative test scenarios whic are parameterized.
│   └── test_product_listing.py  # Test cases for product listing functionality
│
├── pages/
│   ├── login_page.py         # Page object for login page interactions
│   └── product_page.py       # Page object for product listing and details interactions
│
├── config/
│   └── config.py             # Configuration file for environment variables (e.g., URLs)
│
├── requirements.txt          # List of Python dependencies
│
└── .github/
    └── workflows/
        └── run_automation.yml   # GitHub Actions workflow for automated testing and deployment
```

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd automation-framework
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

### Config File (`config/config.py`)

Modify the configuration file to set environment-specific variables like URLs.

```python
# config/config.py

BASE_URL = "http://your-application-url.com"
VALID_USER = "your_valid_username"
VALID_PASSWORD = "your_valid_password"
INVALID_USER = "invalid_username"
INVALID_PASSWORD = "invalid_password"
```

## Running Tests

### Run All Tests

```bash
pytest
```

### Run Specific Tests

```bash
pytest tests/test_login.py
pytest tests/test_product_listing.py
```

### Generate HTML Reports

```bash
pytest tests/test_login.py --html=reports/test_report_login.html
pytest tests/test_product_listing.py --html=reports/test_report_product_listing.html
```

## GitHub Actions

The repository is configured with GitHub Actions to automate testing on every push.

- The workflow (`run_automation.yml`) installs dependencies, runs tests, and generates reports.
- Test reports are uploaded as artifacts and can be accessed from the Actions tab in GitHub.

