import pytest
import allure
from config import Config

@pytest.mark.smoke
def test_register_user_with_existing_email(home_page, register_page):
    config = Config()

    with allure.step("1. Запустить браузер"):
        pass
        
    with allure.step("2. Перейти на URL 'http://automationexercise.com'"):
        home_page.open_home()
        
    with allure.step("3. Убедиться, что главная страница отображается успешно"):
        home_page.verify_logo_visible()
        
    with allure.step("4. Нажать кнопку 'Signup / Login'"):
        home_page.click_login_signup()
        
    with allure.step("5. Убедиться, что форма 'New User Signup!' видна"):
        register_page.verify_new_user_signup_visible()
        
    with allure.step("6. Ввести имя и УЖЕ СУЩЕСТВУЮЩИЙ email"):
        register_page.fill_name(config.NAME)
        register_page.fill_email(config.TEST_USER_EMAIL)
        
    with allure.step("7. Нажать кнопку 'Signup'"):
        register_page.click_signup()
        
    with allure.step("8. Убедиться, что ошибка 'Email Address already exist!' видна"):
        register_page.verify_error_visible()