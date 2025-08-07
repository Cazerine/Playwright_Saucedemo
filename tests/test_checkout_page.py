from playwright.sync_api import Page
from ..pages.content_page import ContentPage
from ..pages.login_page import LoginPage
from ..pages.checkout_page import CheckoutPage
from ..pages.cart_page import CartPage
from ..pages.form_page import FormPage
from ..pages.confirmation_page import ConfirmationPage

def test_checkout_flow(authorized_page, count=0):
    content_page = ContentPage(authorized_page)
    content_page.add_item_to_cart(count) #добавили один товар

    cart_page = content_page.open_cart()

    form_page = cart_page.goto_checkout()
    form_page.fill_form('Test', 'Test', '000000')

    checkout_page = CheckoutPage(authorized_page)

    checkout_page.verify_checkout()
    checkout_page.finish_checkout()

    confirmation_page = ConfirmationPage(authorized_page)
    confirmation_page.verify_success_message()

    checkout_page.isLoaded(ContentPage.INVENTORY_CNTR) # проверяем, что страница с контентом загрузилась

# pytest -s -v test_checkout_page.py
