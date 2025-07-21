from .base_page import BasePage
from .locators import PageLocators
from playwright.sync_api import Page, expect


class ContentPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def filter(self): #фильтры
        self.page.get_by_test_id(PageLocators.SORT).select_option('az')
        expect(self.page.get_by_test_id(PageLocators.FILTER)).to_contain_text("Name (A to Z)")

        self.page.get_by_test_id(PageLocators.SORT).select_option('za')
        expect(self.page.get_by_test_id(PageLocators.FILTER)).to_contain_text("Name (Z to A)")

        self.page.get_by_test_id(PageLocators.SORT).select_option('lohi')
        expect(self.page.get_by_test_id(PageLocators.FILTER)).to_contain_text("Price (low to high)")

        self.page.get_by_test_id(PageLocators.SORT).select_option('hilo')
        expect(self.page.get_by_test_id(PageLocators.FILTER)).to_contain_text("Price (high to low)")

    def add_item_to_cart(self, number: int):
        item = self.page.get_by_test_id(PageLocators.ITEM).nth(number)
        item.get_by_role('button').click()

    def shopping_cart(self): #корзина
        self.add_item_to_cart(0)
        self.add_item_to_cart(1)
        self.add_item_to_cart(2)

        expect(self.page.get_by_test_id(PageLocators.CART_BADGE)).to_contain_text('3')

        self.page.locator(PageLocators.REM_ITEM1).click()  # удаление первого товара

        expect(self.page.get_by_test_id(PageLocators.CART_BADGE)).to_contain_text('2')

    def burger_menu_all_items(self): #бургер-меню
        expect(self.page.locator(PageLocators.BURGER_MENU)).to_be_visible() #проверка, что элемент есть

        self.page.locator(PageLocators.ITEM_BACKPACK).click()
        self.page.locator(PageLocators.BURGER_MENU).click()
        self.page.locator(PageLocators.ALL_ITEMS).click()
        expect(self.page.get_by_test_id(PageLocators.INVENTORY_LIST)).to_be_visible()  # проверка итем есть контейнер

    def burger_menu_about(self):

        self.page.locator(PageLocators.BURGER_MENU).click()
        self.page.locator(PageLocators.ABOUT).click()
        expect(self.page).to_have_url('https://saucelabs.com/') #проверка перехода по кнопке about

    def burger_menu_logout(self):

        self.page.locator(PageLocators.BURGER_MENU).click()
        self.page.locator(PageLocators.LOGOUT).click()
        expect(self.page.locator(PageLocators.ROOT)).to_be_visible() #проверка перехода на страницу логина

    def item_cart(self): #карточка товара (открытие и возврат)
        self.page.locator(PageLocators.ITEM_BACKPACK).click()
        expect(self.page.locator(PageLocators.ITEM_CART)).to_be_visible() #проверка перехода на карточку товара

        self.page.locator(PageLocators.BACK).click()
        expect(self.page.get_by_test_id(PageLocators.INVENTORY_LIST)).to_be_visible()  # проверка итем есть контейнер



    












