from typing import List

from playwright.sync_api import Page

from page_objects.checkout_complete_page import CheckoutCompletePage
from page_objects.checkout_step_one_page import CheckoutStepOnePage


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = self.page.get_by_test_id('checkout')
        self.items = page.get_by_test_id('inventory-item-name')

    @property
    def item_names(self) -> List[str]:
        return self.items.all_text_contents()

    def press_checkout(self) -> CheckoutStepOnePage:
        self.checkout_button.click()
        return CheckoutStepOnePage(self.page)

    def checkout(self, first_name: str, last_name: str, postal_code: str) -> CheckoutCompletePage:
        checkout_step_one_page = self.press_checkout()
        checkout_step_one_page.fill_first_name(first_name)
        checkout_step_one_page.fill_last_name(last_name)
        checkout_step_one_page.fill_postal_code(postal_code)
        checkout_step_two_page = checkout_step_one_page.press_continue()
        return checkout_step_two_page.finish()
