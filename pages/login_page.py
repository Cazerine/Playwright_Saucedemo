from .base_page import BasePage
from .locators import PageLocators
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def login(self, login, password, valid):
        self.open_page()
        self.authorize(login, password)

        if valid:
            expect(self.page.locator(PageLocators.LOGO)).to_contain_text('Swag Labs')
        else:
            expect(self.page.get_by_test_id(PageLocators.ERROR)).to_contain_text('Epic sadface')

    def catalog_page(self, login="standard_user", password="secret_sauce"):
        self.open_page()
        self.authorize(login, password)


        expect(self.page.locator(PageLocators.LOGO)).to_be_visible() #проверка заголовка PageLocators.LOGO
        expect(self.page.get_by_test_id(PageLocators.SUBTITLE)).to_contain_text('Products') #подзаголовок продактс data-test="title" текст Products
        expect(self.page.get_by_test_id(PageLocators.FILTER)).to_be_visible() #лого фильтров data-test="product-sort-container"
        expect(self.page.get_by_test_id(PageLocators.INVENTORY_LIST)).to_be_visible() #проверка итем есть контейнер id="inventory_container"







