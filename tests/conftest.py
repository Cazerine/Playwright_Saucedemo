import pytest
from playwright.sync_api import sync_playwright, Page
from ..pages.login_page import LoginPage
import allure

def pytest_configure(config):
    with sync_playwright() as p:
        p.selectors.set_test_id_attribute("data-test")

@pytest.fixture
def authorized_page(page: Page):
    with allure.step('Open'):
        login_page = LoginPage(page)
        login_page.open_page()
        login_page.authorize("standard_user", "secret_sauce")
        return page
