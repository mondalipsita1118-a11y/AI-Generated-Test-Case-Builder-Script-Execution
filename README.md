# AI-Generated Test Case Builder + Script Execution

## Project Overview

This project demonstrates how AI can be used to assist in software testing by generating test scenarios from a login requirement and then converting one of the test cases into an automated Selenium test.

The project uses the public SauceDemo website for login testing.

**Website:** https://www.saucedemo.com/

### Technology Stack

* Python
* Selenium WebDriver
* pytest
* Page Object Model (POM)
* AI-assisted test-case generation

---

## Requirement

Test the login functionality of the SauceDemo application.

The objective is to:

1. Use an AI tool to generate login test cases.
2. Generate at least 5 test cases.
3. Select at least one test case for automation.
4. Execute the automated test using Selenium.
5. Document how AI helped improve the test design.

---

# AI-Generated Test Cases

AI was used to analyze the login requirement and identify positive, negative, validation, and account-state scenarios.

| Test Case ID | Scenario                     | Test Data                      | Expected Result                                                        |
| ------------ | ---------------------------- | ------------------------------ | ---------------------------------------------------------------------- |
| TC_LOGIN_001 | Login with valid credentials | standard_user / secret_sauce   | User should successfully log in and Products page should be displayed  |
| TC_LOGIN_002 | Login with invalid username  | invalid_user / secret_sauce    | Login should fail and an appropriate error message should be displayed |
| TC_LOGIN_003 | Login with invalid password  | standard_user / wrong_password | Login should fail and an appropriate error message should be displayed |
| TC_LOGIN_004 | Login with empty credentials | Empty / Empty                  | Validation message should be displayed                                 |
| TC_LOGIN_005 | Login with locked-out user   | locked_out_user / secret_sauce | Login should fail and an appropriate error message should be displayed |

---

# How AI Helped With Test Design

AI was used as a test-design assistant rather than only as a code-generation tool.

The login requirement was provided to the AI and it was asked to identify different scenarios that should be tested.

The AI helped identify:

### 1. Positive Scenario

The valid login scenario verifies that a user with correct credentials can successfully access the application.

### 2. Negative Scenarios

AI suggested testing invalid usernames and invalid passwords separately. These scenarios help verify that authentication fails when incorrect credentials are supplied.

### 3. Boundary/Validation Scenario

Testing empty credentials verifies how the application behaves when required login fields are not provided.

### 4. Account-State Scenario

Testing a locked-out user verifies that the application prevents authentication for an account that should not be allowed to log in.

### 5. Test Coverage

Instead of creating only a single happy-path test, AI helped expand the test design to cover positive, negative, validation, and account-state scenarios.

The generated test cases were reviewed and refined before automation.

---

# Automation Approach

The automated test uses Selenium WebDriver with Python and pytest.

A basic Page Object Model is used to separate page locators and page actions from the test logic.

### Page Object

`pages/login_page.py`

The `LoginPage` class contains:

* Username locator
* Password locator
* Login button locator
* Error message locator
* Methods for entering credentials
* Login method
* Error-message retrieval method

### Automated Test

`tests/test_login.py`

The automated test covers:

**TC_LOGIN_001 — Valid Login**

Steps:

1. Open SauceDemo.
2. Enter `standard_user`.
3. Enter `secret_sauce`.
4. Click Login.
5. Verify that the Products page is displayed.

**TC_LOGIN_002 — Invalid Username**

Steps:

1. Open SauceDemo.
2. Enter `invalid_user`.
3. Enter `secret_sauce`.
4. Click Login.
5. Verify that the login should fail and an appropriate error message should be displayed

**TC_LOGIN_003 — Invalid Password**

Steps:

1. Open SauceDemo.
2. Enter `standard_user`.
3. Enter `wrong_password`.
4. Click Login.
5. Verify that the login should fail and an appropriate error message should be displayed

**TC_LOGIN_004 — Login with empty credentials**

Steps:

1. Open SauceDemo.
2. Enter `Empty`.
3. Enter `Empty`.
4. Click Login.
5. Validation message should be displayed

**TC_LOGIN_005 — Login with locked-out user**

Steps:

1. Open SauceDemo.
2. Enter `locked_out_user`.
3. Enter `secret_sauce`.
4. Click Login.
5. Verify that the login should fail and an appropriate error message should be displayed
---

# Project Structure

```text
ai-test-case-builder/
│
├── README.md
├── requirements.txt
│
├── test_cases/
│   └── login_test_cases.md
│
├── pages/
│   └── login_page.py
│
└── tests/
    └── test_login.py
```

---

# Installation

## Step 1: Clone the repository

```bash
git clone <your-github-repository-url>
cd ai-test-case-builder
```

## Step 2: Create a virtual environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

## Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

# Execution

Run the automated test using:

```bash
pytest -v
```

Expected result:

```text
1 passed
```

---

# Test Automation Details

The test uses Selenium WebDriver to interact with the SauceDemo login page.

The test verifies the successful login by checking that the page title displayed after login is:

```text
Products
```

The browser is closed automatically after test execution using the pytest fixture.

---

# AI Usage Summary

AI was used for:

* Identifying login test scenarios
* Expanding positive and negative test coverage
* Identifying validation and locked-account scenarios
* Structuring test cases with test data and expected results
* Reviewing the overall testing approach

The automation code was reviewed and structured manually using Selenium and the Page Object Model.

This demonstrates AI-assisted test design rather than relying only on AI-generated automation code.

---

# Future Improvements

The automation suite could be expanded by:

* Automating the remaining login test cases
* Adding explicit waits where required
* Adding screenshots on test failure
* Generating HTML test reports
* Adding parameterized tests for different credentials
* Integrating the tests with GitHub Actions CI/CD
* Adding additional SauceDemo functional test scenarios
