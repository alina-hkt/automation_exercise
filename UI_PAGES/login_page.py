from playwright.sync_api import Page
from UI_PAGES.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        login_form = page.locator("form").filter(has_text="Login")
        self.email_input = login_form.get_by_placeholder("Email Address")
        self.password_input = page.get_by_placeholder("Password")
        self.login_btn = page.get_by_role("button", name="Login")
        
        self.login_heading = page.locator("h2").filter(has_text="Login to your account")
        
        self.header_container = page.locator("header")
        self.delete_account_btn = page.get_by_role("link", name="Delete Account")

    def wait_for_login_form(self):
        self.wait_for_visible(self.login_heading)

    def fill_email(self, email: str):
        self.fill(self.email_input, email)

    def fill_password(self, password: str):
        self.fill(self.password_input, password)

    def click_login(self):
        self.click(self.login_btn)

    def verify_logged_in(self):
        self.page.reload(wait_until="networkidle",timeout=self.config.PAGE_LOAD_TIMEOUT)
        self.page.wait_for_load_state("domcontentloaded",timeout=self.config.PAGE_LOAD_TIMEOUT)
        
        header_text = self.header_container.text_content()
        assert "Logged in as" in header_text, f"'Logged in as' not found in header. Actual: {header_text}"

    def click_delete_account(self):
        self.click(self.delete_account_btn)