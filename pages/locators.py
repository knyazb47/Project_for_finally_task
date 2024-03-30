from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    NAME_PRODUCT_ON_PAGE = (By.CSS_SELECTOR, ".product_main > h1")
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, '#messages > div > div > strong')
    PRICE_ON_PAGE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    MESSAGE_PRICE_ON_BASKET = (By.CSS_SELECTOR, '#messages > div.alert-info > div.alertinner > p > strong')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')