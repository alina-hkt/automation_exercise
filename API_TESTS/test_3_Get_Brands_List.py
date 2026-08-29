import pytest
import allure
from playwright.sync_api import APIRequestContext

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
@pytest.mark.regression
def test_get_all_brands_list(request_context: APIRequestContext):
    ENDPOINT = "/api/brandsList"
    
    with allure.step("1. Send GET request to /api/brandsList."):
        response = request_context.get(ENDPOINT)
        data = response.json()
        
    with allure.step("2. Verify HTTP Status Code is 200."):
        assert response.status == 200, f"Expected HTTP 200, but got {response.status}"
        
    with allure.step("3. Verify response code in body is 200."):
        assert data.get("responseCode") == 200, \
            f"Expected responseCode 200 in body, but got {data.get('responseCode')}"
            
    with allure.step("4. Verify brands list is present and not empty."):
        brands = data.get("brands", [])
        assert isinstance(brands, list), "Expected 'brands' to be a list"
        assert len(brands) > 0, "Expected brands list to be non-empty"