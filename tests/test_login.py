import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()

# TC_LOGIN_001
def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.login("standard_user", "secret_sauce")

    products_title = driver.find_element(
        By.CLASS_NAME, "title"
    ).text

    assert products_title == "Products"

# TC_LOGIN_002
def test_invalid_username(driver):
    login_page = LoginPage(driver)

    login_page.login("invalid_user", "secret_sauce")

    error_message = login_page.get_error_message()

    assert "Username and password do not match" in error_message

# TC_LOGIN_003
def test_invalid_password(driver):
    login_page = LoginPage(driver)

    login_page.login("standard_user", "wrong_password")

    error_message = login_page.get_error_message()

    assert "Username and password do not match" in error_message

# TC_LOGIN_004
def test_empty_credentials(driver):
    login_page = LoginPage(driver)

    login_page.login("", "")

    error_message = login_page.get_error_message()

    assert "Username is required" in error_message

# TC_LOGIN_005
def test_locked_out_user(driver):
    login_page = LoginPage(driver)

    login_page.login("locked_out_user", "secret_sauce")

    error_message = login_page.get_error_message()

    assert "locked out" in error_message.lower()
