from playwright.sync_api import Page, expect
from config import Config

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.config = Config()

    def open(self, url: str = None):
        target_url = url or self.config.BASE_URL
        self.page.goto(target_url, timeout=self.config.PAGE_LOAD_TIMEOUT)

    def get_title(self) -> str:
        return self.page.title()

    def wait_for_visible(self, locator, timeout: int = None): #время ожидания можно передать при вызове, а если не передали — возьмем стандартное из конфига
        timeout = timeout or self.config.PAGE_LOAD_TIMEOUT
        expect(locator).to_be_visible(timeout=timeout)

    def click(self, locator, timeout=None):
        if timeout is None:
            timeout = self.config.PAGE_LOAD_TIMEOUT
        locator.click(timeout=timeout)

    def fill(self, locator, text: str):
        locator.fill(text, timeout=self.config.SHORT_TIMEOUT)

    def is_visible(self, locator) -> bool:
        return locator.is_visible(timeout=self.config.SHORT_TIMEOUT)

    def select_option(self, locator, value: str):
        locator.select_option(value=value, timeout=self.config.SHORT_TIMEOUT)