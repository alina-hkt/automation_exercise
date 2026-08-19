import pytest
from playwright.sync_api import Browser, Page
from UI_PAGES.home_page import HomePage
from UI_PAGES.register_page import RegisterPage
from UI_PAGES.account_deleted_page import AccountDeletedPage
from UI_PAGES.login_page import LoginPage


@pytest.fixture(scope="function")
def browser_context(browser: Browser):
    context = browser.new_context()
    
    context.route("**/*googlesyndication.com/**", lambda route: route.abort())
    context.route("**/*doubleclick.net/**", lambda route: route.abort())
    context.route("**/*googleadservices.com/**", lambda route: route.abort())
    
    yield context
    
    context.close()


@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def home_page(page: Page):
    return HomePage(page)


@pytest.fixture(scope="function")
def register_page(page: Page):
    return RegisterPage(page)


@pytest.fixture(scope="function")
def login_page(page: Page):
    return LoginPage(page)


@pytest.fixture(scope="function")
def account_deleted_page(page: Page):
    return AccountDeletedPage(page)