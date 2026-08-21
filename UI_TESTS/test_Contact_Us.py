import pytest
import os
import allure
import time
from config import Config

@pytest.mark.smoke
def test_contact_us_form(home_page, contact_page):
    config = Config()

    dynamic_email = f"contact_test_{int(time.time())}@test.com"
    upload_file_path = os.path.join(os.path.dirname(__file__), "../../data/test_upload.txt")
    if not os.path.exists(upload_file_path):
        os.makedirs(os.path.dirname(upload_file_path), exist_ok=True)
        with open(upload_file_path, "w", encoding="utf-8") as f:
            f.write("Test content for automation upload")

    with allure.step("1. Launch browser."):
        pass
        
    with allure.step("2. Navigate to url 'http://automationexercise.com'."):
        home_page.open_home()
        
    with allure.step("3. Verify that home page is visible successfully."):
        home_page.verify_logo_visible()
        
    with allure.step("4. Click on 'Contact Us' button."):
        home_page.click_contact_us() 
        
    with allure.step("5. Verify 'GET IN TOUCH' is visible."):
        contact_page.wait_for_visible(contact_page.get_in_touch_heading)
        
    with allure.step("6. Enter name, email, subject and message."):
        contact_page.fill_contact_form(
            name="Auto Tester",
            email=dynamic_email,
            subject="Automation Test Subject",
            message="This is a test message for automation.",
            file_path=upload_file_path
        )
        
    with allure.step("7. Upload file."):
       
        pass 
        
    with allure.step("8. Click 'Submit' button."):
        contact_page.click_submit_and_handle_alert()
        
    with allure.step("9. Click OK button."):
        pass
        
    with allure.step("10. Verify success message 'Success! Your details have been submitted successfully.' is visible."):
        contact_page.verify_success_message()
        
    with allure.step("11. Click 'Home' button and verify that landed to home page successfully."):
        contact_page.click_home()
        home_page.verify_logo_visible()
        assert "Automation Exercise" in home_page.get_page_title()