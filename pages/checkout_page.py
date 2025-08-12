import pytest
from playwright.sync_api import Page, expect
from .base_page import BasePage
from ..pages.confirmation_page import ConfirmationPage
import allure

class CheckoutPage(BasePage):
    ITEM_NAME = "inventory-item-name"
    ITEM_PRICE = "inventory-item-price"

    FINISH_BTN = "#finish"

    TITLE = "title"

    def __init__(self, page: Page):
        super().__init__(page)

    def isLoaded(self):
        with allure.step('Check downloading page'):
            expect(self.page.get_by_test_id(self.TITLE)).to_contain_text("Checkout: Overview")

    def get_item_name(self, number):
        return self.page.get_by_test_id(self.ITEM_NAME).nth(number).text_content()

    def get_item_price(self, number):
        return self.page.get_by_test_id(self.ITEM_PRICE).nth(number).text_content()

    def get_name_from_item_card(self, number):
        name_added = self.get_item_name(number)
        return name_added

    def get_price_from_item_card(self, number):
        price_added = str(self.get_item_price(number))
        return price_added

    def verify_checkout(self, number):
        with allure.step('Verify checkout'):

            expect(self.page.get_by_test_id(self.ITEM_NAME)).to_contain_text(self.get_name_from_item_card(number))  # проверка названия
            expect(self.page.get_by_test_id(self.ITEM_PRICE)).to_contain_text(self.get_price_from_item_card(number))  # проверка цены

    def finish_checkout(self):
        with allure.step('Click Finish'):
            self.page.locator(self.FINISH_BTN).click()
            return ConfirmationPage(self.page)













