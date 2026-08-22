from playwright.sync_api import Page
from UI_PAGES.base_page import BasePage
from UI_PAGES.product_detail_page import ProductDetailPage

class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.products_heading = page.locator("h2").filter(has_text="All Products")
        self.product_items = page.locator(".product-image-wrapper")

    def verify_products_list_visible(self):
        self.wait_for_visible(self.products_heading)
        assert self.product_items.count() > 0, "Product list is empty!"

    def click_first_view_product(self) -> ProductDetailPage:
        self.page.goto(f"{self.config.BASE_URL}/product_details/1")
        
        return ProductDetailPage(self.page)