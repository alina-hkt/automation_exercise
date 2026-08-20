import pytest
import time
import allure
from config import Config

@pytest.mark.smoke
def test_Register_User(home_page, register_page, account_deleted_page):
    config = Config()
    username = "ALINA"
    dynamic_email = f"alina_{int(time.time())}@test.com"
    
    with allure.step("Шаги 1-3: Открыть браузер, перейти на сайт, проверить главную"):
        home_page.open_home()
        home_page.verify_logo_visible()

    with allure.step("Шаг 4: Кликнуть 'Signup / Login'"):
        home_page.click_login_signup()

    with allure.step("Шаг 5: Проверить, что видна надпись 'New User Signup!'"):
        register_page.verify_new_user_signup_visible()

    with allure.step("Шаг 6: Ввести имя и динамический email"):
        register_page.fill_name(username)
        register_page.fill_email(dynamic_email)

    with allure.step("Шаг 7: Кликнуть 'Signup'"):
        register_page.click_signup()

    with allure.step("Шаги 8-12: Заполнить форму 'Enter Account Information'"):
        register_page.select_title_mrs()
        register_page.fill_password(config.TEST_USER_PASSWORD)
        register_page.set_date_of_birth(day="16", month="9", year="2004")
        register_page.check_newsletter()
        
        register_page.fill_address_details(
            first_name=username, last_name="TestUser", company="QA Corp",
            address1="123 Test St", address2="Apt 1", country="United States",
            state="California", city="Los Angeles", zipcode="90001", mobile="1234567890"
        )

    with allure.step("Шаг 13: Кликнуть 'Create Account'"):
        register_page.click_create_account()

    with allure.step("Шаг 14: Проверить, что аккаунт создан"):
        register_page.verify_account_created()

    with allure.step("Шаг 15: Кликнуть 'Continue'"):
        register_page.click_continue()

    with allure.step("Шаг 16: Проверить, что пользователь залогинен"):
        home_page.verify_logged_in(username)

    with allure.step("Шаг 17: Кликнуть 'Delete Account'"):
        home_page.click_delete_account()

    with allure.step("Шаг 18: Проверить удаление и кликнуть 'Continue'"):
        account_deleted_page.verify_heading_visible()
        account_deleted_page.click_continue()