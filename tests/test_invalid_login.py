import pytest
from pages.login_page import LoginPage

def test_invalid_login(browser_page):
    login_page = LoginPage(browser_page)
    login_page.navigate()
    login_page.login("wrong_user", "wrong_password")

    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text
