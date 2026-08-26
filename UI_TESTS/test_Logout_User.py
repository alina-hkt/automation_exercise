import pytest
import time
import allure
from config import Config

@pytest.mark.smoke
def test_Login_User_Correct(home_page, register_page, login_page, account_deleted_page): 
    config = Config()
    username = "ALINA"
    dynamic_email = f"alina_{int(time.time())}@test.com"
        
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
        pass
        
    with allure.step("2. Navigate to url 'http://automationexercise.com'."):
        home_page.open_home()
        
    with allure.step("3. Verify that home page is visible successfully."):
        home_page.verify_logo_visible()
        
    with allure.step("4. Click on 'Signup / Login' button."):
        home_page.click_login_signup()
        
    with allure.step("5. Verify 'Login to your account' is visible."):
        login_page.wait_for_login_form()
        
    with allure.step("6. Enter correct email address and password."):
        login_page.fill_email(dynamic_email)
        login_page.fill_password(config.TEST_USER_PASSWORD)
        
    with allure.step("7. Click 'login' button."):
        login_page.click_login()
        
    with allure.step("8. Verify that 'Logged in as username' is visible."):
        login_page.verify_logged_in(username)
        
    with allure.step("9. Click 'Logout' button."):
        login_page.click_logout()
        
    with allure.step("10. Verify that user is navigated to login page."):
        login_page.verify_returned_to_login_page()
        home_page.click_login_signup()
        login_page.wait_for_login_form()
        login_page.fill_email(dynamic_email)
        login_page.fill_password(config.TEST_USER_PASSWORD)
        login_page.click_login()
        home_page.click_delete_account()
        account_deleted_page.verify_heading_visible()
        account_deleted_page.click_continue()