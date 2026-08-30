from playwright.sync_api import Page

from UI_PAGES.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.name_input = page.get_by_placeholder("Name")
        self.email_input = page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")
        self.signup_btn = page.get_by_role("button", name="Signup")
        self.new_user_signup_heading = page.locator("h2").filter(has_text="New User Signup!")
        self.error_message = page.locator("p").filter(has_text="Email Address already exist!")
        self.mrs_radio = page.get_by_text("Mrs.")
        self.password_input = page.get_by_label("Password *")
        self.days_select = page.locator("#days")
        self.months_select = page.locator("#months")
        self.years_select = page.locator("#years")
        self.newsletter_checkbox = page.get_by_text("Sign up for our newsletter!")
        self.first_name_input = page.get_by_label("First name *")
        self.last_name_input = page.get_by_label("Last name *")
        self.company_input = page.get_by_label("Company", exact=True)
        self.address1_input = page.get_by_label("Address * (Street address, P.")
        self.address2_input = page.get_by_label("Address 2")
        self.country_select = page.get_by_label("Country *")
        self.state_input = page.get_by_label("State *")
        self.city_input = page.get_by_label("City *")
        self.zipcode_input = page.locator("#zipcode")
        self.mobile_input = page.get_by_label("Mobile Number *")
        self.create_account_btn = page.get_by_role("button", name="Create Account")
        self.account_created_heading = page.locator("h2").filter(has_text="Account Created!")
        self.continue_btn = page.get_by_role("link", name="Continue")

    def fill_name(self, name: str):
        self.fill(self.name_input, name)

    def fill_email(self, email: str):
        self.fill(self.email_input, email)

    def click_signup(self):
        self.click(self.signup_btn)

    def verify_error_visible(self):
        self.wait_for_visible(self.error_message)

    def verify_new_user_signup_visible(self):
        self.wait_for_visible(self.new_user_signup_heading)

    def select_title_mrs(self):
        self.click(self.mrs_radio)

    def fill_password(self, password: str):
        self.fill(self.password_input, password)

    def set_date_of_birth(self, day: str, month: str, year: str):
        self.days_select.select_option(value=day)
        self.months_select.select_option(value=month)
        self.years_select.select_option(value=year)

    def check_newsletter(self):
        self.click(self.newsletter_checkbox)

    def fill_address_details(
        self,
        first_name: str,
        last_name: str,
        company: str,
        address1: str,
        address2: str,
        country: str,
        state: str,
        city: str,
        zipcode: str,
        mobile: str,
    ):
        self.fill(self.first_name_input, first_name)
        self.fill(self.last_name_input, last_name)
        self.fill(self.company_input, company)
        self.fill(self.address1_input, address1)
        self.fill(self.address2_input, address2)
        self.country_select.select_option(label=country)
        self.fill(self.state_input, state)
        self.fill(self.city_input, city)
        self.fill(self.zipcode_input, zipcode)
        self.fill(self.mobile_input, mobile)

    def click_create_account(self):
        self.click(self.create_account_btn)

    def verify_account_created(self):
        self.wait_for_visible(self.account_created_heading)

    def click_continue(self):
        self.click(self.continue_btn)
