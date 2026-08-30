import allure

from config import Config


def test_verify_all_products_and_detail(home_page, products_page, product_detail_page):
    Config()

    with allure.step("1. Launch browser."):
        pass

    with allure.step("2. Navigate to url 'http://automationexercise.com'."):
        home_page.open_home()

    with allure.step("3. Verify that home page is visible successfully."):
        home_page.verify_logo_visible()

    with allure.step("4. Click on 'Products' button."):
        home_page.click_products()

    with allure.step("5. Verify user is navigated to ALL PRODUCTS page successfully."):
        products_page.verify_products_list_visible()

    with allure.step("6. The products list is visible."):
        pass

    with allure.step("7. Click on 'View Product' of first product."):
        products_page.click_first_view_product()

    with allure.step("8. User is landed to product detail page."):
        product_detail_page.wait_for_visible(product_detail_page.product_name)

    with allure.step(
        "9. Verify that detail detail is visible: product name, category, price, availability, condition, brand."
    ):
        product_detail_page.verify_details_visible()
