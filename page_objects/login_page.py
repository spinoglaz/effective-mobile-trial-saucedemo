from playwright.sync_api import Page

from page_objects.inventory_page import InventoryPage


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_name_input = page.get_by_test_id('username')
        self.password_input = page.get_by_test_id('password')

    def navigate(self):
        self.page.goto('https://saucedemo.com')

    def login(self, username: str, password: str) -> InventoryPage:
        self.user_name_input.fill(username)
        self.password_input.fill(password)
        self.password_input.press('Enter')
        return InventoryPage(self.page)
