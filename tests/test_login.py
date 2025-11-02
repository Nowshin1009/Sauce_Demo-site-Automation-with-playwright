from playwright.sync_api import sync_playwright

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Open the site
        page.goto("https://www.saucedemo.com/")
        
        # Enter credentials
        page.fill('input[data-test="username"]', "standard_user")
        page.fill('input[data-test="password"]', "secret_sauce")
        
        # Click login
        page.click('input[data-test="login-button"]')
        
        # Assert we reached the inventory page
        assert "inventory" in page.url
        
        browser.close()
