import allure
import pytest
from playwright.sync_api import APIRequestContext

from config import Config


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
@pytest.mark.regression
def test_post_verify_login_valid_details(request_context: APIRequestContext):
    ENDPOINT = "/api/verifyLogin"

    with allure.step("1. Send POST request to /api/verifyLogin with valid credentials."):
        response = request_context.post(
            ENDPOINT,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=f"email={Config.TEST_USER_EMAIL}&password={Config.TEST_USER_PASSWORD}",
        )
        data = response.json()

    with allure.step("2. Verify HTTP Status Code is 200."):
        assert response.status == 200, f"Expected HTTP 200, but got {response.status}"

    with allure.step("3. Verify success message in response body."):
        expected_message = "User exists!"
        actual_message = data.get("message", "")
        assert actual_message == expected_message, f"Expected message '{expected_message}', but got '{actual_message}'"

    with allure.step("4. Verify response code in body is 200."):
        assert data.get("responseCode") == 200, f"Expected responseCode 200 in body, but got {data.get('responseCode')}"
