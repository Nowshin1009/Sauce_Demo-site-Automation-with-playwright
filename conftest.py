# conftest.py
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD

@pytest.fixture(scope="function")
def browser_page():
    """
    Launch a fresh browser + page for each test and tear it down after.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="function")
def logged_in_page(browser_page):
    """
    Reuse browser_page, then perform a valid login.
    Returns an authenticated page on the inventory screen.
    """
    login = LoginPage(browser_page)
    login.navigate()
    login.login(USERNAME, PASSWORD)
    return browser_page
