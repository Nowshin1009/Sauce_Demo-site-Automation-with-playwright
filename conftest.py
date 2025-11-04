import pytest
import os
import base64
from datetime import datetime
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD

# ------------------------------------------------------------
# Fixture 1: Base browser/page setup
# ------------------------------------------------------------
@pytest.fixture(scope="function")
def browser_page():
    """
    Launch a fresh browser + page for each test, and close afterward.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

# ------------------------------------------------------------
# Fixture 2: Logged-in page (depends on browser_page)
# ------------------------------------------------------------
@pytest.fixture(scope="function")
def logged_in_page(browser_page):
    """
    Use the browser_page fixture to open a logged-in session.
    Returns an authenticated Playwright page.
    """
    login = LoginPage(browser_page)
    login.navigate()
    login.login(USERNAME, PASSWORD)
    return browser_page

# ------------------------------------------------------------
# Pytest Hook: Capture screenshot on failure
# ------------------------------------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    This hook runs after each test.
    If a test fails, capture a screenshot and (optionally) embed it in HTML report.
    """
    outcome = yield
    report = outcome.get_result()

    # Run only after the actual test call
    if report.when == "call" and report.failed:
        page = item.funcargs.get("browser_page") or item.funcargs.get("logged_in_page")
        if page:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            file_path = os.path.join(screenshot_dir, f"{item.name}_{timestamp}.png")

            # Save screenshot
            page.screenshot(path=file_path, full_page=True)
            print(f"\nScreenshot saved to: {file_path}")

            # Attach screenshot to pytest-html report (if enabled)
            if hasattr(report, "extra"):
                with open(file_path, "rb") as f:
                    encoded = base64.b64encode(f.read()).decode("utf-8")
                html = (
                    f'<div><img src="data:image/png;base64,{encoded}" '
                    f'alt="screenshot" style="width:600px;height:auto;" '
                    f'onclick="window.open(this.src)" /></div>'
                )
                report.extra.append(pytest.html.extras.html(html))
