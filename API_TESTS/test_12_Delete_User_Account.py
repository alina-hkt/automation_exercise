import pytest
import time
import allure
from playwright.sync_api import APIRequestContext
from config import Config
from urllib.parse import urlencode

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
@pytest.mark.regression
def test_delete_user_account(request_context: APIRequestContext):
    config = Config()
    ENDPOINT = "/api/deleteAccount"
    test_email = f"testuser_del_{int(time.time())}@example.com"
    test_password = config.TEST_USER_PASSWORD
    create_data = {
        "name": "DeleteTestUser",
        "email": test_email,
        "password": test_password,
        "title": "Mr",
        "birth_date": "01",
        "birth_month": "01",
        "birth_year": "2000",
        "firstname": "Delete",
        "lastname": "Test",
        "company": "Test Co",
        "address1": "1 Test St",
        "address2": "",
        "country": "United States",
        "zipcode": "00000",
        "state": "New York",
        "city": "New York",
        "mobile_number": "0000000000"
    }
    
    with allure.step("1. Create a test user via POST /api/createAccount to be deleted."):
        request_context.post(
            "/api/createAccount",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=urlencode(create_data)
        )

    with allure.step("2. Send DELETE request to /api/deleteAccount with credentials."):
        delete_payload = {"email": test_email, "password": test_password}
        response = request_context.delete(
            ENDPOINT,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=urlencode(delete_payload)
        )
        data = response.json()
        
    with allure.step("3. Verify HTTP Status Code is 200."):
        assert response.status == 200, f"Expected HTTP 200, but got {response.status}"
        
    with allure.step("4. Verify response code in body is 200."):
        assert data.get("responseCode") == 200, \
            f"Expected responseCode 200 in body, but got {data.get('responseCode')}"
            
    with allure.step("5. Verify success message 'Account deleted!' in response body."):
        expected_message = "Account deleted!"
        actual_message = data.get("message", "")
        assert actual_message == expected_message, \
            f"Expected message '{expected_message}', but got '{actual_message}'"