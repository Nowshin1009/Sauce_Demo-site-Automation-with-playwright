from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_to_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    target_item = "Sauce Labs Backpack"
    inventory.add_item_by_name(target_item)
    assert inventory.get_cart_count() == 1

    inventory.go_to_cart()
    cart = CartPage(logged_in_page)
    assert target_item in cart.get_item_names()
