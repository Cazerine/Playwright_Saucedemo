import pytest
from playwright.sync_api import Page, expect
from .base_page import BasePage

class CheckoutPage(BasePage):
    CHECKOUT_BTN = "#checkout"

    ITEM_NAME = "inventory-item-name"
    ITEM_PRICE = "inventory-item-price"

    def __init__(self, page: Page):
        super().__init__(page)

    def get_item_name(self, number):
        return self.page.get_by_test_id(self.ITEM_NAME).nth(number).text_content()

    def get_item_price(self, number):
        return self.page.get_by_test_id(self.ITEM_PRICE).nth(number).text_content()

    def get_name_from_item_card(self, number = 0):
        name_added = self.get_item_name(number)
        return name_added

    def get_price_from_item_card(self, number=0):
        price_added = str(self.get_item_price(number))
        return price_added

    def goto_checkout(self):
        self.page.locator(self.CHECKOUT_BTN).click()

    def verify_checkout(self):
        expect(self.page.get_by_test_id(self.ITEM_NAME)).to_contain_text(self.get_name_from_item_card(0))  # проверка названия
        expect(self.page.get_by_test_id(self.ITEM_PRICE)).to_contain_text(self.get_price_from_item_card(0))  # проверка цены

class CartPage(BasePage):
    SHOPPING_CART = "#shopping_cart_container"

    def __init__(self, page: Page):
        super().__init__(page)

    def open_cart(self):
        self.page.locator(self.SHOPPING_CART).click() # SHOPP CART FUNC


class FormPage(BasePage):
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POST_CODE_INPUT = "#postal-code"
    CONTINUE_BTN = "#continue"

    def __init__(self, page: Page):
        super().__init__(page)

    def fill_form(self, first_name, last_name, post_code):
        self.page.locator(self.FIRST_NAME_INPUT).fill(first_name)
        self.page.locator(self.LAST_NAME_INPUT).fill(last_name)
        self.page.locator(self.POST_CODE_INPUT).fill(post_code)
        self.page.locator(self.CONTINUE_BTN).click()


class ConfirmationPage(BasePage):
    FINISH_BTN = "#finish"

    COMPLETE_MSG = "complete-header"
    BACK_HOME_BTN = "#back-to-products"

    def __init__(self, page: Page):
        super().__init__(page)

    def finish_checkout(self):
        self.page.locator(self.FINISH_BTN).click()

    def verify_success_message(self):
        self.isLoaded(self.COMPLETE_MSG)
        self.page.locator(self.BACK_HOME_BTN).click()












