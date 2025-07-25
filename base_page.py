from playwright.sync_api import Page

class BasePage():
    def __init__(self, page: Page):
        self.page = page

    def open_page(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

