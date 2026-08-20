import pytest
import allure
from config import Config

@pytest.mark.smoke
def test_logout_user(home_page, login_page):
    config = Config()
    
    with allure.step("1. Запустить браузер"):
        pass
        
    with allure.step("2. Перейти на URL 'http://automationexercise.com'"):
        home_page.open_home()
        
    with allure.step("3. Убедиться, что главная страница отображается успешно"):
        home_page.verify_logo_visible()
        
    with allure.step("4. Нажать кнопку 'Signup / Login'"):
        home_page.click_login_signup()
        
    with allure.step("5. Убедиться, что форма 'Login to your account' видна"):
        login_page.wait_for_login_form()
        
    with allure.step("6. Ввести корректный email и пароль"):
        login_page.fill_email(config.TEST_USER_EMAIL)
        login_page.fill_password(config.TEST_USER_PASSWORD)
        
    with allure.step("7. Нажать кнопку 'login'"):
        login_page.click_login()
        
    with allure.step("8. Убедиться, что 'Logged in as username' виден"):
        login_page.verify_logged_in()
        
    with allure.step("9. Нажать кнопку 'Logout'"):
        login_page.click_logout()
        
    with allure.step("10. Убедиться, что пользователь перенаправлен на страницу входа"):
        login_page.verify_returned_to_login_page()