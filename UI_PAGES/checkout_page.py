from playwright.sync_api import Page

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
        self.checkout_heading = page.locator("h2").filter(has_text="Checkout")
        self.download_invoice_btn = page.get_by_role("link", name="Download Invoice")
        self.continue_btn = page.get_by_role("link", name="Continue")

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

    def verify_address_matches(
        self,
        expected_name: str,
        expected_address: str,
        expected_city: str,
        expected_state: str,
        expected_zip: str,
        expected_mobile: str,
    ):
        delivery_text = self.get_delivery_address_text()
        billing_text = self.get_billing_address_text()
        for field_name, field_value in [
            ("name", expected_name),
            ("address", expected_address),
            ("city", expected_city),
            ("state", expected_state),
            ("zip", expected_zip),
            ("mobile", expected_mobile),
        ]:
            assert field_value.lower() in delivery_text.lower(), (
                f"Delivery address missing {field_name}: '{field_value}'"
            )
            assert field_value.lower() in billing_text.lower(), f"Billing address missing {field_name}: '{field_value}'"

    def get_delivery_address_text(self) -> str:
        return self.delivery_address.text_content() or ""

    def get_billing_address_text(self) -> str:
        return self.billing_address.text_content() or ""

    def verify_order_placed_successfully(self):
        self.page.wait_for_url("**/payment_done/**", timeout=self.config.SHORT_TIMEOUT)
        self.wait_for_visible(self.download_invoice_btn, timeout=self.config.SHORT_TIMEOUT)

    def download_invoice(self):
        with self.page.expect_download(timeout=self.config.PAGE_LOAD_TIMEOUT) as download_info:
            self.click(self.download_invoice_btn)
        download = download_info.value
        download_path = download.path()
        assert download_path is not None, "Invoice download failed!"
        return download_path

    def click_continue_after_order(self):
        self.click(self.continue_btn)
