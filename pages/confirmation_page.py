from playwright.sync_api import Page, expect
from .base_page import BasePage


class ConfirmationPage(BasePage):
    COMPLETE_MSG = "complete-header"
    BACK_HOME_BTN = "#back-to-products"

    TITLE = "title"

    def __init__(self, page: Page):
        super().__init__(page)

    def isLoaded(self):
        expect(self.page.get_by_test_id(self.TITLE)).to_contain_text("Checkout: Complete!")

    def verify_success_message(self):
        self.isLoaded()

    def goto_content_page(self):
        from ..pages.content_page import ContentPage

        self.page.locator(self.BACK_HOME_BTN).click()
        return ContentPage(self.page)
