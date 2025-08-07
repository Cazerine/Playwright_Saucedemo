from playwright.sync_api import Page, expect
from .base_page import BasePage

class ConfirmationPage(BasePage):
    COMPLETE_MSG = "complete-header"
    BACK_HOME_BTN = "#back-to-products"

    def isLoaded(self, element):
        expect(self.page.get_by_test_id(element)).to_be_visible()

    def __init__(self, page: Page):
        super().__init__(page)

    def verify_success_message(self):
        self.isLoaded(self.COMPLETE_MSG)
        self.page.locator(self.BACK_HOME_BTN).click()
