from playwright.sync_api import Page

from UI_PAGES.base_page import BasePage


class SidebarComponent(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.categories_heading = page.get_by_role("heading", name="Category")
        self.women_trigger = page.get_by_role("link", name=" Women")
        self.men_trigger = page.get_by_role("link", name=" Men")
        self.women_dress_link = page.get_by_role("link", name="Dress")
        self.men_tshirts_link = page.get_by_role("link", name="Tshirts")
        self.women_dress_heading = page.get_by_role("heading", name="Women - Dress Products")
        self.men_tshirts_heading = page.get_by_role("heading", name="Men - Tshirts Products")
        self.brands_heading = page.get_by_role("heading", name="Brands")
        self.polo_brand_link = page.get_by_role("link", name="(6) Polo")
        self.madame_brand_link = page.get_by_role("link", name="(5) Madame")
        self.polo_brand_page_heading = page.get_by_role("heading", name="Brand - Polo Products")
        self.madame_brand_page_heading = page.get_by_role("heading", name="Brand - Madame Products")

    def verify_categories_visible(self):
        self.wait_for_visible(self.categories_heading)

    def expand_and_click_women_subcategory(self):
        self.women_trigger.click()
        self.page.wait_for_timeout(timeout=self.config.SHORT_TIMEOUT)
        self.wait_for_visible(self.women_dress_link)
        self.women_dress_link.click()

    def verify_women_dress_page(self):
        self.wait_for_visible(self.women_dress_heading)

    def expand_and_click_men_subcategory(self):
        self.men_trigger.click()
        self.page.wait_for_timeout(timeout=self.config.SHORT_TIMEOUT)
        self.wait_for_visible(self.men_tshirts_link)
        self.men_tshirts_link.click()

    def verify_men_tshirts_page(self):
        self.wait_for_visible(self.men_tshirts_heading)

    def verify_brands_visible(self):
        self.wait_for_visible(self.brands_heading)

    def click_brand(self, brand_locator):
        self.wait_for_visible(brand_locator)
        brand_locator.click()

    def verify_brand_page(self, brand_heading_locator):
        self.wait_for_visible(brand_heading_locator)
