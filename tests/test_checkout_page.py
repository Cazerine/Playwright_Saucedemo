import pytest
from playwright.sync_api import Page, expect
from ..pages.content_page import ContentPage
from ..pages.login_page import LoginPage
from ..pages.checkout_page import CheckoutPage

def test_checkout_flow(page: Page, count=0):
    login_page  = LoginPage(page)
    login_page.open_page()
    login_page.authorize("standard_user", "secret_sauce")

    content_page = ContentPage(page)
    content_page.add_item_to_cart(count) #добавили один товар

    checkout_page = CheckoutPage(page)
    checkout_page.checkout_goto()







# pytest -s -v test_checkout_page.py

