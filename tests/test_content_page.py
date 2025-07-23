import pytest
from playwright.sync_api import Page, expect
from ..pages.content_page import ContentPage
from ..pages.login_page import LoginPage

@pytest.fixture
def authorization(page):
    content_page = LoginPage(page)
    content_page.open_page()
    content_page.authorize("standard_user", "secret_sauce")

    yield

    page.close()

def test_goto_content_page(page: Page, authorization):
    content_page = ContentPage(page)
    content_page.verify_content_page_open()

@pytest.mark.parametrize("option, expected_text", [
     ('az', "Name (A to Z)"),
     ('za', "Name (Z to A)"),
     ('lohi', "Price (low to high)"),
     ('hilo', "Price (high to low)"),
 ])
def test_verify_filter(page: Page, authorization, option, expected_text):
    content_page = ContentPage(page)
    content_page.verify_filter(option, expected_text)

def test_add_to_cart(page: Page, authorization, count = 3):
    content_page = ContentPage(page)
    for i in range (count):
        content_page.add_item_to_cart(i) #добавили в корзину 3 товара

    content_page.verify_shopping_cart()

def test_item_card(page: Page, authorization):
    content_page = ContentPage(page)
    content_page.verify_item_card_goto_and_back()

#pytest -s -v test_content_page.py