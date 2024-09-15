from playwright.sync_api import Page

from page_objects.checkout_step_two_page import CheckoutStepTwoPage


class CheckoutStepOnePage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.get_by_test_id('firstName')
        self.last_name_input = page.get_by_test_id('lastName')
        self.postal_code_input = page.get_by_test_id('postalCode')
        self.continue_button = page.get_by_test_id('continue')

    def fill_first_name(self, first_name: str):
        self.first_name_input.fill(first_name)

    def fill_last_name(self, last_name: str):
        self.last_name_input.fill(last_name)

    def fill_postal_code(self, postal_code: str):
        self.postal_code_input.fill(postal_code)

    def press_continue(self) -> CheckoutStepTwoPage:
        self.continue_button.click()
        return CheckoutStepTwoPage(self.page)
