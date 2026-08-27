import pytest
import allure
from config import Config

def test_verify_subscription_in_cart(home_page):
    
    config = Config()
    
    with allure.step("1. Launch browser."):
        pass

    with allure.step("2. Navigate to url 'http://automationexercise.com'."):
        home_page.open_home()

    with allure.step("3. Verify that home page is visible successfully."):
        home_page.verify_logo_visible()

    with allure.step("4. Click 'Cart' button."):
        home_page.click_cart()

    with allure.step("5. Scroll down to footer."):
        home_page.scroll_to_footer()

    with allure.step("6. Verify text 'SUBSCRIPTION'."):
        home_page.verify_subscription_heading_visible()

    with allure.step("7. Enter email address in input and click arrow button."):
        home_page.subscribe(config.TEST_USER_EMAIL)

    with allure.step("8. Verify success message 'You have been successfully subscribed!' is visible."):
        home_page.verify_success_message()