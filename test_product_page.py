from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        registration = LoginPage(browser, link)
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + 'K!@'
        registration.open()
        registration.go_to_login_page()
        registration.register_new_user(email,password)
        registration.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = MainPage(browser, link)
        page.open()
        check_basket = ProductPage(browser, browser.current_url)
        check_basket.should_not_be_success_message()
        page.clik_add_to_basket()
        page.solve_quiz_and_get_code()
        check_basket.should_be_product_page()

    def test_user_cant_see_success_message(self, browser):
        page = MainPage(browser, link)
        page.open()
        check_basket = ProductPage(browser, browser.current_url)
        check_basket.should_not_be_success_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = MainPage(browser, link)
    page.open()
    page.clik_add_to_basket()
    page.solve_quiz_and_get_code()
    check_basket = ProductPage(browser, browser.current_url)
    check_basket.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = MainPage(browser, link)
    page.open()
    page.clik_add_to_basket()
    page.solve_quiz_and_get_code()
    check_basket = ProductPage(browser, browser.current_url)
    check_basket.should_success_message_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = MainPage(browser, link)
    page.open()
    page.click_button_view_basket()
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.item_is_not_basket()
    page_basket.message_basket_empty()
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = MainPage(browser, link)
    page.open()
    check_basket = ProductPage(browser, browser.current_url)
    check_basket.should_not_be_success_message()
    page.clik_add_to_basket()
    page.solve_quiz_and_get_code()
    check_basket.should_be_product_page()

def test_guest_cant_see_success_message(browser):
    page = MainPage(browser, link)
    page.open()
    check_basket = ProductPage(browser, browser.current_url)
    check_basket.should_not_be_success_message()