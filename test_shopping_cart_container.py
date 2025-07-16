import pytest
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
from .locators import PageLocators

@pytest.fixture
def authorization(page: Page):
    url = 'https://www.saucedemo.com/'
    login = 'standard_user'
    password = 'secret_sauce'

    page.goto(url)
    page.locator(PageLocators.LOGIN).fill(login)
    page.locator(PageLocators.PASSWORD).fill(password)
    page.locator(PageLocators.LOGIN_BTN).click()

    yield

    page.close()

def add_item_to_cart(page: Page, number: int):

    page.locator(f'//div[@class="inventory_list"]/div[{number}]//button').click()

def test_add_multiple_item_to_cart_and_remove(page: Page, authorization):
    add_item_to_cart(page, 1)
    add_item_to_cart(page, 2)
    add_item_to_cart(page, 3)

    expect(page.get_by_test_id(PageLocators.CART_BADGE)).to_contain_text('3')
    page.locator('//div[@class="inventory_list"]/div[1]//button').click() #удаление
    #
    expect(page.get_by_test_id(PageLocators.CART_BADGE)).to_contain_text('2')

def test_name_filter(page: Page, authorization):
    page.get_by_test_id(PageLocators.SORT).select_option('az')

    name1 = page.locator(PageLocators.NAME1).text_content()
    name2 = page.locator(PageLocators.NAME2).text_content()
    name3 = page.locator(PageLocators.NAME3).text_content()
    name4 = page.locator(PageLocators.NAME4).text_content()
    name5 = page.locator(PageLocators.NAME5).text_content()
    name6 = page.locator(PageLocators.NAME6).text_content()

    assert name1 < name2 < name3 < name4 < name5 < name6, 'Wrong filtration A-Z'

    page.get_by_test_id(PageLocators.SORT).select_option('za') #сортировка в обратном порядке

    name1 = page.locator(PageLocators.NAME1).text_content()
    name2 = page.locator(PageLocators.NAME2).text_content()
    name3 = page.locator(PageLocators.NAME3).text_content()
    name4 = page.locator(PageLocators.NAME4).text_content()
    name5 = page.locator(PageLocators.NAME5).text_content()
    name6 = page.locator(PageLocators.NAME6).text_content()

    assert name1 > name2 > name3 > name4 > name5 > name6, 'Wrong filtration Z-A'

def test_price_filter(page: Page, authorization):
    page.get_by_test_id(PageLocators.SORT).select_option('lohi')

    price1 = page.locator(PageLocators.PRICE1).text_content()
    price2 = page.locator(PageLocators.PRICE2).text_content()
    price3 = page.locator(PageLocators.PRICE3).text_content()
    price4 = page.locator(PageLocators.PRICE4).text_content()
    price5 = page.locator(PageLocators.PRICE5).text_content()
    price6 = page.locator(PageLocators.PRICE6).text_content()

    assert float(price1[1:]) <= float(price2[1:]) <= float(price3[1:]) <= float(price4[1:]) <= float(price5[1:]) <= float(price6[1:]), 'Wrong filtration ASC'

    page.get_by_test_id(PageLocators.SORT).select_option('hilo') #сортировка в обратном порядке

    price1 = page.locator(PageLocators.PRICE1).text_content()
    price2 = page.locator(PageLocators.PRICE2).text_content()
    price3 = page.locator(PageLocators.PRICE3).text_content()
    price4 = page.locator(PageLocators.PRICE4).text_content()
    price5 = page.locator(PageLocators.PRICE5).text_content()
    price6 = page.locator(PageLocators.PRICE6).text_content()

    assert float(price1[1:]) >= float(price2[1:]) >= float(price3[1:]) >= float(price4[1:]) >= float(price5[1:]) >= float(price6[1:]), 'Wrong filtration DESC'

#pytest -s -v test_shopping_cart_container.py