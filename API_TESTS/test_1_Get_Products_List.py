import pytest
import allure
from playwright.sync_api import APIRequestContext

@allure.epic("API Testing")
@allure.feature("Products")
class TestGetAllProductsList:
    ENDPOINT = "/api/productsList"

    @allure.story("Get All Products List")
    @allure.title("Verify Status Code is 200")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    @pytest.mark.smoke
    def test_status_code_200(self, request_context: APIRequestContext):
        response = request_context.get(self.ENDPOINT)
        assert response.status == 200, f"Expected status code 200, but got {response.status}"

    @allure.story("Get All Products List")
    @allure.title("Verify Response Structure and Content")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    @pytest.mark.smoke
    def test_response_is_json_list(self, request_context: APIRequestContext):
        with allure.step(f"Send GET request to {self.ENDPOINT}"):
            response = request_context.get(self.ENDPOINT)
            data = response.json()

        with allure.step("Verify response body is a dictionary"):
            assert isinstance(data, dict), "Response body should be a dictionary"

        with allure.step("Verify 'products' key exists"):
            assert "products" in data, "Response should contain 'products' key"
            products = data["products"]

        with allure.step("Verify 'products' is a non-empty list"):
            assert isinstance(products, list), "'products' value should be a list"
            assert len(products) > 0, "Product list is empty"

    @allure.story("Get All Products List")
    @allure.title("Verify Required Fields in Products")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    @pytest.mark.regression
    def test_products_have_required_fields(self, request_context: APIRequestContext):
        with allure.step(f"Send GET request to {self.ENDPOINT}"):
            response = request_context.get(self.ENDPOINT)
            products = response.json()["products"]

        required_fields = ["id", "name", "price", "brand", "category"]

        with allure.step(f"Verify fields {required_fields} exist in all products"):
            for product in products:
                for field in required_fields:
                    assert field in product, f"Field '{field}' is missing in product id={product.get('id')}"

    @allure.story("Get All Products List")
    @allure.title("Verify Product IDs are Unique")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    @pytest.mark.regression
    def test_all_ids_are_unique(self, request_context: APIRequestContext):
        with allure.step(f"Send GET request to {self.ENDPOINT}"):
            response = request_context.get(self.ENDPOINT)
            products = response.json()["products"]

        with allure.step("Extract all product IDs"):
            ids = [p["id"] for p in products]

        with allure.step("Verify all IDs are unique"):
            assert len(ids) == len(set(ids)), "Found duplicate IDs"