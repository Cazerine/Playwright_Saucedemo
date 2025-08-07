from playwright.sync_api import Page, expect
from .base_page import BasePage


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