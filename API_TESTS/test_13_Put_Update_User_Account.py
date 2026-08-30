import time
from urllib.parse import urlencode

import allure
import pytest
from playwright.sync_api import APIRequestContext

from config import Config


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
@pytest.mark.regression
def test_put_update_user_account(request_context: APIRequestContext):
    config = Config()
    ENDPOINT = "/api/updateAccount"
    test_email = f"testuser_upd_{int(time.time())}@example.com"
    original_name = "OriginalUser"
    updated_name = "UpdatedUser"
    create_data = {
        "name": original_name,
        "email": test_email,
        "password": config.TEST_USER_PASSWORD,
        "title": "Mr",
        "birth_date": "01",
        "birth_month": "01",
        "birth_year": "2000",
        "firstname": "Original",
        "lastname": "User",
        "company": "Test Co",
        "address1": "1 Test St",
        "address2": "",
        "country": "United States",
        "zipcode": "00000",
        "state": "New York",
        "city": "New York",
        "mobile_number": "0000000000",
    }

    with allure.step("1. Create a test user via POST /api/createAccount to be updated."):
        request_context.post(
            "/api/createAccount",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=urlencode(create_data),
        )

    update_data = {
        "name": updated_name,
        "email": test_email,
        "password": config.TEST_USER_PASSWORD,
        "title": "Mrs",
        "birth_date": "15",
        "birth_month": "8",
        "birth_year": "1995",
        "firstname": "Updated",
        "lastname": "Person",
        "company": "Updated Corp",
        "address1": "456 New Ave",
        "address2": "Suite 100",
        "country": "Canada",
        "zipcode": "M5V 3A8",
        "state": "Ontario",
        "city": "Toronto",
        "mobile_number": "1112223333",
    }

    with allure.step("2. Send PUT request to /api/updateAccount with new data."):
        response = request_context.put(
            ENDPOINT, headers={"Content-Type": "application/x-www-form-urlencoded"}, data=urlencode(update_data)
        )
        data = response.json()

    with allure.step("3. Verify HTTP Status Code is 200."):
        assert response.status == 200, f"Expected HTTP 200, but got {response.status}"

    with allure.step("4. Verify response code in body is 200."):
        assert data.get("responseCode") == 200, f"Expected responseCode 200 in body, but got {data.get('responseCode')}"

    with allure.step("5. Verify success message 'User updated!' in response body."):
        expected_message = "User updated!"
        actual_message = data.get("message", "")
        assert actual_message == expected_message, f"Expected message '{expected_message}', but got '{actual_message}'"

    with allure.step("6. Delete updated account via POST /api/deleteAccount for cleanup."):
        delete_payload = {"email": test_email, "password": config.TEST_USER_PASSWORD}
        request_context.post(
            "/api/deleteAccount",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=urlencode(delete_payload),
        )
