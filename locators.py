from playwright.sync_api import Page, expect

class PageLocators:

    LOGIN = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"

    CART_BADGE = 'shopping-cart-badge'
    INVENTORY_LIST = '//div[@class="inventory_list"]'

    SORT = "product-sort-container"

    NAME1 = '//div[@class="inventory_list"]/div[1]//div[@class="inventory_item_name "]'
    NAME2 = '//div[@class="inventory_list"]/div[2]//div[@class="inventory_item_name "]'
    NAME3 = '//div[@class="inventory_list"]/div[3]//div[@class="inventory_item_name "]'
    NAME4 = '//div[@class="inventory_list"]/div[4]//div[@class="inventory_item_name "]'
    NAME5 = '//div[@class="inventory_list"]/div[5]//div[@class="inventory_item_name "]'
    NAME6 = '//div[@class="inventory_list"]/div[6]//div[@class="inventory_item_name "]'

    PRICE1 = '//div[@class="inventory_list"]/div[1]//div[@class="inventory_item_price"]'
    PRICE2 = '//div[@class="inventory_list"]/div[2]//div[@class="inventory_item_price"]'
    PRICE3 = '//div[@class="inventory_list"]/div[3]//div[@class="inventory_item_price"]'
    PRICE4 = '//div[@class="inventory_list"]/div[4]//div[@class="inventory_item_price"]'
    PRICE5 = '//div[@class="inventory_list"]/div[5]//div[@class="inventory_item_price"]'
    PRICE6 = '//div[@class="inventory_list"]/div[6]//div[@class="inventory_item_price"]'



