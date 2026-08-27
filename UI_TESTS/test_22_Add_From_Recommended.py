import pytest
import allure

def test_add_to_cart_from_recommended(home_page, cart_page):
    with allure.step("1-2. Launch browser. Navigate to url 'http://automationexercise.com'."):
        home_page.open_home()
        home_page.verify_logo_visible()

    with allure.step("3. Scroll to bottom of page."):
        home_page.scroll_to_recommended_items()

    with allure.step("4. Verify 'RECOMMENDED ITEMS' are visible."):
        home_page.verify_recommended_items_visible()
        home_page.scroll_recommended_carousel_to_start()

    with allure.step("5. Click on 'Add To Cart' on Recommended product."):
        product_name = home_page.get_recommended_product_name(index=0)
        print(f"Adding product: {product_name}")
        home_page.add_recommended_product_to_cart(index=0)

    with allure.step("6-7. Click on 'View Cart' button (if applicable) and Verify that product is displayed in cart page."):
        cart_page.verify_recommended_product_in_cart(product_name)