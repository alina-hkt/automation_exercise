import pytest
import allure
from playwright.sync_api import APIRequestContext

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
@pytest.mark.regression
def test_post_to_search_product_without_parameter(request_context: APIRequestContext):
    ENDPOINT = "/api/searchProduct"
    
    with allure.step("1. Send POST request to /api/searchProduct without search parameter."):
        response = request_context.post(
            ENDPOINT,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=""
        )
        data = response.json()
        
    with allure.step("2. Verify HTTP Status Code is 200."):
        assert response.status == 200, f"Expected HTTP 200, but got {response.status}"
        
    with allure.step("3. Verify error code 400 in response body."):
        assert data.get("responseCode") == 400, \
            f"Expected responseCode 400 in body, but got {data.get('responseCode')}"
            
    with allure.step("4. Verify error message in response body."):
        expected_message = "Bad request, search_product parameter is missing in POST request."
        actual_message = data.get("message", "")
        assert actual_message == expected_message, \
            f"Expected message '{expected_message}', but got '{actual_message}'"