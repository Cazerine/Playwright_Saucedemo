from playwright.sync_api import Page
from .locators import PageLocators

class BasePage():
    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        url = 'https://www.saucedemo.com/'
        self.page.goto(url)

    def authorize(self, login, password):
        self.page.locator(PageLocators.LOGIN).fill(login)
        self.page.locator(PageLocators.PASSWORD).fill(password)
        self.page.locator(PageLocators.LOGIN_BTN).click()

    def get_title(self):
        return self.page.title()

