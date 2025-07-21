import pytest
from playwright.sync_api import Page, expect
from ..pages.content_page import ContentPage

@pytest.fixture
def authorization(page):
    content_page = ContentPage(page)
    content_page.open_page()
    content_page.authorize("standard_user", "secret_sauce")

    yield

    page.close()

def test_name_filter(page: Page, authorization):
    content_page = ContentPage(page)
    content_page.filter()

def test_add_to_cart(page: Page, authorization):
    content_page = ContentPage(page)
    content_page.shopping_cart()

def test_burger_menu_all_items(page: Page, authorization):
    content_page = ContentPage(page)
    content_page.burger_menu_all_items()

def test_burger_about(page: Page, authorization):
    content_page = ContentPage(page)
    content_page.burger_menu_about()

def test_burger_logout(page: Page, authorization):
    content_page = ContentPage(page)
    content_page.burger_menu_logout()

def test_item_cart(page: Page, authorization):
    content_page = ContentPage(page)
    content_page.item_cart()

#pytest -s -v test_content_page.py