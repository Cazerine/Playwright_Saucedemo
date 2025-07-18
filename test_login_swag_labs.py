import pytest
from playwright.sync_api import Page, expect
from .base_page import BasePage
from .locators import PageLocators
from .login_page import LoginPage

@pytest.mark.parametrize("login, password, valid", [
     ("standard_user", 'secret_sauce', True),
     ("locked_out_user", 'secret_sauce', False),
     ("problem_user", 'secret_sauce', True),
     ("performance_glitch_user", 'secret_sauce', True),
     ("error_user", 'secret_sauce', True),
     ("visual_user", 'secret_sauce', True),
     ("not_existing_user", 'secret_sauce', False)
 ])
def test_authorization_multiple_login(page: Page, login, password, valid):
    url = 'https://www.saucedemo.com/'

    login_page = LoginPage(page)
    login_page.open_page(url)

    login_page.authorization(login, password, valid)



# pytest -s -v test_login_swag_labs.py






