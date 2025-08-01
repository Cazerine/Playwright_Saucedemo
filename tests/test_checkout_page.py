import pytest
from playwright.sync_api import Page, expect
from ..pages.content_page import ContentPage
from ..pages.login_page import LoginPage
from ..pages.checkout_page import CheckoutPage, CartPage, FormPage, ConfirmationPage

def test_checkout_flow(page: Page, count=0):
    login_page  = LoginPage(page)
    login_page.open_page()
    login_page.authorize("standard_user", "secret_sauce")

    content_page = ContentPage(page)
    content_page.add_item_to_cart(count) #добавили один товар

    cart_page = CartPage(page)
    cart_page.open_cart()

    checkout_page = CheckoutPage(page)
    checkout_page.goto_checkout()

    form_page = FormPage(page)
    form_page.fill_form('Test', 'Test', '000000')

    checkout_page.verify_checkout()

    confirmation_page = ConfirmationPage(page)
    confirmation_page.finish_checkout()
    confirmation_page.verify_success_message()

    checkout_page.isLoaded_LOGO()  # проверяем, что страница с контентом загрузилась
    checkout_page.isLoaded(ContentPage.FILTER_BTN)
    checkout_page.isLoaded(ContentPage.INVENTORY_LIST)

# pytest -s -v test_checkout_page.py
