import pytest
from playwright.sync_api import Page, expect
from ..pages.content_page import ContentPage
from ..pages.login_page import LoginPage
from .base_page import BasePage

class CheckoutPage(BasePage):
    SHOPPING_CART = "#shopping_cart_container"
    CHECKOUT = "#checkout"
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POST_CODE = "#postal-code"
    CONTINUE = "#continue"

    ITEM_NAME = "inventory-item-name"
    ITEM_PRICE = "inventory-item-price"

    FINISH = "#finish"

    COMPLETE_MSG = "complete-header"
    BACK_HOME = "#back-to-products"

    def __init__(self, page: Page):
        super().__init__(page)

    def get_name_item(self, number):
        return self.page.get_by_test_id(self.ITEM_NAME).nth(number).text_content()

    def get_price_item(self, number):
        return self.page.get_by_test_id(self.ITEM_PRICE).nth(number).text_content()

    def checkout_goto(self, number = 0, first_name = 'Test', last_name = 'Test', post_code = '000000'):
        NAME_ADDED = self.get_name_item(number)
        PRICE_ADDED = str(self.get_price_item(number))

        self.page.locator(self.SHOPPING_CART).click()
        self.page.locator(self.CHECKOUT).click()

        self.page.locator(self.FIRST_NAME).fill(first_name)
        self.page.locator(self.LAST_NAME).fill(last_name)
        self.page.locator(self.POST_CODE).fill(post_code)
        self.page.locator(self.CONTINUE).click()

        expect(self.page.get_by_test_id(self.ITEM_NAME)).to_contain_text(NAME_ADDED)  # проверка названия
        expect(self.page.get_by_test_id(self.ITEM_PRICE)).to_contain_text(PRICE_ADDED)  # проверка цены

        self.page.locator(self.FINISH).click()

        expect(self.page.get_by_test_id(self.COMPLETE_MSG)).to_contain_text('Thank you for your order!')
        self.page.locator(self.BACK_HOME).click()

        expect(self.page.get_by_test_id(ContentPage.INVENTORY_LIST)).to_be_visible()










