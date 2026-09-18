from playwright.sync_api import Page, expect

from UI_PAGES.base_page import BasePage


class ProductDetailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.product_name = page.get_by_role("heading", name="Blue Top")
        self.category = page.get_by_text("Category: Women > Tops")
        self.price = page.get_by_text("Rs.")
        self.quantity_label = page.get_by_text("Quantity:")
        self.condition = page.get_by_text("Condition:")
        self.brand = page.get_by_text("Brand:")
        self.availability = page.get_by_text("Availability:")
        self.product_heading = page.locator("h2").first
        self.quantity_input = page.locator("#quantity")
        self.add_to_cart_btn = page.get_by_role("button", name=" Add to cart")
        self.cart_modal = page.locator("#cartModal")
        self.view_cart_btn = page.locator("#cartModal").get_by_text("View Cart")

    def verify_product_detail_opened(self):
        expect(self.product_heading).to_be_visible(timeout=self.config.PAGE_LOAD_TIMEOUT)

    def set_quantity(self, quantity: int):
        self.quantity_input.fill(str(quantity))

    def click_add_to_cart(self):
        self.click(self.add_to_cart_btn)
        self.wait_for_visible(self.cart_modal)

    def click_view_cart(self):
        expect(self.view_cart_btn).to_be_visible(timeout=self.config.SHORT_TIMEOUT)
        self.click(self.view_cart_btn)
        self.page.wait_for_url("**/view_cart", timeout=self.config.SHORT_TIMEOUT)

    def verify_details_visible(self):
        expect(self.product_name).to_be_visible(timeout=self.config.SHORT_TIMEOUT)
        expect(self.category).to_be_visible(timeout=self.config.SHORT_TIMEOUT)
        expect(self.price).to_be_visible(timeout=self.config.SHORT_TIMEOUT)
        expect(self.availability).to_be_visible(timeout=self.config.SHORT_TIMEOUT)
        expect(self.condition).to_be_visible(timeout=self.config.SHORT_TIMEOUT)
        expect(self.brand).to_be_visible(timeout=self.config.SHORT_TIMEOUT)
