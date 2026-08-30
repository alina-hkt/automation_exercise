import random
import string

import allure


def test_add_review_on_product(home_page, products_page, product_details_page):

    with allure.step("1. Launch browser."):
        home_page.open_home()

    with allure.step("2. Navigate to url 'http://automationexercise.com'."):
        home_page.verify_logo_visible()

    with allure.step("3. Click on 'Products' button."):
        home_page.click_products()

    with allure.step("4. Verify user is navigated to ALL PRODUCTS page successfully."):
        products_page.verify_products_list_visible()

    with allure.step("5. Click on 'View Product' button."):
        products_page.click_view_product(index=0)

    with allure.step("6. Verify 'Write Your Review' is visible."):
        product_details_page.verify_write_review_visible()

    with allure.step("7. Enter name, email and review."):
        random_suffix = "".join(random.choices(string.digits, k=4))
        test_name = f"Test User {random_suffix}"
        test_email = f"testuser{random_suffix}@example.com"
        test_review = f"This is a great product! Review #{random_suffix}"

        product_details_page.fill_review_form(name=test_name, email=test_email, review=test_review)

    with allure.step("8. Click 'Submit' button."):
        product_details_page.submit_review()

    with allure.step("9. Verify success message 'Thank you for your review.'."):
        product_details_page.verify_success_message()
