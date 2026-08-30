from playwright.sync_api import Page, expect

from UI_PAGES.base_page import BasePage


class AccountDeletedPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.heading = page.locator("h2").filter(has_text="Account Deleted!")
        self.deleted_message_locator = self.page.locator("b:has-text('ACCOUNT DELETED!')").first
        self.continue_btn = page.get_by_role("link", name="Continue")

    def verify_heading_visible(self):
        self.wait_for_visible(self.heading)

    def verify_account_deleted(self):
        expect(self.deleted_message_locator).to_be_visible()

    def click_continue(self):
        self.click(self.continue_btn)
