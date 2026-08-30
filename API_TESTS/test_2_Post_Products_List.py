import allure
import pytest
from playwright.sync_api import APIRequestContext


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
@pytest.mark.regression
def test_post_to_products_list_not_allowed(request_context: APIRequestContext):
    ENDPOINT = "/api/productsList"

    with allure.step("1. Send POST request to /api/productsList."):
        response = request_context.post(ENDPOINT)
        data = response.json()

    with allure.step("2. Verify HTTP Status Code is 200."):
        assert response.status == 200, f"Expected HTTP 200, but got {response.status}"

    with allure.step("3. Verify error code 405 in response body."):
        assert data.get("responseCode") == 405, f"Expected responseCode 405 in body, but got {data.get('responseCode')}"

    with allure.step("4. Verify error message in response body."):
        expected_message = "This request method is not supported."
        actual_message = data.get("message", "")
        assert actual_message == expected_message, f"Expected message '{expected_message}', but got '{actual_message}'"
