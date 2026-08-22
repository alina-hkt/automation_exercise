import pytest
import allure

@pytest.mark.smoke
def test_add_products_to_cart(home_page, products_page, cart_page):
    
    with allure.step("1. Launch browser"):
        pass

    with allure.step("2. Navigate to url 'http://automationexercise.com'"):
        home_page.open_home()

    with allure.step("3. Verify that home page is visible successfully"):
        home_page.verify_logo_visible()

    with allure.step("4. Click 'Products' button"):
        home_page.click_products()

    with allure.step("5. Hover over first product and click 'Add to cart'"):
        products_page.add_first_product_to_cart()

    with allure.step("6. Click 'Continue Shopping' button"):
        products_page.click_continue_shopping()

    with allure.step("7. Hover over second product and click 'Add to cart'"):
        products_page.add_second_product_to_cart()

    with allure.step("8. Click 'View Cart' button"):
        products_page.click_view_cart()

    with allure.step("9. Verify both products are added to Cart"):
        cart_page.verify_cart_loaded()
        cart_page.verify_products_in_cart()

    with allure.step("10. Verify their prices, quantity and total price"):
        cart_page.verify_prices_and_quantity()