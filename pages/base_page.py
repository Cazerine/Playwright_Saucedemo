from playwright.sync_api import Page

class BasePage():
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://www.saucedemo.com'

    def open_page(self):
        self.page.goto(self.url)

    def get_title(self):
        return self.page.title()

