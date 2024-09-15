from playwright.sync_api import Page

from page_objects.checkout_complete_page import CheckoutCompletePage


class CheckoutStepTwoPage:
    def __init__(self, page: Page):
        self.page = page
        self.finish_button = page.get_by_test_id('finish')

    def finish(self) -> CheckoutCompletePage:
        self.finish_button.click()
        return CheckoutCompletePage(self.page)
