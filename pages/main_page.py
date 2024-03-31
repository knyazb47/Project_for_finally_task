
from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):

    def clik_add_to_basket(self):
        button_basket = self.browser.find_element(*MainPageLocators.BUTTON_BASKET)
        button_basket.click()




