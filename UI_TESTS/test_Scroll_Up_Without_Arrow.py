import pytest
import allure
from config import Config

def test_scroll_up_and_down(home_page):
    config = Config()

    with allure.step("1. Launch browser."):
        pass

    with allure.step("2. Navigate to url 'http://automationexercise.com'."):
        home_page.open_home()

    with allure.step("3. Verify that home page is visible successfully."):
        home_page.verify_logo_visible()

    with allure.step("4. Scroll down page to bottom."):
        home_page.scroll_to_bottom()

    with allure.step("5. Verify 'SUBSCRIPTION' is visible."):
        home_page.verify_subscription_visible()

    with allure.step("6. Scroll up page to top."):
        home_page.scroll_to_top()

    with allure.step("7. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen."):
        home_page.verify_scrolled_to_top()