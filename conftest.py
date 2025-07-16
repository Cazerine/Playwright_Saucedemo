import pytest

def pytest_configure(config):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        p.selectors.set_test_id_attribute("data-test")