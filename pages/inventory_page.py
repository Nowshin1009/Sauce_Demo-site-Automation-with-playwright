from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_link = 'a.shopping_cart_link'
        self.cart_badge = '.shopping_cart_badge'
        self.inventory_item = '.inventory_item'

    def add_item_by_name(self, name: str):
        """
        Find a product card by its name (e.g., 'Sauce Labs Backpack')
        and click its 'Add to cart' button inside that card.
        """
        item = self.page.locator(self.inventory_item).filter(has_text=name).first
        item.get_by_role("button", name="Add to cart").click()

    def get_cart_count(self) -> int:
        # If no badge is shown, cart is 0
        badge = self.page.locator(self.cart_badge)
        if badge.count() == 0:
            return 0
        text = badge.inner_text()
        return int(text.strip())

    def go_to_cart(self):
        self.page.click(self.cart_link)
