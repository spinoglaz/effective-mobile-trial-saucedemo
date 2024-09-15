from playwright.sync_api import Page


class CheckoutCompletePage:
    def __init__(self, page: Page):
        self.page = page
        self.complete_header = page.get_by_test_id('complete-header')
        self.complete_text = page.get_by_test_id('complete-text')
