import pytest
import time
import allure
from playwright.sync_api import APIRequestContext
from config import Config
from urllib.parse import urlencode

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.hybrid
def test_post_create_user_account_via_api_and_cleanup(
    home_page, login_page, account_deleted_page, request_context: APIRequestContext
):
    config = Config()
    username = "TestUser"
    dynamic_email = f"testuser_api_{int(time.time())}@example.com"

    ENDPOINT = "/api/createAccount"
    user_data = {
        "name": username,
        "email": dynamic_email,
        "password": config.TEST_USER_PASSWORD,
        "title": "Mrs",
        "birth_date": "15",
        "birth_month": "8",
        "birth_year": "1995",
        "firstname": username,
        "lastname": "User",
        "company": "Automation Co",
        "address1": "123 Test Street",
        "address2": "Apt 4B",
        "country": "United States",
        "zipcode": "10001",
        "state": "New York",
        "city": "New York",
        "mobile_number": "5551234567"
    }

    with allure.step("1. Send POST request to /api/createAccount with registration data."):
        response = request_context.post(
            ENDPOINT,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=urlencode(user_data)
        )
        data = response.json()

    with allure.step("2. Verify HTTP Status Code is 200."):
        assert response.status == 200, f"Expected HTTP 200, but got {response.status}"

    with allure.step("3. Verify response code in body is 201."):
        assert data.get("responseCode") == 201, \
            f"Expected responseCode 201 in body, but got {data.get('responseCode')}"

    with allure.step("4. Verify success message in response body."):
        expected_message = "User created!"
        actual_message = data.get("message", "")
        assert actual_message == expected_message, \
            f"Expected message '{expected_message}', but got '{actual_message}'"

    with allure.step("5. Login via UI to establish session for cleanup."):
        home_page.open_home()
        home_page.click_login_signup()
        login_page.fill_email(dynamic_email)
        login_page.fill_password(config.TEST_USER_PASSWORD)
        login_page.click_login()
        home_page.verify_logged_in(username)

    with allure.step("6. Delete created account via UI for cleanup."):
        home_page.click_delete_account()
        account_deleted_page.verify_heading_visible()
        account_deleted_page.click_continue()