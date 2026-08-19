import pytest
import allure

@pytest.mark.smoke
def test_login_user_with_incorrect_credentials(home_page, login_page):
    
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
        
    with allure.step("6. Ввести неверный email и пароль"):
        login_page.fill_email("wrong_email@example.com")
        login_page.fill_password("WrongPassword")
        
    with allure.step("7. Нажать кнопку 'login'"):
        login_page.click_login()
        
    with allure.step("8. Убедиться, что ошибка 'Your email or password is incorrect!' видна"):
        login_page.verify_error_visible()