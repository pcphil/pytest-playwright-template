"""Example pytest tests for playwright."""
import pytest
from tests.page_objects.login_page import LoginPage

@pytest.mark.smoke
def test_login(page):
    """Example of a simple async test using the browser fixture."""
    loginPage = LoginPage(page)
    loginPage.navigate()
    loginPage.fill_username()
    loginPage.fill_password()
    loginPage.click_login()
    assert "Swag Labs" in page.title()

@pytest.mark.smoke
def test_negative_login(page):
    """Example of a negative login test using the Page Object."""
    loginPage = LoginPage(page)
    loginPage.navigate()
    loginPage.fill_username("invalid_user")
    loginPage.fill_password("invalid_pass")
    loginPage.click_login()
    error_message = loginPage.get_error_message()
    assert "Epic sadface: Username and password do not match any user in this service" in error_message