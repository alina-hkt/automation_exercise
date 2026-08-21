import pytest
import allure

@pytest.mark.smoke
def test_login_user_with_incorrect_credentials(home_page, login_page):
    
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
        
    with allure.step("6. Enter incorrect email address and password."):
        login_page.fill_email("wrong_email@example.com")
        login_page.fill_password("WrongPassword")
        
    with allure.step("7. Click 'login' button."):
        login_page.click_login()
        
    with allure.step("8. Verify error 'Your email or password is incorrect!' is visible."):
        login_page.verify_error_visible()