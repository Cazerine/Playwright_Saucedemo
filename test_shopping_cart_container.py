import pytest
from playwright.sync_api import Page, expect
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

    item = page.get_by_test_id(PageLocators.ITEM).nth(number)
    item.get_by_role('button').click()

def test_add_multiple_item_to_cart_and_remove(page: Page, authorization):
    add_item_to_cart(page, 0)
    add_item_to_cart(page, 1)
    add_item_to_cart(page, 2)

    expect(page.get_by_test_id(PageLocators.CART_BADGE)).to_contain_text('3')

    page.locator(PageLocators.REM_ITEM1).click() #удаление первого товара

    expect(page.get_by_test_id(PageLocators.CART_BADGE)).to_contain_text('2')

def test_name_filter(page: Page, authorization):
    page.get_by_test_id(PageLocators.SORT).select_option('az')

    name1 = page.get_by_test_id(PageLocators.NAME).nth(0).text_content()
    name2 = page.get_by_test_id(PageLocators.NAME).nth(1).text_content()
    name3 = page.get_by_test_id(PageLocators.NAME).nth(2).text_content()
    name4 = page.get_by_test_id(PageLocators.NAME).nth(3).text_content()
    name5 = page.get_by_test_id(PageLocators.NAME).nth(4).text_content()
    name6 = page.get_by_test_id(PageLocators.NAME).nth(5).text_content()

    assert name1 < name2 < name3 < name4 < name5 < name6, 'Wrong filtration A-Z'

    page.get_by_test_id(PageLocators.SORT).select_option('za') #сортировка в обратном порядке

    name1 = page.get_by_test_id(PageLocators.NAME).nth(0).text_content()
    name2 = page.get_by_test_id(PageLocators.NAME).nth(1).text_content()
    name3 = page.get_by_test_id(PageLocators.NAME).nth(2).text_content()
    name4 = page.get_by_test_id(PageLocators.NAME).nth(3).text_content()
    name5 = page.get_by_test_id(PageLocators.NAME).nth(4).text_content()
    name6 = page.get_by_test_id(PageLocators.NAME).nth(5).text_content()

    assert name1 > name2 > name3 > name4 > name5 > name6, 'Wrong filtration Z-A'

def test_price_filter(page: Page, authorization):
    page.get_by_test_id(PageLocators.SORT).select_option('lohi')

    price1 = page.get_by_test_id(PageLocators.PRICE).nth(0).text_content()
    price2 = page.get_by_test_id(PageLocators.PRICE).nth(1).text_content()
    price3 = page.get_by_test_id(PageLocators.PRICE).nth(2).text_content()
    price4 = page.get_by_test_id(PageLocators.PRICE).nth(3).text_content()
    price5 = page.get_by_test_id(PageLocators.PRICE).nth(4).text_content()
    price6 = page.get_by_test_id(PageLocators.PRICE).nth(5).text_content()

    assert float(price1[1:]) <= float(price2[1:]) <= float(price3[1:]) <= float(price4[1:]) <= float(price5[1:]) <= float(price6[1:]), 'Wrong filtration ASC'

    page.get_by_test_id(PageLocators.SORT).select_option('hilo') #сортировка в обратном порядке

    price1 = page.get_by_test_id(PageLocators.PRICE).nth(0).text_content()
    price2 = page.get_by_test_id(PageLocators.PRICE).nth(1).text_content()
    price3 = page.get_by_test_id(PageLocators.PRICE).nth(2).text_content()
    price4 = page.get_by_test_id(PageLocators.PRICE).nth(3).text_content()
    price5 = page.get_by_test_id(PageLocators.PRICE).nth(4).text_content()
    price6 = page.get_by_test_id(PageLocators.PRICE).nth(5).text_content()

    assert float(price1[1:]) >= float(price2[1:]) >= float(price3[1:]) >= float(price4[1:]) >= float(price5[1:]) >= float(price6[1:]), 'Wrong filtration DESC'

#pytest -s -v test_shopping_cart_container.py