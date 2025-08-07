from playwright.sync_api import Page, expect
from .base_page import BasePage
from ..pages.form_page import FormPage

class CartPage(BasePage):
    CHECKOUT_BTN = "#checkout"

    def __init__(self, page: Page):
        super().__init__(page)

    def goto_checkout(self):
        self.page.locator(self.CHECKOUT_BTN).click()
        return FormPage(self.page)

