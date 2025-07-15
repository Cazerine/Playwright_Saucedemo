import pytest
from playwright.sync_api import Page, expect

url = 'https://www.saucedemo.com/'

@pytest.mark.parametrize("login, password, valid", [
    ("standard_user", 'secret_sauce', True),
    ("locked_out_user", 'secret_sauce', False),
    ("problem_user", 'secret_sauce', True),
    ("performance_glitch_user", 'secret_sauce', True),
    ("error_user", 'secret_sauce', True),
    ("visual_user", 'secret_sauce', True),
    ("not_existing_user", 'secret_sauce', False)
])
def test_authorization(page: Page, login, password, valid):
    page.goto(url)

    page.get_by_placeholder('Username').fill(login)
    page.get_by_placeholder('Password').fill(password)
    page.locator("#login-button").click()

    if valid:
        expect(page.locator('.app_logo')).to_contain_text('Swag Labs')
    else:
        expect(page.locator('.error-message-container.error')).to_contain_text('Epic sadface')











# pytest -s -v test_login_swag_labs.py






