import pytest
import allure
from config import Config

@pytest.mark.smoke
def test_Login_User_Correct(home_page, login_page, account_deleted_page):
    config = Config()
    
    with allure.step("Шаги 1-2: Открыть главную страницу и проверить загрузку"):
        home_page.open_home()
        home_page.verify_logo_visible()

    with allure.step("Шаг 3: Перейти на форму авторизации"):
        home_page.click_login_signup()
        login_page.wait_for_login_form()

    with allure.step("Шаги 4-5: Ввести корректные учетные данные"):
        login_page.fill_email(config.TEST_USER_EMAIL)
        login_page.fill_password(config.TEST_USER_PASSWORD)

    with allure.step("Шаг 6: Нажать кнопку 'Login'"):
        login_page.click_login()

    with allure.step("Шаг 7: Проверить успешную авторизацию"):
        login_page.verify_logged_in()

    with allure.step("Шаг 8: Удалить аккаунт (очистка после теста)"):
        login_page.click_delete_account()

    with allure.step("Шаг 9: Подтвердить удаление и завершить сценарий"):
        account_deleted_page.verify_heading_visible()
        account_deleted_page.click_continue()