import allure
import pytest
from playwright.sync_api import APIRequestContext


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
@pytest.mark.regression
def test_post_verify_login_invalid_details(request_context: APIRequestContext):
    ENDPOINT = "/api/verifyLogin"
    INVALID_EMAIL = "invalid@example.com"
    INVALID_PASSWORD = "wrongpassword"

    with allure.step("1. Send POST request to /api/verifyLogin with invalid credentials."):
        response = request_context.post(
            ENDPOINT,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=f"email={INVALID_EMAIL}&password={INVALID_PASSWORD}",
        )
        data = response.json()

    with allure.step("2. Verify HTTP Status Code is 200."):
        assert response.status == 200, f"Expected HTTP 200, but got {response.status}"

    with allure.step("3. Verify error code 404 in response body."):
        assert data.get("responseCode") == 404, f"Expected responseCode 404 in body, but got {data.get('responseCode')}"

    with allure.step("4. Verify error message in response body."):
        expected_message = "User not found!"
        actual_message = data.get("message", "")
        assert actual_message == expected_message, f"Expected message '{expected_message}', but got '{actual_message}'"
