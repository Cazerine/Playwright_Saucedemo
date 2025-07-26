from .base_page import BasePage
from playwright.sync_api import Page, expect
from ..pages.login_page import LoginPage


class ContentPage(BasePage):
    SUBTITLE = 'title'
    FILTER_BTN = 'active-option'
    INVENTORY_LIST = 'inventory-list'
    SORT_OPTION = 'product-sort-container'
    ITEM = 'inventory-item-description'
    REM_ITEM1 = '#remove-sauce-labs-backpack'
    CART_BADGE = 'shopping-cart-badge'
    ITEM_BACKPACK = "#item_4_title_link"
    ITEM_CART = "#inventory_item_container"
    BACK = "#back-to-products"

    def __init__(self, page: Page):
        super().__init__(page)

    # def verify_content_page_open(self):

        # expect(self.page.locator(LoginPage.LOGO)).to_be_visible() #проверка заголовка PageLocators.LOGO
        # expect(self.page.get_by_test_id(self.SUBTITLE)).to_contain_text('Products') #подзаголовок продактс
        # expect(self.page.get_by_test_id(self.FILTER_BTN)).to_be_visible() #лого фильтров data-test="product-sort-container"
        # expect(self.page.get_by_test_id(self.INVENTORY_LIST)).to_be_visible() #проверка итем есть контейнер id="inventory_container"

    def verify_filter(self, option, expected_text): #фильтры
        self.page.get_by_test_id(self.SORT_OPTION).select_option(option)
        expect(self.page.get_by_test_id(self.FILTER_BTN)).to_contain_text(expected_text)

    def add_item_to_cart(self, number: int):
        item = self.page.get_by_test_id(self.ITEM).nth(number)
        item.get_by_role('button').click()

    def verify_shopping_cart(self, count = 3): #корзина
        expect(self.page.get_by_test_id(self.CART_BADGE)).to_contain_text(str(count))

        self.page.locator(self.REM_ITEM1).click()  # удаление первого товара

        expect(self.page.get_by_test_id(self.CART_BADGE)).to_contain_text(str(count -1))

    def verify_item_card_goto_and_back(self): #карточка товара (открытие и возврат)
        self.page.locator(self.ITEM_BACKPACK).click()
        expect(self.page.locator(self.ITEM_CART)).to_be_visible() #проверка перехода на карточку товара

        self.page.locator(self.BACK).click()
        expect(self.page.get_by_test_id(self.INVENTORY_LIST)).to_be_visible()  # проверка итем есть контейнер



    












