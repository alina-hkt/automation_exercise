from playwright.sync_api import Page
from UI_PAGES.base_page import BasePage
from UI_PAGES.product_detail_page import ProductDetailPage

class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.products_heading = page.locator("h2").filter(has_text="All Products")
        self.product_items = page.locator(".product-image-wrapper")
        self.found_products_count = 0
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
        if not self.search_btn.is_visible(timeout=self.config.SHORT_TIMEOUT):
            self.search_btn = page.get_by_role("button", name="")
        self.searched_products_heading = page.locator("h2").filter(has_text="Searched Products")
        self.search_results = page.locator(".product-image-wrapper")

    def search_product(self, product_name: str):
        self.wait_for_visible(self.search_input)
        self.fill(self.search_input, product_name)
        self.click(self.search_btn)

    def verify_products_list_visible(self):
        self.wait_for_visible(self.products_heading)

    def add_all_searched_products_to_cart(self):
        if self.found_products_count == 0:
            raise AssertionError("No products found to add to cart.")
        
        for index in range(self.found_products_count):
            product_wrapper = self.search_results.nth(index)
            add_btn = product_wrapper.locator(".overlay-content > .btn")
            self.add_product_to_cart_via_mouse(product_wrapper, add_btn)
            self.click_continue_shopping()

    def verify_search_results_visible(self):
        self.wait_for_visible(self.searched_products_heading)
        self.found_products_count = self.search_results.count()
        assert self.found_products_count > 0, f"No products found for search query. Count: {self.found_products_count}"

    def verify_all_searched_products_are_visible(self):
        if self.found_products_count == 0:
            raise AssertionError("Product list is empty, cannot verify visibility.")
        
        for index in range(self.found_products_count):
            product_wrapper = self.search_results.nth(index)
            img_locator = product_wrapper.locator("img")
            try:
                img_locator.wait_for(state="visible", timeout=self.config.SHORT_TIMEOUT)
            except Exception:
                raise AssertionError(f"Image in product at index {index} did not become visible within 5s!")

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
        self.continue_shopping_btn.click()
        self.cart_modal.wait_for(state="hidden", timeout=self.config.SHORT_TIMEOUT)

    def click_view_cart(self):
        self.wait_for_visible(self.view_cart_btn_modal, timeout=self.config.SHORT_TIMEOUT)
        self.view_cart_btn_modal.click()
        self.page.wait_for_url("**/view_cart", timeout=self.config.SHORT_TIMEOUT)

    def click_first_view_product(self) -> ProductDetailPage:
        self.page.goto(f"{self.config.BASE_URL}/product_details/1")

    def click_view_product(self, index: int = 0):
        view_product_btns = self.page.locator("a[href*='/product_details/']")
        btn = view_product_btns.nth(index)
        btn.scroll_into_view_if_needed()
        self.page.wait_for_timeout(timeout=self.config.SHORT_TIMEOUT)
        btn.click()
        self.page.wait_for_url("**/product_details/**", timeout=self.config.SHORT_TIMEOUT)