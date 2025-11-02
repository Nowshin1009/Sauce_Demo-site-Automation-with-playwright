import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser_page():
    """
    Fixture to launch browser, create a new page, and close it after test.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()
