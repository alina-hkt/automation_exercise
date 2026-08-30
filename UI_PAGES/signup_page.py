from playwright.sync_api import Page

from UI_PAGES.base_page import BasePage


class SignupPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.name_input = page.get_by_placeholder("Name")
        signup_form = page.locator("form").filter(has_text="Signup")
        self.email_input = signup_form.get_by_placeholder("Email Address")
        self.signup_btn = page.get_by_role("button", name="Signup")
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
        self.account_created_heading = page.locator("b").filter(has_text="Account Created!")
        self.continue_btn = page.get_by_role("link", name="Continue")

    def fill_initial_signup(self, name: str, email: str):
        self.wait_for_visible(self.name_input)
        self.fill(self.name_input, name)
        self.fill(self.email_input, email)
        self.click(self.signup_btn)

    def fill_account_details(self, details: dict):
        self.click(self.mrs_radio)
        self.fill(self.password_input, details["password"])
        self.select_option(self.days_select, details["day"])
        self.select_option(self.months_select, details["month"])
        self.select_option(self.years_select, details["year"])
        self.click(self.newsletter_checkbox)
        self.fill(self.first_name_input, details["first_name"])
        self.fill(self.last_name_input, details["last_name"])
        self.fill(self.company_input, details["company"])
        self.fill(self.address1_input, details["address1"])
        self.fill(self.address2_input, details["address2"])
        self.select_option(self.country_select, details["country"])
        self.fill(self.state_input, details["state"])
        self.fill(self.city_input, details["city"])
        self.fill(self.zipcode_input, details["zipcode"])
        self.fill(self.mobile_input, details["mobile"])

    def click_create_account(self):
        self.click(self.create_account_btn)

    def verify_account_created(self):
        self.wait_for_visible(self.account_created_heading)

    def click_continue_after_creation(self):
        self.click(self.continue_btn)
