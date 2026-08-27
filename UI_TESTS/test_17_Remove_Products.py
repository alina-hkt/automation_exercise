import pytest
import allure
from config import Config

def test_Remove_Products_From_Cart(home_page, products_page, cart_page):
    config = Config()

    with allure.step("1. Launch browser."):
        pass
    
    with allure.step("2. Navigate to url 'http://automationexercise.com'."):
        home_page.open_home()

    with allure.step("3. Verify that home page is visible successfully."):
        home_page.verify_logo_visible()

    with allure.step("4. Add products to cart."):
        home_page.click_products()
        products_page.verify_products_list_visible()
        products_page.add_first_product_to_cart()
        products_page.click_continue_shopping()

    with allure.step("5. Click 'Cart' button."):
        home_page.open_home() 
        home_page.click_cart()

    with allure.step("6. Verify that cart page is displayed."):
        cart_page.verify_cart_loaded()

    with allure.step("7. Click 'X' button corresponding to particular product."):
        cart_page.click_delete_first_product()

    with allure.step("8. Verify that product is removed from the cart."):
        cart_page.verify_cart_is_empty()