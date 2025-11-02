from playwright.sync_api import Page
from utils.config import BASE_URL

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = 'input[data-test="username"]'
        self.password_input = 'input[data-test="password"]'
        self.login_button = 'input[data-test="login-button"]'
        self.error_message = '[data-test="error"]'  # added for invalid login

    def navigate(self):
        self.page.goto(BASE_URL)

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self):
        return self.page.inner_text(self.error_message)
