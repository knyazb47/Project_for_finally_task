from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url_current = self.browser.current_url
        assert 'login' in url_current, 'incorrect URL'

    def should_be_login_form(self):

        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM) , 'login_form not found'

    def should_be_register_form(self):

        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'register_form not found'

    def register_new_user(self, email, password):
        fild_register_email = self.browser.find_element(*LoginPageLocators.FILD_REGISTER_EMAIL)
        fild_register_email.send_keys(email)
        fild_register_pasword = self.browser.find_element(*LoginPageLocators.FILD_REGISTER_PASSWORD)
        fild_register_pasword.send_keys(password)
        fild_register_pasword_confirm = self.browser.find_element(*LoginPageLocators.FILD_REGISTER_PASSWORD_CONFIRM)
        fild_register_pasword_confirm.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button_register.click()


