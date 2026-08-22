from playwright.sync_api import Page
from UI_PAGES.base_page import BasePage
from UI_PAGES.product_detail_page import ProductDetailPage

class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.products_heading = page.locator("h2").filter(has_text="All Products")
        self.product_items = page.locator(".product-image-wrapper")
        self.add_to_cart_btn_first = page.locator(".overlay-content > .btn").first
        self.add_to_cart_btn_second = page.locator(
            "div:nth-child(4) > .product-image-wrapper > .single-products > "
            ".product-overlay > .overlay-content > .btn"
        )
        
        self.cart_modal = page.locator("#cartModal")
        self.continue_shopping_btn = page.locator("#cartModal").get_by_text("Continue Shopping")
        self.view_cart_btn_modal = page.locator("#cartModal").get_by_text("View Cart")
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

    def add_product_to_cart_via_mouse(self, card_locator, btn_locator):
        card_locator.scroll_into_view_if_needed()
        
        box = card_locator.bounding_box()
        if box:
            center_x = box['x'] + box['width'] / 2
            center_y = box['y'] + box['height'] / 2
            self.page.mouse.move(center_x, center_y)
        
        btn_locator.evaluate("el => el.click()")
        self.wait_for_visible(self.cart_modal)

    def add_first_product_to_cart(self):
        first_card = self.product_items.nth(0)
        self.add_product_to_cart_via_mouse(first_card, self.add_to_cart_btn_first)
        
    def add_second_product_to_cart(self):
        second_card = self.product_items.nth(1)
        self.add_product_to_cart_via_mouse(second_card, self.add_to_cart_btn_second)

    def click_continue_shopping(self):
        self.wait_for_visible(self.continue_shopping_btn)
        self.continue_shopping_btn.click(force=True)
        self.cart_modal.wait_for(state="hidden", timeout=self.config.PAGE_LOAD_TIMEOUT)

    def click_view_cart(self):
        self.wait_for_visible(self.view_cart_btn_modal, timeout=self.config.PAGE_LOAD_TIMEOUT)
        self.view_cart_btn_modal.click(force=True)
        self.page.wait_for_url("**/view_cart", timeout=self.config.PAGE_LOAD_TIMEOUT)
        
        return ProductDetailPage(self.page)