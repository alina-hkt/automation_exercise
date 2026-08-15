from playwright.sync_api import Page
from UI_PAGES.base_page import BasePage

class AccountDeletedPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.heading = page.locator("h2").filter(has_text="Account Deleted!")
        self.continue_btn = page.get_by_role("link", name="Continue")

    def verify_heading_visible(self):
        self.wait_for_visible(self.heading)

    def click_continue(self):
        self.click(self.continue_btn)