from .base_page import BasePage
from playwright.sync_api import Page, expect


class ContentPage(BasePage):
    class Locators:
        LOGO = '.app_logo'
        SUBTITLE = 'title'
        FILTER = 'active-option'
        INVENTORY_LIST = 'inventory-list'
        SORT = 'product-sort-container'
        ITEM = 'inventory-item-description'
        REM_ITEM1 = '#remove-sauce-labs-backpack'
        CART_BADGE = 'shopping-cart-badge'
        ITEM_BACKPACK = "#item_4_title_link"
        ITEM_CART = "#inventory_item_container"
        BACK = "#back-to-products"

    def __init__(self, page: Page):
        super().__init__(page)

    def verify_content_page_open(self):
        expect(self.page.locator(self.Locators.LOGO)).to_be_visible() #проверка заголовка PageLocators.LOGO
        expect(self.page.get_by_test_id(self.Locators.SUBTITLE)).to_contain_text('Products') #подзаголовок продактс
        expect(self.page.get_by_test_id(self.Locators.FILTER)).to_be_visible() #лого фильтров data-test="product-sort-container"
        expect(self.page.get_by_test_id(self.Locators.INVENTORY_LIST)).to_be_visible() #проверка итем есть контейнер id="inventory_container"

    def verify_filter(self, option, expected_text): #фильтры
        self.page.get_by_test_id(self.Locators.SORT).select_option(option)
        expect(self.page.get_by_test_id(self.Locators.FILTER)).to_contain_text(expected_text)

    def add_item_to_cart(self, number: int):
        item = self.page.get_by_test_id(self.Locators.ITEM).nth(number)
        item.get_by_role('button').click()

    def verify_shopping_cart(self): #корзина
        expect(self.page.get_by_test_id(self.Locators.CART_BADGE)).to_contain_text('3')

        self.page.locator(self.Locators.REM_ITEM1).click()  # удаление первого товара

        expect(self.page.get_by_test_id(self.Locators.CART_BADGE)).to_contain_text('2')

    def verify_item_cart_goto_and_back(self): #карточка товара (открытие и возврат)
        self.page.locator(self.Locators.ITEM_BACKPACK).click()
        expect(self.page.locator(self.Locators.ITEM_CART)).to_be_visible() #проверка перехода на карточку товара

        self.page.locator(self.Locators.BACK).click()
        expect(self.page.get_by_test_id(self.Locators.INVENTORY_LIST)).to_be_visible()  # проверка итем есть контейнер



    












