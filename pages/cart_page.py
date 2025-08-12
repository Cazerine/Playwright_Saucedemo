from playwright.sync_api import Page, expect
from .base_page import BasePage
from ..pages.form_page import FormPage
import allure

class CartPage(BasePage):
    CHECKOUT_BTN = "#checkout"
    TITLE = "title"

    def __init__(self, page: Page):
        super().__init__(page)

    def goto_checkout(self):
        self.page.locator(self.CHECKOUT_BTN).click()
        return FormPage(self.page)

    def isLoaded(self):
        with allure.step('Check downloading page'):
            expect(self.page.get_by_test_id(self.TITLE)).to_contain_text("Your Cart")

