from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_process(logged_in_page):
    # Step 1: Add item to cart
    inventory = InventoryPage(logged_in_page)
    target_item = "Sauce Labs Backpack"
    inventory.add_item_by_name(target_item)
    assert inventory.get_cart_count() == 1

    # Step 2: Go to cart
    inventory.go_to_cart()
    cart = CartPage(logged_in_page)
    items = cart.get_item_names()
    assert target_item in items

    # Step 3: Start checkout
    checkout = CheckoutPage(logged_in_page)
    checkout.start_checkout()

    # Step 4: Fill user information
    checkout.fill_information("John", "Doe", "12345")

    # Step 5: Finish order
    checkout.finish_checkout()

    # Step 6: Verify success message
    success = checkout.get_success_message()
    assert "Thank you for your order!" in success
