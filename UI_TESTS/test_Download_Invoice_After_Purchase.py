import pytest
import time
import allure
from config import Config

@pytest.mark.smoke
def test_verify_address_in_checkout(home_page, account_deleted_page, products_page, cart_page,
                                     signup_page, payment_page, register_page, checkout_page):

    config = Config()
    username = "ALINA_SEARCH"
    dynamic_email = f"alina_search_{int(time.time())}@test.com"

    with allure.step("1. Launch browser."):
        home_page.open_home()

    with allure.step("2. Navigate to url 'http://automationexercise.com'."):
        home_page.verify_logo_visible()

    with allure.step("3. Verify that home page is visible successfully."):
        home_page.get_page_title()

    with allure.step("4. Add products to cart."):
        home_page.click_products()
        products_page.verify_products_list_visible()
        products_page.add_first_product_to_cart()
        products_page.click_continue_shopping()
        products_page.add_second_product_to_cart()
        products_page.click_continue_shopping()

    with allure.step("5. Click 'Cart' button."):
        home_page.click_cart()

    with allure.step("6. Verify that cart page is displayed."):
        cart_page.verify_cart_loaded()

    with allure.step("7. Click Proceed To Checkout."):
        cart_page.click_proceed_to_checkout()

    with allure.step("8. Click 'Register / Login' button."):
        checkout_page.click_register_login()

    with allure.step("9. Fill all details in Signup and create account."):
        register_page.verify_new_user_signup_visible()
        register_page.fill_name(username)
        register_page.fill_email(dynamic_email)
        register_page.click_signup()
        register_page.select_title_mrs()
        register_page.fill_password(config.TEST_USER_PASSWORD)
        register_page.set_date_of_birth(day="16", month="9", year="2004")
        register_page.check_newsletter()
        
        first_name = username
        last_name = "TestUser"
        address1 = "123 Test St"
        city = "Los Angeles"
        state = "California"
        zipcode = "90001"
        mobile = "1234567890"
        full_name = f"{first_name} {last_name}"
        
        register_page.fill_address_details(
            first_name=first_name, 
            last_name=last_name, 
            company="QA Corp",
            address1=address1, 
            address2="Apt 1", 
            country="United States",
            state=state, 
            city=city, 
            zipcode=zipcode, 
            mobile=mobile
        )
        register_page.click_create_account()

    with allure.step("10. Verify 'ACCOUNT CREATED!' and click 'Continue' button."):
        register_page.verify_account_created()
        register_page.click_continue()

    with allure.step("11. Verify ' Logged in as username' at top."):
        home_page.verify_logged_in(username)

    with allure.step("12.Click 'Cart' button."):
        home_page.click_cart()

    with allure.step("13. Click 'Proceed To Checkout' button."):
        cart_page.click_proceed_to_checkout()

    with allure.step("14. Verify Address Details and Review Your Order."):
        checkout_page.verify_address_matches(
            expected_name=full_name,
            expected_address=address1,
            expected_city=city,
            expected_state=state,
            expected_zip=zipcode,
            expected_mobile=mobile
        )

    with allure.step("15. Enter description in comment text area and click 'Place Order'."):
        checkout_page.fill_comment_and_place_order(comment="Test order comment")

    with allure.step("16. Enter payment details: Name on Card, Card Number, CVC, Expiration date."):
        payment_page.fill_payment_details(
            name=full_name,
            card="4111111111111111",
            cvc="123",
            month="12",
            year="2030"
        )
            
    with allure.step("17. Click 'Pay and Confirm Order' button."):
        payment_page.click_pay_and_confirm()

    with allure.step("18. Verify success message 'Your order has been placed successfully!'."):
        checkout_page.verify_order_placed_successfully()
                    
    with allure.step("19. Click 'Download Invoice' button and verify invoice is downloaded successfully.."):
        checkout_page.download_invoice()   

    with allure.step("20. Click 'Continue' button."):
        checkout_page.click_continue_after_order()
                            
    with allure.step("21. Click 'Delete Account' button."):
        home_page.click_delete_account()

    with allure.step("22. Verify 'ACCOUNT DELETED!' and click 'Continue' button."):
        account_deleted_page.verify_heading_visible()
        account_deleted_page.click_continue()