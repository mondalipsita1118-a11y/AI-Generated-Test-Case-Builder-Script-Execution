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
