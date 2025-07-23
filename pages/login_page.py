from .base_page import BasePage
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    LOGO = '.app_logo'
    ERROR = 'error'

    LOGIN = '#user-name'
    PASSWORD = '#password'
    LOGIN_BTN = '#login-button'

    def __init__(self, page: Page):
        super().__init__(page)

    def authorize(self, login, password):
        self.page.locator(self.LOGIN).fill(login)
        self.page.locator(self.PASSWORD).fill(password)
        self.page.locator(self.LOGIN_BTN).click()

    def login(self, login, password, valid):
        self.open_page()
        self.authorize(login, password)

        if valid:
            expect(self.page.locator(self.LOGO)).to_contain_text('Swag Labs')
        else:
            expect(self.page.get_by_test_id(self.ERROR)).to_contain_text('Epic sadface')







