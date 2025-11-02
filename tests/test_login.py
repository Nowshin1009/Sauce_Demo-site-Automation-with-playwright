from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        assert "inventory" in page.url

        browser.close()
