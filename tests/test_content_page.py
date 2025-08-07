import pytest
from ..pages.content_page import ContentPage

def test_goto_content_page(authorized_page):
    content_page = ContentPage(authorized_page)
    content_page.isLoaded()

@pytest.mark.parametrize("option, expected_text", [
     ('az', "Name (A to Z)"),
     ('za', "Name (Z to A)"),
     ('lohi', "Price (low to high)"),
     ('hilo', "Price (high to low)"),
 ])
def test_verify_filter(authorized_page, option, expected_text):
    content_page = ContentPage(authorized_page)
    content_page.verify_filter(option, expected_text)

def test_add_to_cart(authorized_page, count = 3):
    content_page = ContentPage(authorized_page)
    for i in range (count):
        content_page.add_item_to_cart(i) #добавили в корзину 3 товара

    content_page.verify_shopping_cart()

def test_item_card(authorized_page):
    content_page = ContentPage(authorized_page)
    content_page.verify_item_card_goto_and_back()



#pytest -s -v test_content_page.py