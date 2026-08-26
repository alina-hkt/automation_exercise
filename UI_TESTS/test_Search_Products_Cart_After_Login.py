import pytest
import time
import allure
from config import Config

@pytest.mark.smoke
def test_Search_Products_Cart_After_Login(home_page, account_deleted_page, login_page, products_page, cart_page, register_page):
    config = Config()
    username = "ALINA_SEARCH"
    dynamic_email = f"alina_search_{int(time.time())}@test.com"
    search_term = "Top"

    home_page.open_home()
    home_page.verify_logo_visible()
    home_page.click_login_signup()
    register_page.verify_new_user_signup_visible()
    register_page.fill_name(username)
    register_page.fill_email(dynamic_email)
    register_page.click_signup()
    register_page.select_title_mrs()
    register_page.fill_password(config.TEST_USER_PASSWORD)
    register_page.set_date_of_birth(day="16", month="9", year="2004")
    register_page.check_newsletter()
    register_page.fill_address_details(
                first_name=username, last_name="TestUser", company="QA Corp",
                address1="123 Test St", address2="Apt 1", country="United States",
                state="California", city="Los Angeles", zipcode="90001", mobile="1234567890"
            )
    
    register_page.click_create_account()
    register_page.verify_account_created()
    register_page.click_continue()
    home_page.verify_logged_in(username)
    login_page.click_logout()
    login_page.verify_returned_to_login_page()

    with allure.step("1. Launch browser."):
        home_page.open_home()

    with allure.step("2. Navigate to url 'http://automationexercise.com'.."):
        home_page.verify_logo_visible()

    with allure.step("3. Click on 'Products' button."):
        home_page.click_products()

    with allure.step("4. Verify user is navigated to ALL PRODUCTS page successfully."):
        products_page.verify_products_list_visible()

    with allure.step("5. Enter product name in search input and click search button."):
        products_page.search_product(search_term)

    with allure.step("6. Verify 'SEARCHED PRODUCTS' is visible."):
        products_page.verify_search_results_visible()

    with allure.step("7. Verify all the products related to search are visible."):
        products_page.verify_all_searched_products_are_visible()

    with allure.step("8. Add those products to cart."):
        products_page.add_all_searched_products_to_cart()

    with allure.step("9. Click 'Cart' button and verify that products are visible in cart."):
        home_page.click_cart()
        cart_page.verify_searched_products_in_cart()

    with allure.step("10. Click 'Signup / Login' button and submit login details."):
        home_page.open_home()
        home_page.verify_logo_visible()
        home_page.click_login_signup()
        login_page.wait_for_login_form()
        login_page.fill_email(dynamic_email)
        login_page.fill_password(config.TEST_USER_PASSWORD)
        login_page.click_login()
   
    with allure.step("11. Again, go to Cart page."):
        home_page.click_cart()

    with allure.step("12. Verify that those products are visible in cart after login as well."):
        cart_page.verify_searched_products_in_cart()
        home_page.click_delete_account()
        account_deleted_page.verify_heading_visible()
        account_deleted_page.click_continue()