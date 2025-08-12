from playwright.sync_api import Page, expect
from .base_page import BasePage
from ..pages.checkout_page import CheckoutPage
import allure


class FormPage(BasePage):
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POST_CODE_INPUT = "#postal-code"
    CONTINUE_BTN = "#continue"

    TITLE = "title"

    def __init__(self, page: Page):
        super().__init__(page)

    def fill_form_and_submit(self, first_name, last_name, post_code):
        with allure.step('Fill the form'):
            self.page.locator(self.FIRST_NAME_INPUT).fill(first_name)
            self.page.locator(self.LAST_NAME_INPUT).fill(last_name)
            self.page.locator(self.POST_CODE_INPUT).fill(post_code)
        with allure.step('Click submit'):
            self.page.locator(self.CONTINUE_BTN).click()
            return CheckoutPage(self.page)

    def isLoaded(self):
        with allure.step('Check downloading page'):
            expect(self.page.get_by_test_id(self.TITLE)).to_contain_text("Checkout: Your Information")