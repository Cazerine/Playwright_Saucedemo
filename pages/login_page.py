from .base_page import BasePage
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def login(self, login, password, valid):
        self.open_page()
        self.authorize(login, password)

        LOGO = '.app_logo'
        ERROR = 'error'

        if valid:
            expect(self.page.locator(LOGO)).to_contain_text('Swag Labs')
        else:
            expect(self.page.get_by_test_id(ERROR)).to_contain_text('Epic sadface')







