from playwright.sync_api import Page, expect

class BasePage():
    LOGO = '.app_logo'

    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://www.saucedemo.com'

    def open_page(self):
        url = 'https://www.saucedemo.com/'
        self.page.goto(url)

    def isLoaded(self):
        expect(self.page.locator(self.LOGO)).to_be_visible()

    def get_title(self):
        return self.page.title()

