import pytest
import allure

@pytest.mark.smoke
def test_verify_product_quantity_in_cart(home_page, product_detail_page, cart_page):
    with allure.step("1. Launch browser."):
        pass

    with allure.step("2. Navigate to url 'http://automationexercise.com'."):
        home_page.open_home()

    with allure.step("3. Verify that home page is visible successfully."):
        home_page.verify_logo_visible()

    with allure.step("4. Click 'View Product' for any product on home page."):
        home_page.click_first_view_product_on_home()

    with allure.step("5. Verify product detail is opened."):
        product_detail_page.verify_product_detail_opened()

    with allure.step("6. Increase quantity to 4."):
        product_detail_page.set_quantity(4)

    with allure.step("7. Click 'Add to cart' button."):
        product_detail_page.click_add_to_cart()

    with allure.step("8. Click 'View Cart' button."):
        product_detail_page.click_view_cart()

    with allure.step("9. Verify that product is displayed in cart page with exact quantity."):
        cart_page.verify_cart_loaded()
        cart_page.verify_product_quantity("4")