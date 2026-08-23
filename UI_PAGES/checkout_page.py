from playwright.sync_api import Page, expect
from UI_PAGES.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.proceed_to_checkout_btn = page.get_by_text("Proceed To Checkout")
        self.register_login_btn = page.get_by_role("link", name="Register / Login")
        self.billing_address = page.locator("#address_delivery")
        self.delivery_address = page.locator("#address_invoice")
        self.order_review = page.locator("h2").filter(has_text="Review Your Order")
        self.comment_textarea = page.locator("textarea[name='message']")
        self.place_order_btn = page.get_by_text("Place Order")

    def click_proceed_to_checkout(self):
        self.wait_for_visible(self.proceed_to_checkout_btn)
        self.proceed_to_checkout_btn.click()

    def click_register_login(self):
        self.wait_for_visible(self.register_login_btn)
        self.click(self.register_login_btn)

    def verify_addresses_and_review(self):
        self.wait_for_visible(self.billing_address)
        self.wait_for_visible(self.delivery_address)
        self.wait_for_visible(self.order_review)

    def fill_comment_and_place_order(self, comment: str):
        self.comment_textarea.scroll_into_view_if_needed()
        self.page.wait_for_timeout(timeout=self.config.SHORT_TIMEOUT)
        self.fill(self.comment_textarea, comment)
        
        self.page.evaluate("""
            const btn = Array.from(document.querySelectorAll('a, button'))
                .find(el => el.innerText.trim() === 'Place Order');
            if (btn) btn.scrollIntoView({block: 'center', inline: 'center'});
        """)
        self.page.wait_for_timeout(timeout=self.config.SHORT_TIMEOUT)
        
        self.place_order_btn.evaluate("el => el.click()")