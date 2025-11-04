from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = '[data-test="checkout"]'
        self.first_name_input = '[data-test="firstName"]'
        self.last_name_input = '[data-test="lastName"]'
        self.postal_code_input = '[data-test="postalCode"]'
        self.continue_button = '[data-test="continue"]'
        self.finish_button = '[data-test="finish"]'
        self.success_message = '.complete-header'

    def start_checkout(self):
        self.page.click(self.checkout_button)

    def fill_information(self, first_name, last_name, postal_code):
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.postal_code_input, postal_code)
        self.page.click(self.continue_button)

    def finish_checkout(self):
        self.page.click(self.finish_button)

    def get_success_message(self):
        return self.page.inner_text(self.success_message)
