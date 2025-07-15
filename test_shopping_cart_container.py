import pytest
from playwright.sync_api import Page, expect

@pytest.fixture
def authorization(page: Page):
    url = 'https://www.saucedemo.com/'
    login = 'standard_user'
    password = 'secret_sauce'

    page.goto(url)
    page.get_by_placeholder('Username').fill(login)
    page.get_by_placeholder('Password').fill(password)
    page.locator("#login-button").click()

    yield

    page.close()

def adding_three_items_to_shopping_cart_container(page: Page):
    page.locator('//div[@class="inventory_list"]/div[1]//button').click()
    page.locator('//div[@class="inventory_list"]/div[2]//button').click()
    page.locator('//div[@class="inventory_list"]/div[3]//button').click()

def test_adding_three_items_to_shopping_cart_container(page: Page, authorization):
    adding_three_items_to_shopping_cart_container(page)

    expect(page.locator('//span[@class="shopping_cart_badge"]')).to_contain_text('3')

def test_removing_from_shopping_cart_container(page: Page, authorization):
    adding_three_items_to_shopping_cart_container(page)

    page.locator('//div[@class="inventory_list"]/div[1]//button').click()

    expect(page.locator('//span[@class="shopping_cart_badge"]')).to_contain_text('2')

def test_filtration_a_to_z(page: Page, authorization):
    page.locator('//select[@class="product_sort_container"]').select_option('az')

    name1 = page.locator('//div[@class="inventory_list"]/div[1]//div[@class="inventory_item_name "]').text_content()
    name2 = page.locator('//div[@class="inventory_list"]/div[2]//div[@class="inventory_item_name "]').text_content()
    name3 = page.locator('//div[@class="inventory_list"]/div[3]//div[@class="inventory_item_name "]').text_content()
    name4 = page.locator('//div[@class="inventory_list"]/div[4]//div[@class="inventory_item_name "]').text_content()
    name5 = page.locator('//div[@class="inventory_list"]/div[5]//div[@class="inventory_item_name "]').text_content()
    name6 = page.locator('//div[@class="inventory_list"]/div[6]//div[@class="inventory_item_name "]').text_content()

    assert name1 < name2 < name3 < name4 < name5 < name6, 'Wrong filtration'

def test_filtration_z_to_a(page: Page, authorization):
    page.locator('//select[@class="product_sort_container"]').select_option('za')

    name1 = page.locator('//div[@class="inventory_list"]/div[1]//div[@class="inventory_item_name "]').text_content()
    name2 = page.locator('//div[@class="inventory_list"]/div[2]//div[@class="inventory_item_name "]').text_content()
    name3 = page.locator('//div[@class="inventory_list"]/div[3]//div[@class="inventory_item_name "]').text_content()
    name4 = page.locator('//div[@class="inventory_list"]/div[4]//div[@class="inventory_item_name "]').text_content()
    name5 = page.locator('//div[@class="inventory_list"]/div[5]//div[@class="inventory_item_name "]').text_content()
    name6 = page.locator('//div[@class="inventory_list"]/div[6]//div[@class="inventory_item_name "]').text_content()

    assert name1 > name2 > name3 > name4 > name5 > name6, 'Wrong filtration'

def test_filtration_low_to_high(page: Page, authorization):
    page.locator('//select[@class="product_sort_container"]').select_option('lohi')

    price1 = page.locator('//div[@class="inventory_list"]/div[1]//div[@class="inventory_item_price"]').text_content()
    price2 = page.locator('//div[@class="inventory_list"]/div[2]//div[@class="inventory_item_price"]').text_content()
    price3 = page.locator('//div[@class="inventory_list"]/div[3]//div[@class="inventory_item_price"]').text_content()
    price4 = page.locator('//div[@class="inventory_list"]/div[4]//div[@class="inventory_item_price"]').text_content()
    price5 = page.locator('//div[@class="inventory_list"]/div[5]//div[@class="inventory_item_price"]').text_content()
    price6 = page.locator('//div[@class="inventory_list"]/div[6]//div[@class="inventory_item_price"]').text_content()

    assert float(price1[1:]) <= float(price2[1:]) <= float(price3[1:]) <= float(price4[1:]) <= float(price5[1:]) <= float(price6[1:]), 'Wrong filtration'

def test_filtration_high_to_low(page: Page, authorization):
    page.locator('//select[@class="product_sort_container"]').select_option('hilo')

    price1 = page.locator('//div[@class="inventory_list"]/div[1]//div[@class="inventory_item_price"]').text_content()
    price2 = page.locator('//div[@class="inventory_list"]/div[2]//div[@class="inventory_item_price"]').text_content()
    price3 = page.locator('//div[@class="inventory_list"]/div[3]//div[@class="inventory_item_price"]').text_content()
    price4 = page.locator('//div[@class="inventory_list"]/div[4]//div[@class="inventory_item_price"]').text_content()
    price5 = page.locator('//div[@class="inventory_list"]/div[5]//div[@class="inventory_item_price"]').text_content()
    price6 = page.locator('//div[@class="inventory_list"]/div[6]//div[@class="inventory_item_price"]').text_content()

    assert float(price1[1:]) >= float(price2[1:]) >= float(price3[1:]) >= float(price4[1:]) >= float(price5[1:]) >= float(price6[1:]), 'Wrong filtration'

#pytest -s -v test_shopping_cart_container.py