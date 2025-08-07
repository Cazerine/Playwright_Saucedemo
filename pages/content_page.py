from .base_page import BasePage
from playwright.sync_api import Page, expect
from ..pages.cart_page import CartPage

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
    INVENTORY_CNTR = "inventory-container"
    SHOPPING_CART = "#shopping_cart_container"

    def __init__(self, page: Page):
        super().__init__(page)

    def isLoaded(self):
        expect(self.page.get_by_test_id(self.INVENTORY_CNTR)).to_be_visible()

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
        self.isLoaded()
        #expect(self.page.get_by_test_id(self.INVENTORY_LIST)).to_be_visible()  # проверка итем есть контейнер

    def open_cart(self):
        self.page.locator(self.SHOPPING_CART).click() # SHOPP CART FUNC
        return CartPage(self.page)



    












