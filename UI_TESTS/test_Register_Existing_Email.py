import pytest
import allure
from config import Config

@pytest.mark.smoke
def test_register_user_with_existing_email(home_page, register_page):
    config = Config()

    with allure.step("1. Launch browser."):
        pass
        
    with allure.step("2. Navigate to url 'http://automationexercise.com'."):
        home_page.open_home()
        
    with allure.step("3. Verify that home page is visible successfully."):
        home_page.verify_logo_visible()
        
    with allure.step("4. Click on 'Signup / Login' button."):
        home_page.click_login_signup()
        
    with allure.step("5. Verify 'New User Signup!' is visible."):
        register_page.verify_new_user_signup_visible()
        
    with allure.step("6. Enter name and already registered email address."):
        register_page.fill_name(config.NAME)
        register_page.fill_email(config.TEST_USER_EMAIL)
        
    with allure.step("7. Click 'Signup' button."):
        register_page.click_signup()
        
    with allure.step("8. Verify error 'Email Address already exist!' is visible."):
        register_page.verify_error_visible()