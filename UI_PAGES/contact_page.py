from playwright.sync_api import Page, expect

from UI_PAGES.base_page import BasePage


class ContactPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.name_input = page.get_by_placeholder("Name")
        self.email_input = page.get_by_placeholder("Email", exact=True)
        self.subject_input = page.get_by_placeholder("Subject")
        self.message_input = page.get_by_placeholder("Your Message Here")
        self.upload_file_input = page.locator("input[name='upload_file']")
        self.submit_btn = page.get_by_role("button", name="Submit")
        self.success_message = page.locator(".status.alert-success").first
        self.home_link = page.get_by_role("link", name="Home").first
        self.get_in_touch_heading = page.locator("h2").filter(has_text="GET IN TOUCH")

    def fill_contact_form(self, name: str, email: str, subject: str, message: str, file_path: str):
        expect(self.name_input).to_be_visible(timeout=self.config.SHORT_TIMEOUT)
        self.name_input.fill(name)

        expect(self.email_input).to_be_visible(timeout=self.config.SHORT_TIMEOUT)
        self.email_input.fill(email)

        expect(self.subject_input).to_be_visible(timeout=self.config.SHORT_TIMEOUT)
        self.subject_input.fill(subject)

        expect(self.message_input).to_be_visible(timeout=self.config.SHORT_TIMEOUT)
        self.message_input.fill(message)

        expect(self.upload_file_input).to_be_visible(timeout=self.config.SHORT_TIMEOUT)
        self.upload_file_input.set_input_files(file_path)

        self.page.wait_for_timeout(timeout=self.config.SHORT_TIMEOUT)

    def click_submit_and_handle_alert(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.click(self.submit_btn)
        self.page.wait_for_load_state(timeout=self.config.PAGE_LOAD_TIMEOUT)

    def verify_success_message(self):
        expect(self.success_message).to_have_count(1, timeout=self.config.SHORT_TIMEOUT)

        expect(self.success_message).to_contain_text(
            "Success! Your details have been submitted successfully.", timeout=self.config.SHORT_TIMEOUT
        )

    def click_home(self):
        self.click(self.home_link)
        self.page.wait_for_url("**/", timeout=self.config.SHORT_TIMEOUT)
