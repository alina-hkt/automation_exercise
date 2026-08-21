from playwright.sync_api import Page
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
        
        self.success_message = page.locator("#contact-page").get_by_text("Success! Your details have been submitted successfully.")
        self.home_link = page.get_by_role("link", name="Home") 
        if not self.home_link.is_visible(timeout=self.config.PAGE_LOAD_TIMEOUT):
             self.home_link = page.locator("img[alt='Website for automation practice']")

        self.get_in_touch_heading = page.locator("h2").filter(has_text="GET IN TOUCH")

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
        self.wait_for_visible(self.success_message)

    def click_home(self):
        self.click(self.home_link)
        self.page.wait_for_url("**/", timeout=self.config.PAGE_LOAD_TIMEOUT)