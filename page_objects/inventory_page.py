from typing import Optional

from playwright.sync_api import Page, Locator

from page_objects.cart_page import CartPage
import re


class InventoryItem:
    def __init__(self, locator: Locator):
        self.name = locator.get_by_test_id('inventory-item-name').text_content()
        self.add_to_card_button = locator.get_by_test_id(re.compile('add-to-cart-.*'))

    def add_to_cart(self):
        self.add_to_card_button.click()


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.shopping_cart_link = page.get_by_test_id('shopping-cart-link')
        self.items = [InventoryItem(item) for item in page.get_by_test_id('inventory-item').all()]

    def add_to_cart(self, item_name: str):
        item = self.find_item_by_name(item_name)
        item.add_to_cart()

    def find_item_by_name(self, name: str) -> Optional[InventoryItem]:
        for item in self.items:
            if item.name == name:
                return item

    def go_to_cart(self):
        self.shopping_cart_link.click()
        return CartPage(self.page)
