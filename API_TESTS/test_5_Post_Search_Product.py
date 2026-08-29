import pytest
import allure
from playwright.sync_api import APIRequestContext

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
@pytest.mark.regression
def test_post_to_search_product(request_context: APIRequestContext):
    ENDPOINT = "/api/searchProduct"
    SEARCH_TERM = "top"
    
    with allure.step("1. Send POST request to /api/searchProduct with search parameter."):
        response = request_context.post(
            ENDPOINT,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=f"search_product={SEARCH_TERM}"
        )
        data = response.json()
        
    with allure.step("2. Verify HTTP Status Code is 200."):
        assert response.status == 200, f"Expected HTTP 200, but got {response.status}"
        
    with allure.step("3. Verify response code in body is 200."):
        assert data.get("responseCode") == 200, \
            f"Expected responseCode 200 in body, but got {data.get('responseCode')}"
            
    with allure.step("4. Verify searched products list is present and not empty."):
        products = data.get("products", [])
        assert isinstance(products, list), "Expected 'products' to be a list"
        assert len(products) > 0, f"Expected products list for '{SEARCH_TERM}' to be non-empty"