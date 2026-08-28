import pytest
from playwright.sync_api import Browser, Page
from UI_PAGES.home_page import HomePage
from UI_PAGES.register_page import RegisterPage
from UI_PAGES.account_deleted_page import AccountDeletedPage
from UI_PAGES.login_page import LoginPage
from UI_PAGES.contact_page import ContactPage
from UI_PAGES.products_page import ProductsPage
from UI_PAGES.product_detail_page import ProductDetailPage
from UI_PAGES.cart_page import CartPage
from UI_PAGES.checkout_page import CheckoutPage
from UI_PAGES.signup_page import SignupPage
from UI_PAGES.payment_page import PaymentPage
from UI_COMPONENTS.sidebar import SidebarComponent
from UI_PAGES.product_details_page import ProductDetailsPage
from playwright.sync_api import sync_playwright, APIRequestContext

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
def contact_page(page: Page):
    return ContactPage(page)

@pytest.fixture(scope="function")
def account_deleted_page(page: Page):
    return AccountDeletedPage(page)

@pytest.fixture(scope="function")
def products_page(page: Page):
    return ProductsPage(page)

@pytest.fixture(scope="function")
def product_detail_page(page: Page):
    return ProductDetailPage(page)

@pytest.fixture(scope="function")
def cart_page(page: Page):
    return CartPage(page)

@pytest.fixture(scope="function")
def checkout_page(page: Page): 
    return CheckoutPage(page)

@pytest.fixture(scope="function")
def signup_page(page: Page): 
    return SignupPage(page)

@pytest.fixture(scope="function")
def payment_page(page: Page): 
    return PaymentPage(page)

@pytest.fixture(scope="function")
def sidebar(page: Page): 
    return SidebarComponent(page)

@pytest.fixture(scope="function")
def product_details_page(page: Page): 
    return ProductDetailsPage(page)

@pytest.fixture(scope="session")
def request_context() -> APIRequestContext:
    from config import Config
    base_url = Config.BASE_URL
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(base_url=base_url)
        yield context.request
        context.request.dispose()
        browser.close()