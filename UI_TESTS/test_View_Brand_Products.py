import pytest
import allure
from config import Config

@pytest.mark.smoke
def test_view_brand_products(home_page, products_page, sidebar):
    config = Config()

    with allure.step("1. Launch browser."):
        pass

    with allure.step("2. Navigate to url 'http://automationexercise.com'."):
        home_page.open_home()

    with allure.step("3. Click on 'Products' button."):
        home_page.click_products()
        products_page.verify_products_list_visible()

    with allure.step("4. Verify that Brands are visible on left side bar."):
        sidebar.verify_brands_visible()

    with allure.step("5. Click on any brand name."):
        with home_page.page.expect_navigation(wait_until="domcontentloaded", timeout=config.SHORT_TIMEOUT):
            sidebar.click_brand(sidebar.polo_brand_link)

    with allure.step("6. Verify that user is navigated to brand page and brand products are displayed."):
        assert "/brand_products/Polo" in home_page.page.url, \
            f"Expected /brand_products/Polo, got {home_page.page.url}"
        sidebar.verify_brand_page(sidebar.polo_brand_page_heading)

    with allure.step("7. On left side bar, click on any other brand link."):
        with home_page.page.expect_navigation(wait_until="domcontentloaded", timeout=config.SHORT_TIMEOUT):
            sidebar.click_brand(sidebar.madame_brand_link)

    with allure.step("8. Verify that user is navigated to that brand page and can see products."):
        assert "/brand_products/Madame" in home_page.page.url, \
            f"Expected /brand_products/Madame, got {home_page.page.url}"
        sidebar.verify_brand_page(sidebar.madame_brand_page_heading)