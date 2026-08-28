import pytest
import allure
from playwright.sync_api import APIRequestContext

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
@pytest.mark.smoke
def test_get_all_products_list(request_context: APIRequestContext):
    ENDPOINT = "/api/productsList"

    with allure.step("1. Send GET request and verify Status Code is 200"):
        response = request_context.get(ENDPOINT)
        assert response.status == 200, f"Expected status code 200, but got {response.status}"
        data = response.json()

    with allure.step("2. Verify Response Structure and Content"):
        assert isinstance(data, dict), "Response body should be a dictionary"
        assert "products" in data, "Response should contain 'products' key"
        products = data["products"]
        assert isinstance(products, list), "'products' value should be a list"
        assert len(products) > 0, "Product list is empty"

    with allure.step("3. Verify Required Fields in Products"):
        required_fields = ["id", "name", "price", "brand", "category"]
        for product in products:
            for field in required_fields:
                assert field in product, \
                    f"Field '{field}' is missing in product id={product.get('id')}"

    with allure.step("4. Verify Product IDs are Unique"):
        ids = [p["id"] for p in products]
        assert len(ids) == len(set(ids)), "Found duplicate IDs"