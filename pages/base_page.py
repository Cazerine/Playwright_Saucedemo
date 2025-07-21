from playwright.sync_api import Page

class BasePage():
    def __init__(self, page: Page, url = 'https://www.saucedemo.com/'):
        self.page = page
        self.url = url

    def open_page(self):
        self.page.goto(self.url)

    def authorize(self, login, password):
        LOGIN = '#user-name'
        PASSWORD = '#password'
        LOGIN_BTN = '#login-button'

        self.page.locator(LOGIN).fill(login)
        self.page.locator(PASSWORD).fill(password)
        self.page.locator(LOGIN_BTN).click()

    def get_title(self):
        return self.page.title()

