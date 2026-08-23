from playwright.sync_api import Page
from UI_PAGES.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.logo = page.locator("img[alt='Website for automation practice']")
        self.cart_button = page.get_by_role("link", name="Cart")
        self.products_link = page.locator("a[href='/products']")
        self.login_signup_link = page.locator("a[href='/login']")
        self.products_heading = page.locator("h2").filter(has_text="All Products")
        self.header_container = page.locator("header")
        self.delete_account_btn = page.get_by_role("link", name="Delete Account")
        self.test_cases_link = page.get_by_role("link", name="Test Cases", exact=True)
        self.test_cases_heading = page.locator("h2").filter(has_text="Test Cases")
        self.subscription_heading = page.locator("h2").filter(has_text="SUBSCRIPTION")
        self.subscription_input = page.locator("#susbscribe_email")
        self.subscription_btn = page.locator("#subscribe")


    def open_home(self):
        self.open()

    def verify_logo_visible(self):
        self.wait_for_visible(self.logo)

    def click_contact_us(self):
        self.click(self.page.get_by_role("link", name="Contact Us"))

    def get_page_title(self) -> str:
        return self.get_title()

    def is_cart_button_visible(self) -> bool:
        return self.is_visible(self.cart_button)

    def click_cart(self):
        self.click(self.cart_button)

    def click_products(self):
        self.click(self.products_link)
        self.page.wait_for_url("**/products", timeout=self.config.PAGE_LOAD_TIMEOUT, wait_until="domcontentloaded")
        self.wait_for_visible(self.products_heading)

    def click_login_signup(self):
        self.click(self.login_signup_link)

    def verify_logged_in(self, username: str):
        self.page.reload(wait_until="networkidle", timeout=self.config.PAGE_LOAD_TIMEOUT)
        self.page.wait_for_load_state("domcontentloaded", timeout=self.config.PAGE_LOAD_TIMEOUT)
        header_text = self.header_container.text_content()
        assert "Logged in" in header_text, f"'Logged in' not found in header. Actual: {header_text}"
        assert username in header_text, f"User '{username}' not found in header. Actual: {header_text}"

    def click_delete_account(self):
        self.click(self.delete_account_btn)

    def click_test_cases(self):
        self.click(self.test_cases_link)
        self.wait_for_visible(self.test_cases_heading)

    def verify_test_cases_page_loaded(self):
        self.wait_for_visible(self.test_cases_heading)
        assert "Test Cases" in self.get_page_title(), "Title does not contain 'Test Cases'"

    def click_first_view_product_on_home(self):
        view_product_btn = self.page.get_by_text("View Product").first
        view_product_btn.scroll_into_view_if_needed()
        view_product_btn.click(force=True)

    def scroll_to_footer(self):
        self.subscription_heading.scroll_into_view_if_needed()

    def verify_subscription_heading_visible(self):
        self.wait_for_visible(self.subscription_heading)

    def subscribe(self, email: str):
        self.fill(self.subscription_input, email)
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.click(self.subscription_btn)

    def verify_success_message(self):
        success_msg = self.page.locator(".alert-success").filter(has_text="You have been successfully subscribed!")
        self.wait_for_visible(success_msg)