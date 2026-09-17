from playwright.sync_api import Page, expect

from UI_PAGES.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        login_form = page.locator("form").filter(has_text="Login")
        self.email_input = login_form.get_by_placeholder("Email Address")
        self.password_input = page.get_by_placeholder("Password")
        self.login_btn = page.get_by_role("button", name="Login")
        self.login_heading = page.locator("h2").filter(has_text="Login to your account")
        self.logout_btn = page.get_by_role("link", name="Logout")
        self.error_message = page.locator("p").filter(has_text="Your email or password is incorrect!")
        self.header_container = page.locator("header")
        self.delete_account_btn = page.get_by_role("link", name="Delete Account")

    def wait_for_login_form(self):
        expect(self.login_heading).to_be_visible(timeout=self.config.PAGE_LOAD_TIMEOUT)

    def fill_login_form(self, email: str, password: str):
        self.fill_email(email)
        self.fill_password(password)
        self.click_login()

    def fill_email(self, email: str):
        self.fill(self.email_input, email)

    def fill_password(self, password: str):
        self.fill(self.password_input, password)

    def click_login(self):
        self.click(self.login_btn)

    def verify_error_visible(self):
        expect(self.error_message).to_be_visible(timeout=self.config.SHORT_TIMEOUT)

    def verify_logged_in(self, username: str):
        expected_text = f"Logged in as {username}"
        expect(self.header_container).to_contain_text(expected_text, timeout=self.config.SHORT_TIMEOUT)

    def click_logout(self):
        expect(self.logout_btn).to_be_visible(timeout=self.config.PAGE_LOAD_TIMEOUT)
        self.click(self.logout_btn)

    def verify_returned_to_login_page(self):
        expect(self.login_heading).to_be_visible(timeout=self.config.PAGE_LOAD_TIMEOUT)

    def click_delete_account(self):
        expect(self.delete_account_btn).to_be_visible(timeout=self.config.PAGE_LOAD_TIMEOUT)
        self.click(self.delete_account_btn)
