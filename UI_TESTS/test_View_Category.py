import pytest
import allure

@pytest.mark.smoke
def test_view_category_products(home_page, sidebar):
    with allure.step("1-2. Launch browser and Navigate to url"):
        home_page.open_home()
        home_page.verify_logo_visible()

    with allure.step("3. Verify that categories are visible on left side bar"):
        sidebar.verify_categories_visible()

    with allure.step("4-5. Click on 'Women' category and click on 'Dress' sub-category"):
        sidebar.expand_and_click_women_subcategory()

    with allure.step("6. Verify that category page is displayed and confirm text 'WOMEN - DRESS PRODUCTS'"):
        sidebar.verify_women_dress_page()

    with allure.step("7. On left side bar, click on any sub-category link of 'Men' category"):
        sidebar.expand_and_click_men_subcategory()

    with allure.step("8. Verify that user is navigated to that category page"):
        sidebar.verify_men_tshirts_page()