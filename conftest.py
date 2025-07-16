import pytest
from playwright.sync_api import sync_playwright

def pytest_configure(config):
    with sync_playwright() as p:
        p.selectors.set_test_id_attribute("data-test")