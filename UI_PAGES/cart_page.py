from playwright.sync_api import Page, expect
from UI_PAGES.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.cart_heading = page.get_by_text("Shopping Cart")
        self.first_product_price = page.get_by_text("Rs.").nth(1)
        self.second_product_price = page.get_by_text("Rs.").nth(3)
        self.first_product_name = page.get_by_text("Blue Top")
        self.second_product_name = page.get_by_text("Men Tshirt")

    def verify_cart_loaded(self):
        self.page.wait_for_url("**/view_cart", timeout=self.config.PAGE_LOAD_TIMEOUT)
        self.wait_for_visible(self.cart_heading)

    def verify_products_in_cart(self):
        self.wait_for_visible(self.first_product_name)
        self.wait_for_visible(self.second_product_name)

    def verify_prices_and_quantity(self):
        self.wait_for_visible(self.first_product_price)
        self.wait_for_visible(self.second_product_price)
        
        assert "Rs." in self.first_product_price.text_content()
        assert "Rs." in self.second_product_price.text_content()

    def verify_product_quantity(self, expected_qty: str):
        qty_locator = self.page.get_by_role("button", name=expected_qty)
        self.wait_for_visible(qty_locator)
        actual_text = qty_locator.text_content()
        assert actual_text == expected_qty, f"Expected qty '{expected_qty}', got '{actual_text}'"