import pytest
import allure

@pytest.mark.smoke
def test_search_product(home_page, products_page):
    
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

    with allure.step("6. Enter product name in search input and click search button."):
        products_page.search_product("T-Shirt")

    with allure.step("7. Verify 'SEARCHED PRODUCTS' is visible."):
        products_page.verify_search_results_visible()
        
    with allure.step("8. Verify all the products related to search are visible."):
        pass