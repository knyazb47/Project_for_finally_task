
from .base_page import BasePage
from .locators import MainPageLocators, BasePageLocators

class MainPage(BasePage):

    def clik_add_to_basket(self):
        button_basket = self.browser.find_element(*MainPageLocators.BUTTON_BASKET)
        button_basket.click()

    def click_button_view_basket(self):
        button_view_basket = self.browser.find_element(*MainPageLocators.BUTTON_VIEW_BASET)
        button_view_basket.click()

    def should_see_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'link is visible on the page'




