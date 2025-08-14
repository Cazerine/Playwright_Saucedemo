from ..pages.content_page import ContentPage
import allure

@allure.feature('Flow')
class TestCheckoutFlow:
    def test_checkout_flow(self, authorized_page):
        content_page = ContentPage(authorized_page)
        content_page.add_item_to_cart(0) #добавили первый товар
        content_page.isLoaded()

        cart_page = content_page.open_cart()
        cart_page.isLoaded()

        form_page = cart_page.goto_checkout()
        form_page.isLoaded()

        checkout_page = form_page.fill_form_and_submit('Test', 'Test', '000000')
        checkout_page.isLoaded()
        checkout_page.verify_checkout(0)

        confirmation_page = checkout_page.finish_checkout()
        confirmation_page.verify_success_message()

        content_page = confirmation_page.goto_content_page()
        content_page.isLoaded() # проверяем, что страница с контентом загрузилась

# pytest -s -v test_checkout_page.py
