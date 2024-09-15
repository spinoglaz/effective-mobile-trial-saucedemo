from playwright.sync_api import Page

from page_objects.login_page import LoginPage


def test_order(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    inventory_page = login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_to_cart('Sauce Labs Backpack')
    cart_page = inventory_page.go_to_cart()
    assert 'Sauce Labs Backpack' in cart_page.item_names
    checkout_complete_page = cart_page.checkout(
        first_name='Daria',
        last_name='Egorova',
        postal_code='10000',
    )
    assert checkout_complete_page.complete_header.text_content() == 'Thank you for your order!'
    assert checkout_complete_page.complete_text.text_content() == (
        'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
    )
