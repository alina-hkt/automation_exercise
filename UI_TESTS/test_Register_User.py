import pytest
import time
import allure
from config import Config

@pytest.mark.smoke
def test_Register_User(home_page, register_page, account_deleted_page):
    config = Config()
    username = "ALINA"
    dynamic_email = f"alina_{int(time.time())}@test.com"
    
    with allure.step("1-3. Launch browser. Navigate to url 'http://automationexercise.com'. Verify that home page is visible successfully."):
        home_page.open_home()
        home_page.verify_logo_visible()

    with allure.step("4. Click on 'Signup / Login' button."):
        home_page.click_login_signup()

    with allure.step("5. Verify 'New User Signup!' is visible."):
        register_page.verify_new_user_signup_visible()

    with allure.step("6. Enter name and email address."):
        register_page.fill_name(username)
        register_page.fill_email(dynamic_email)

    with allure.step("7. Click 'Signup' button."):
        register_page.click_signup()

    with allure.step("8-12. Verify that 'ENTER ACCOUNT INFORMATION' is visible. Fill details: Title, Name, Email, Password, Date of birth. Select checkbox 'Sign up for our newsletter!'. Select checkbox 'Receive special offers from our partners!'. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number."):
        register_page.select_title_mrs()
        register_page.fill_password(config.TEST_USER_PASSWORD)
        register_page.set_date_of_birth(day="16", month="9", year="2004")
        register_page.check_newsletter()
        
        register_page.fill_address_details(
            first_name=username, last_name="TestUser", company="QA Corp",
            address1="123 Test St", address2="Apt 1", country="United States",
            state="California", city="Los Angeles", zipcode="90001", mobile="1234567890"
        )

    with allure.step("13. Click 'Create Account button'."):
        register_page.click_create_account()

    with allure.step("14. Verify that 'ACCOUNT CREATED!' is visible."):
        register_page.verify_account_created()

    with allure.step("15. Click 'Continue' button."):
        register_page.click_continue()

    with allure.step("16. Verify that 'Logged in as username' is visible."):
        home_page.verify_logged_in(username)

    with allure.step("17. Click 'Delete Account' button."):
        home_page.click_delete_account()

    with allure.step("18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button."):
        account_deleted_page.verify_heading_visible()
        account_deleted_page.click_continue()