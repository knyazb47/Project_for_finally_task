from .base_page import BasePage
from .locators import BaskePageLocators

class BasketPage(BasePage):
    def item_is_not_basket(self):
        assert self.is_not_element_present(*BaskePageLocators.ITEM_IN_BASKET), "The basket is not empty"

    def message_basket_empty(self):
        message_basket_empty = self.browser.find_element(*BaskePageLocators.MESSAGE_BASKET_EMPTY).text
        print(message_basket_empty)
        assert 'Your basket is empty.' in message_basket_empty, 'The message is not on the page'
