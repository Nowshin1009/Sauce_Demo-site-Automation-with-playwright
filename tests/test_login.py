from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD

def test_valid_login(browser_page):
    """
    Test a successful login using valid credentials.
    """
    login_page = LoginPage(browser_page)
    login_page.navigate()
    login_page.login(USERNAME, PASSWORD)

    # Verify user is redirected to inventory page
    assert "inventory" in browser_page.url
