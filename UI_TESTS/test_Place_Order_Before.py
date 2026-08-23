import pytest
import allure
import random

@pytest.mark.smoke
def test_place_order_register_before_checkout(home_page, signup_page, products_page,
                                               cart_page, checkout_page, 
                                               payment_page, account_deleted_page):
    
    unique_email = f"test_user_{random.randint(10000, 99999)}@automation.test"
    user_name = f"TestUser{random.randint(1000, 9999)}"

    with allure.step("1. Launch browser"):
        pass

    with allure.step("2. Navigate to url 'http://automationexercise.com'"):
        home_page.open_home()

    with allure.step("3. Verify that home page is visible successfully"):
        home_page.verify_logo_visible()

    with allure.step("4. Click 'Signup / Login' button"):
        home_page.click_login_signup()

    with allure.step("5. Fill all details in Signup and create account"):
        signup_page.fill_initial_signup(user_name, unique_email)
        signup_page.fill_account_details({
            "password": "SecurePass123!",
            "day": "15", "month": "June", "year": "1995",
            "first_name": "John", "last_name": "Doe",
            "company": "AutoTest Inc",
            "address1": "123 QA Street", "address2": "Suite 100",
            "country": "United States", "state": "California",
            "city": "San Francisco", "zipcode": "94102",
            "mobile": "4155551234"
        })
        signup_page.click_create_account()

    with allure.step("6. Verify 'ACCOUNT CREATED!' and click 'Continue' button"):
        signup_page.verify_account_created()
        signup_page.click_continue_after_creation()

    with allure.step("7. Verify ' Logged in as username' at top"):
        home_page.verify_logged_in(user_name)

    with allure.step("8. Add products to cart"):
        home_page.click_products()
        products_page.add_first_product_to_cart()
        products_page.click_continue_shopping()

    with allure.step("9. Click 'Cart' button"):
        home_page.click_cart()

    with allure.step("10. Verify that cart page is displayed"):
        cart_page.verify_cart_loaded()

    with allure.step("11. Click Proceed To Checkout"):
        checkout_page.click_proceed_to_checkout()

    with allure.step("12. Verify Address Details and Review Your Order"):
        checkout_page.verify_addresses_and_review()

    with allure.step("13. Enter description in comment text area and click 'Place Order'"):
        checkout_page.fill_comment_and_place_order("Please deliver before Friday!")

    with allure.step("14. Enter payment details: Name on Card, Card Number, CVC, Expiration date"):
        payment_page.fill_payment_details()

    with allure.step("15. Click 'Pay and Confirm Order' button"):
        payment_page.click_pay_and_confirm()

    with allure.step("16. Verify success message 'Your order has been placed successfully!'"):
        payment_page.verify_order_success_and_continue()

    with allure.step("17. Click 'Delete Account' button"):
        home_page.click_delete_account()

    with allure.step("18. Verify 'ACCOUNT DELETED!' and click 'Continue' button"):
        account_deleted_page.verify_account_deleted()