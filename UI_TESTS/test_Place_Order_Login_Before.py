import pytest
import allure
from config import Config


@pytest.mark.smoke
def test_place_order_login_before_checkout(home_page, login_page, products_page,
                                            cart_page, checkout_page, 
                                            payment_page, account_deleted_page):
    
    config = Config()
    
    with allure.step("1-3. Launch browser. Navigate to url. Verify home page visible"):
        home_page.open_home()
        home_page.verify_logo_visible()

    with allure.step("4. Click 'Signup / Login' button"):
        home_page.click_login_signup()

    with allure.step("5. Fill email, password and click 'Login' button"):
        login_page.fill_login_form(config.TEST_USER_EMAIL, config.TEST_USER_PASSWORD)

    with allure.step("6. Verify 'Logged in as username' at top"):
        home_page.verify_logged_in(config.NAME) 

    with allure.step("7. Add products to cart"):
        home_page.click_products()
        products_page.add_first_product_to_cart()
        products_page.click_continue_shopping()

    with allure.step("8-9. Click 'Cart' button and verify cart page is displayed"):
        home_page.click_cart()
        cart_page.verify_cart_loaded()

    with allure.step("10. Click Proceed To Checkout"):
        checkout_page.click_proceed_to_checkout()

    with allure.step("11. Verify Address Details and Review Your Order"):
        checkout_page.verify_addresses_and_review()

    with allure.step("12. Enter description in comment text area and click 'Place Order'"):
        checkout_page.fill_comment_and_place_order("Login before checkout test order")

    with allure.step("13-14. Enter payment details and click 'Pay and Confirm Order'"):
        payment_page.fill_payment_details()
        payment_page.click_pay_and_confirm()

    with allure.step("15. Verify success message 'Your order has been placed successfully!'"):
        payment_page.verify_order_success_and_continue()

    with allure.step("16. Click 'Delete Account' button"):
        home_page.click_delete_account()

    with allure.step("17. Verify 'ACCOUNT DELETED!' and click 'Continue' button"):
        account_deleted_page.verify_heading_visible()
        account_deleted_page.click_continue()