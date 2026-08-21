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
    
    with allure.step("1-3. Launch browser. Navigate to url 'http://automationexercise.com'. Verify that home page is visible successfully."):
        home_page.open_home()
        home_page.verify_logo_visible()

    with allure.step("4-5. Click on 'Signup / Login' button. Verify 'Login to your account' is visible."):
        home_page.click_login_signup()
        login_page.wait_for_login_form()

    with allure.step("6-8. Enter correct email address and password. Click 'login' button. Verify that 'Logged in as username' is visible."):
        login_page.fill_email(dynamic_email)
        login_page.fill_password(config.TEST_USER_PASSWORD)
        login_page.click_login()
        login_page.verify_logged_in(username)

    with allure.step("9. Click 'Delete Account' button."):
        login_page.click_delete_account()

    with allure.step("10. Verify that 'ACCOUNT DELETED!' is visible."):
        account_deleted_page.verify_heading_visible()
        account_deleted_page.click_continue()