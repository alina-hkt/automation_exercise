from playwright.sync_api import Page, expect
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
        self.logged_in_indicator = self.page.locator(":has-text('Logged in as')").first
        self.recommended_heading = page.locator("h2").filter(has_text="recommended items")
        self.recommended_items = page.locator(".recommended_items .item")
        self.subscription_section = page.locator(".footer-widget").filter(has_text="Subscription")
        self.scroll_up_arrow = page.locator("#scrollUp")
        self.hero_text = page.locator("header .logo")

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
        cart_locator = self.page.locator("a[href='/view_cart']").first
        self.wait_for_visible(cart_locator)
        self.click(cart_locator)

    def click_products(self):
        self.click(self.products_link)
        self.page.wait_for_url("**/products", wait_until="domcontentloaded")
        self.wait_for_visible(self.products_heading)

    def click_login_signup(self):
        self.click(self.login_signup_link)

    def verify_logged_in(self, username: str):
        expect(self.logged_in_indicator).to_be_visible(timeout=self.config.SHORT_TIMEOUT)
        actual_text = self.logged_in_indicator.text_content()
        assert username in actual_text, f"Expected username '{username}' not found in '{actual_text}'"

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

    def scroll_to_recommended_items(self):
        recommended_container = self.page.locator(".recommended_items")
        recommended_container.scroll_into_view_if_needed()
        self.page.wait_for_timeout(timeout=self.config.SHORT_TIMEOUT) 

    def verify_recommended_items_visible(self):
        self.wait_for_visible(self.recommended_heading)
        assert self.recommended_items.count() > 0, "No recommended items found!"

    def scroll_recommended_carousel_to_start(self):
        prev_btn = self.page.locator(".recommended_items .left.carousel-control")
        while prev_btn.is_visible():
            prev_btn.click()
            self.page.wait_for_timeout(timeout=self.config.SHORT_TIMEOUT)
            if not prev_btn.is_visible():
                break
        first_item = self.page.locator(".recommended_items .item.active .productinfo p").first
        try:
            first_item.wait_for(state="visible", timeout=self.config.SHORT_TIMEOUT)
        except:
            pass

    def add_recommended_product_to_cart(self, index: int = 0):
        add_btns = self.page.locator(".recommended_items .productinfo > .btn")
        add_btns.first.wait_for(state="visible", timeout=self.config.SHORT_TIMEOUT)
        total = add_btns.count()
        assert total > 0, "No Add to Cart buttons found!"
        assert index < total, f"Index {index} out of range"
        btn = add_btns.nth(index)
        btn.scroll_into_view_if_needed()
        self.page.wait_for_timeout(timeout=self.config.SHORT_TIMEOUT)
        btn.click(force=True)
        view_cart_link = self.page.locator("#cartModal a[href='/view_cart']")
        view_cart_link.wait_for(state="visible", timeout=self.config.SHORT_TIMEOUT)
        view_cart_link.click()
        self.page.wait_for_url("**/view_cart", timeout=self.config.SHORT_TIMEOUT)

    def get_recommended_product_name(self, index: int = 0) -> str:
        name_locator = self.page.locator(".recommended_items .productinfo p").nth(index)
        try:
            name_locator.wait_for(state="visible", timeout=self.config.SHORT_TIMEOUT)
        except:
            pass
        text = name_locator.text_content()
        return text.strip() if text else "Unknown Product"

    def scroll_to_bottom(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        self.page.wait_for_timeout(timeout=self.config.SHORT_TIMEOUT)

    def verify_subscription_visible(self):
        self.wait_for_visible(self.subscription_section)

    def click_scroll_up_arrow(self):
        self.wait_for_visible(self.scroll_up_arrow)
        self.click(self.scroll_up_arrow)
        self.page.wait_for_timeout(timeout=self.config.SHORT_TIMEOUT)

    def verify_scrolled_to_top(self):
        self.wait_for_visible(self.hero_text)
        scroll_y = self.page.evaluate("window.scrollY")
        assert scroll_y < 100, f"Page not scrolled to top! scrollY={scroll_y}"