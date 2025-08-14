import pytest
from playwright.sync_api import Page
from ..pages.login_page import LoginPage
import allure

@allure.feature('Login')
class TestLogin:
    @pytest.mark.parametrize("login, password, valid", [
         ("standard_user", 'secret_sauce', True),
         ("locked_out_user", 'secret_sauce', False),
         ("problem_user", 'secret_sauce', True),
         ("performance_glitch_user", 'secret_sauce', True),
         ("error_user", 'secret_sauce', True),
         ("visual_user", 'secret_sauce', True),
         ("not_existing_user", 'secret_sauce', False)
     ])
    def test_authorization_multiple_login(self, page: Page, login, password, valid):

        login_page = LoginPage(page)
        login_page.login(login, password, valid)

# pytest -s -v test_login_swag_labs.py






