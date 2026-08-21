import allure
from playwright.sync_api import Page, expect
from UI_PAGES.base_page import BasePage


class ContactPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.name_input = page.get_by_placeholder("Name")
        self.email_input = page.get_by_placeholder("Email", exact=True)
        self.subject_input = page.get_by_placeholder("Subject")
        self.message_input = page.get_by_placeholder("Your Message Here")
        self.upload_file_input = page.locator("input[name=\"upload_file\"]")
        self.submit_btn = page.get_by_role("button", name="Submit")
        
        self.get_in_touch_heading = page.locator("h2").filter(has_text="GET IN TOUCH")
        
        self.home_link = page.get_by_role("link", name="Home") 
        if not self.home_link.is_visible(timeout=self.config.PAGE_LOAD_TIMEOUT):
             self.home_link = page.locator("img[alt='Website for automation practice']")

    def fill_contact_form(self, name: str, email: str, subject: str, message: str, file_path: str):
        self.fill(self.name_input, name)
        self.fill(self.email_input, email)
        self.fill(self.subject_input, subject)
        self.fill(self.message_input, message)
        
        self.upload_file_input.set_input_files(file_path)
    
    def click_submit_and_handle_alert(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.click(self.submit_btn)
    
    def verify_success_message(self):
        locator = self.page.locator("#contact-page .alert-success").filter(
            has_text="Success! Your details have been submitted successfully."
        )
        
        try:
            expect(locator).to_be_visible(timeout=10000)
        except AssertionError:
            screenshot_path = "debug_contact_success.png"
            self.page.screenshot(path=screenshot_path)
            allure.attach.file(
                screenshot_path, 
                name="Debug Screenshot", 
                attachment_type=allure.attachment_type.PNG
            )
            
            html_content = self.page.content()
            allure.attach(
                html_content, 
                name="Page HTML on Failure", 
                attachment_type=allure.attachment_type.TEXT
            )
            
            raise AssertionError("Сообщение об успехе не найдено. См. вложения в отчете Allure.")

    def click_home(self):
        self.click(self.home_link)
        self.page.wait_for_url("**/", timeout=self.config.PAGE_LOAD_TIMEOUT)