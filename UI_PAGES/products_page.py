from playwright.sync_api import Page
from UI_PAGES.base_page import BasePage
from UI_PAGES.product_detail_page import ProductDetailPage

class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.products_heading = page.locator("h2").filter(has_text="All Products")
        self.product_items = page.locator(".product-image-wrapper")
        self.search_input = page.get_by_placeholder("Search Product")
        self.search_btn = page.locator("#search_submit")
        if not self.search_btn.is_visible(timeout=self.config.PAGE_LOAD_TIMEOUT):
            self.search_btn = page.get_by_role("button", name="")
        
        self.searched_products_heading = page.locator("h2").filter(has_text="Searched Products")
        self.search_results = page.locator(".product-image-wrapper")

    def search_product(self, product_name: str):
        self.wait_for_visible(self.search_input)
        self.fill(self.search_input, product_name)
        self.click(self.search_btn)

    def verify_search_results_visible(self):
        self.wait_for_visible(self.searched_products_heading)
        count = self.search_results.count()
        assert count > 0, f"No products found for search query. Count: {count}"

    def verify_products_list_visible(self):
        self.wait_for_visible(self.products_heading)
        assert self.product_items.count() > 0, "Product list is empty!"

    def click_first_view_product(self) -> ProductDetailPage:
        self.page.goto(f"{self.config.BASE_URL}/product_details/1")
        
        return ProductDetailPage(self.page)