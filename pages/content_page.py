from .base_page import BasePage
from playwright.sync_api import Page, expect
from ..pages.cart_page import CartPage
import allure

class ContentPage(BasePage):
    SUBTITLE = 'title'
    FILTER_BTN = 'active-option'
    INVENTORY_LIST = 'inventory-list'
    SORT_OPTION = 'product-sort-container'
    ITEM_DESC = 'inventory-item-description'
    REMOVE_FIRST_ITEM = '#remove-sauce-labs-backpack'
    CART_BADGE = 'shopping-cart-badge'
    ITEM_BACKPACK = "#item_4_title_link"
    ITEM_CART = "#inventory_item_container"
    BACK_BTN = "#back-to-products"
    ITEM_CONTAINER = "inventory-container"
    SHOPPING_CART = "#shopping_cart_container"

    def __init__(self, page: Page):
        super().__init__(page)

    def isLoaded(self):
        with allure.step('Check downloading page'):
            expect(self.page.get_by_test_id(self.ITEM_CONTAINER)).to_be_visible()

    def verify_filter(self, option, expected_text): #фильтры
        with allure.step('Filter'):
            self.page.get_by_test_id(self.SORT_OPTION).select_option(option)
        with allure.step('Verify filter'):
            expect(self.page.get_by_test_id(self.FILTER_BTN)).to_contain_text(expected_text)

    def add_item_to_cart(self, number: int):
        with allure.step('Add item to cart'):
            item = self.page.get_by_test_id(self.ITEM_DESC).nth(number)
            item.get_by_role('button').click()

    def verify_shopping_cart(self, count = 3): #корзина
        with allure.step('Verify count of added items'):
            expect(self.page.get_by_test_id(self.CART_BADGE)).to_contain_text(str(count))

        if count == 0:
            return
        else:
            self.page.locator(self.REMOVE_FIRST_ITEM).click()  # удаление первого товара

        with allure.step('Verify count of items after remove'):
            expect(self.page.get_by_test_id(self.CART_BADGE)).to_contain_text(str(count-1))

    def verify_item_card_goto_and_back(self): #карточка товара (открытие и возврат)
        self.page.locator(self.ITEM_BACKPACK).click()
        expect(self.page.locator(self.ITEM_CART)).to_be_visible() #проверка перехода на карточку товара

        self.page.locator(self.BACK_BTN).click()
        self.isLoaded()

    def open_cart(self):
        self.page.locator(self.SHOPPING_CART).click() # SHOPP CART FUNC
        return CartPage(self.page)



    












