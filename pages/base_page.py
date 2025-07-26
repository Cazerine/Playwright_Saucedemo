from playwright.sync_api import Page, expect


class BasePage():
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://www.saucedemo.com'

    def open_page(self):
        url = 'https://www.saucedemo.com/'
        self.page.goto(url)

    def isLoaded_LOGO(self, element):
        expect(self.page.locator(element)).to_be_visible()

    def isLoaded(self, element):
        expect(self.page.get_by_test_id(element)).to_be_visible() #лого фильтров data-test="product-sort-container"
        expect(self.page.get_by_test_id(element)).to_be_visible() #проверка итем есть контейнер id="inventory_container"


    def get_title(self):
        return self.page.title()

