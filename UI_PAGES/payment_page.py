from playwright.sync_api import Page, expect
from UI_PAGES.base_page import BasePage

class PaymentPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.name_on_card = page.locator("[data-qa='name-on-card']")
        self.card_number = page.locator("[data-qa='card-number']")
        self.cvc = page.locator("[data-qa='cvc']")
        self.exp_month = page.locator("[data-qa='expiry-month']")
        self.exp_year = page.locator("[data-qa='expiry-year']")
        self.pay_confirm_btn = page.get_by_role("button", name="Pay and Confirm Order")
        self.success_message = page.locator("p").filter(
            has_text="Congratulations! Your order has been confirmed!"
        )
        self.continue_btn = page.get_by_role("link", name="Continue")

    def fill_payment_details(self, name: str = "John Doe", 
                              card: str = "4111111111111111",
                              cvc: str = "123",
                              month: str = "12",
                              year: str = "2030"):
        self.fill(self.name_on_card, name)
        self.fill(self.card_number, card)
        self.fill(self.cvc, cvc)
        self.fill(self.exp_month, month)
        self.fill(self.exp_year, year)

    def click_pay_and_confirm(self):
        self.click(self.pay_confirm_btn)

    def verify_order_success_and_continue(self):
        self.wait_for_visible(self.success_message)
        self.click(self.continue_btn)
        self.page.wait_for_url("**/", timeout=self.config.SHORT_TIMEOUT)