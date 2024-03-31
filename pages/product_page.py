from .base_page import BasePage
from .locators import MainPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_message_add_to_basket()
        self.should_be_price_add_to_basket()

    def should_be_message_add_to_basket(self):
        name_product_on_page = self.browser.find_element(*MainPageLocators.NAME_PRODUCT_ON_PAGE).text
        message_add_to_basket = self.browser.find_element(*MainPageLocators.MESSAGE_ADD_TO_BASKET).text
        assert message_add_to_basket == name_product_on_page, 'name product not match'

    def should_be_price_add_to_basket(self):
        price_on_page = self.browser.find_element(*MainPageLocators.PRICE_ON_PAGE).text
        message_price_on_basket = self.browser.find_element(*MainPageLocators.MESSAGE_PRICE_ON_BASKET).text
        assert price_on_page == message_price_on_basket, ' prices not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*MainPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_success_message_disappeared(self):
        assert self.is_disappeared(*MainPageLocators.MESSAGE_ADD_TO_BASKET)
