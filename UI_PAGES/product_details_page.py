from playwright.sync_api import Page
from UI_PAGES.base_page import BasePage

class ProductDetailsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.product_name = page.locator(".product-information h2")
        self.category = page.locator(".product-information p").first
        self.write_review_heading = page.get_by_text("Write Your Review")
        self.name_input = page.locator("#name")
        self.email_input = page.locator("#email")
        self.review_textarea = page.locator("#review")
        self.submit_btn = page.locator("#button-review")
        self.success_message = page.locator("#review-section").get_by_text(
            "Thank you for your review."
        )

    def verify_write_review_visible(self):
        self.write_review_heading.scroll_into_view_if_needed()
        self.wait_for_visible(self.write_review_heading)

    def fill_review_form(self, name: str, email: str, review: str):
        self.fill(self.name_input, name)
        self.fill(self.email_input, email)
        self.fill(self.review_textarea, review)

    def submit_review(self):
        self.click(self.submit_btn)

    def verify_success_message(self):
        self.wait_for_visible(self.success_message)