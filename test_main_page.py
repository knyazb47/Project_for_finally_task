import pytest

from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage

link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
@pytest.mark.login_quest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        page.should_be_login_link()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_see_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.click_button_view_basket()
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.item_is_not_basket()
    page_basket.message_basket_empty()



