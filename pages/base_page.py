from playwright.sync_api import Page, expect


class BasePage():
    LOGO = '.app_logo'
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://www.saucedemo.com'

    def open_page(self):
        url = 'https://www.saucedemo.com/'
        self.page.goto(url)

    def isLoaded_LOGO(self):
        expect(self.page.locator(self.LOGO)).to_be_visible()

    def isLoaded(self, element):
        expect(self.page.get_by_test_id(element)).to_be_visible()

    # def isLoaded_by_locator(self, element):
    #     expect(self.page.locator(element)).to_be_visible()

    def get_title(self):
        return self.page.title()

