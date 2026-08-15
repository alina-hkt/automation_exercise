import pytest
from playwright.sync_api import Page
from UI_PAGES.home_page import HomePage
from UI_PAGES.register_page import RegisterPage
from UI_PAGES.account_deleted_page import AccountDeletedPage

@pytest.fixture(scope="function")
def home_page(page: Page):
    return HomePage(page)

@pytest.fixture(scope="function")
def register_page(page: Page):
    return RegisterPage(page)

@pytest.fixture(scope="function")
def account_deleted_page(page: Page):
    return AccountDeletedPage(page)

@pytest.fixture(scope="function")
def page(context): #как режим "Инкогнито" в браузере
    pg = context.new_page()
    
    pg.route("**/*googlesyndication.com/**", lambda route: route.abort())
    pg.route("**/*doubleclick.net/**", lambda route: route.abort())
    pg.route("**/*googleadservices.com/**", lambda route: route.abort())
    
    yield pg #Всё, что написано ДО yield — выполнится перед тестом
    
    pg.close()