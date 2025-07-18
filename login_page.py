from .base_page import BasePage
from .locators import PageLocators
from playwright.sync_api import Page, expect
import pytest


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def authorization(self, login, password, valid):
        self.page.locator(PageLocators.LOGIN).fill(login)
        self.page.locator(PageLocators.PASSWORD).fill(password)
        self.page.locator(PageLocators.LOGIN_BTN).click()

        if valid:
            expect(self.page.locator('.app_logo')).to_contain_text('Swag Labs')
        else:
            expect(self.page.locator('.error-message-container.error')).to_contain_text('Epic sadface')




