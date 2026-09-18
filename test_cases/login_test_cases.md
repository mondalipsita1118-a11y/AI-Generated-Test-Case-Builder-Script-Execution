# AI-Generated Test Cases
The following test cases were generated with the assistance of AI based on the login functionality requirement of the SauceDemo application.

## Test Case Summary

| TC ID        | Test Scenario                                  | Test Data                          | Expected Result                                                                           |
| ------------ | ---------------------------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------- |
| TC_LOGIN_001 | Login with valid username and password         | `standard_user` / `secret_sauce`   | User should successfully log in and navigate to the Products page                         |
| TC_LOGIN_002 | Login with invalid username and valid password | `invalid_user` / `secret_sauce`    | Login should fail and an appropriate error message should be displayed                    |
| TC_LOGIN_003 | Login with valid username and invalid password | `standard_user` / `wrong_password` | Login should fail and an appropriate error message should be displayed                    |
| TC_LOGIN_004 | Login with empty username and password         | Empty / Empty                      | Validation message should be displayed for empty fields                                   |
| TC_LOGIN_005 | Login with locked-out user                     | `locked_out_user` / `secret_sauce` | User should not be allowed to log in and an appropriate error message should be displayed |

---

# Detailed Test Cases

## TC_LOGIN_001 — Login with Valid Credentials
**Test Scenario:**
Verify that a user can successfully log in using valid credentials.

**Precondition:**
User is on the SauceDemo login page.

**Test Data:**
* Username: `standard_user`
* Password: `secret_sauce`

**Test Steps:**
1. Open the SauceDemo website.
2. Verify that the login page is displayed.
3. Enter `standard_user` in the Username field.
4. Enter `secret_sauce` in the Password field.
5. Click the Login button.

**Expected Result:**
The user should be successfully logged in and redirected to the Products page. The page should display the **Products** title.

**Test Type:** Positive / Functional

---

## TC_LOGIN_002 — Login with Invalid Username

**Test Scenario:**
Verify that login fails when an invalid username is provided with a valid password.

**Precondition:**
User is on the SauceDemo login page.

**Test Data:**
* Username: `invalid_user`
* Password: `secret_sauce`

**Test Steps:**
1. Open the SauceDemo website.
2. Verify that the login page is displayed.
3. Enter `invalid_user` in the Username field.
4. Enter `secret_sauce` in the Password field.
5. Click the Login button.

**Expected Result:**
The user should not be logged in. An appropriate error message should be displayed indicating that the username or credentials are not valid.

**Test Type:** Negative / Functional

---

## TC_LOGIN_003 — Login with Invalid Password

**Test Scenario:**
Verify that login fails when a valid username is used with an incorrect password.

**Precondition:**
User is on the SauceDemo login page.

**Test Data:**
* Username: `standard_user`
* Password: `wrong_password`

**Test Steps:**
1. Open the SauceDemo website.
2. Verify that the login page is displayed.
3. Enter `standard_user` in the Username field.
4. Enter `wrong_password` in the Password field.
5. Click the Login button.

**Expected Result:**
The user should not be logged in. An appropriate error message should be displayed indicating that the username or password is not valid.

**Test Type:** Negative / Functional

---

## TC_LOGIN_004 — Login with Empty Credentials

**Test Scenario:**
Verify that the application displays a validation message when the user attempts to log in without entering credentials.

**Precondition:**
User is on the SauceDemo login page.

**Test Data:**
* Username: Empty
* Password: Empty

**Test Steps:**
1. Open the SauceDemo website.
2. Verify that the login page is displayed.
3. Leave the Username field empty.
4. Leave the Password field empty.
5. Click the Login button.

**Expected Result:**
The user should not be logged in. The application should display a validation message indicating that the Username field is required.

**Test Type:** Negative / Validation

---

## TC_LOGIN_005 — Login with Locked-Out User

**Test Scenario:**
Verify that a locked-out user cannot log in to the application.

**Precondition:**
User is on the SauceDemo login page.

**Test Data:**
* Username: `locked_out_user`
* Password: `secret_sauce`

**Test Steps:**
1. Open the SauceDemo website.
2. Verify that the login page is displayed.
3. Enter `locked_out_user` in the Username field.
4. Enter `secret_sauce` in the Password field.
5. Click the Login button.

**Expected Result:**
The user should not be allowed to log in. An appropriate error message should be displayed indicating that the user has been locked out.

**Test Type:** Negative / Functional / Account State

---
