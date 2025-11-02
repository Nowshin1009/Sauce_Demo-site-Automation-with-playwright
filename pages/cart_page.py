from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_item_names = '.inventory_item_name'

    def get_item_names(self):
        return self.page.locator(self.cart_item_names).all_inner_texts()
