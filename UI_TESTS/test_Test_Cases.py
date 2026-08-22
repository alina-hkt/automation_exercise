import pytest
import allure
from config import Config

@pytest.mark.smoke
def test_verify_test_cases_page(home_page):
    config = Config()
    
    with allure.step("1. Launch browser."):
        pass
        
    with allure.step("2. Navigate to url 'http://automationexercise.com'."):
        home_page.open_home()
        
    with allure.step("3. Verify that home page is visible successfully."):
        home_page.verify_logo_visible()
        
    with allure.step("4. Click on 'Test Cases' button."):
        home_page.click_test_cases()
        
    with allure.step("5. Verify user is navigated to test cases page successfully."):
        home_page.verify_test_cases_page_loaded()