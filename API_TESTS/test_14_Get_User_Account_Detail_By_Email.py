import allure
import pytest
from playwright.sync_api import Page

from config import Config


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
@pytest.mark.regression
def test_get_user_account_detail_by_email(page: Page):
    config = Config()
    ENDPOINT = "/api/getUserDetailByEmail"

    test_email = config.TEST_USER_EMAIL
    FULL_URL = f"{config.BASE_URL}{ENDPOINT}"

    with allure.step(f"1. Send GET request to {FULL_URL} for existing user."):
        response = page.request.get(FULL_URL, params={"email": test_email})
        data = response.json()

    with allure.step("2. Verify HTTP Status Code is 200."):
        assert response.status == 200, f"Expected HTTP 200, but got {response.status}"

    with allure.step("3. Verify response code in body is 200."):
        assert data.get("responseCode") == 200, f"Expected responseCode 200 in body, but got {data.get('responseCode')}"

    with allure.step("4. Verify user details match config email."):
        target_user = data.get("user")
        assert target_user is not None, f"Expected 'user' object in response, but got keys: {list(data.keys())}"
        actual_email = target_user.get("email")
        assert actual_email == test_email, f"Expected email '{test_email}', but got '{actual_email}'"
        assert "name" in target_user, "Expected 'name' field in user details"
        assert "email" in target_user, "Expected 'email' field in user details"
