import allure
import pytest
from playwright.sync_api import APIRequestContext

from config import Config


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
@pytest.mark.regression
def test_post_verify_login_without_email(request_context: APIRequestContext):
    ENDPOINT = "/api/verifyLogin"

    with allure.step("1. Send POST request to /api/verifyLogin without email parameter."):
        response = request_context.post(
            ENDPOINT,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=f"password={Config.TEST_USER_PASSWORD}",
        )
        data = response.json()

    with allure.step("2. Verify HTTP Status Code is 200."):
        assert response.status == 200, f"Expected HTTP 200, but got {response.status}"

    with allure.step("3. Verify error code 400 in response body."):
        assert data.get("responseCode") == 400, f"Expected responseCode 400 in body, but got {data.get('responseCode')}"

    with allure.step("4. Verify error message in response body."):
        expected_message = "Bad request, email or password parameter is missing in POST request."
        actual_message = data.get("message", "")
        assert actual_message == expected_message, f"Expected message '{expected_message}', but got '{actual_message}'"
