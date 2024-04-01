from selenium.webdriver.common.by import By

class MainPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BUTTON_VIEW_BASET = (By.CSS_SELECTOR, ".btn-group > a.btn-default")
    NAME_PRODUCT_ON_PAGE = (By.CSS_SELECTOR, ".product_main > h1")
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, '#messages > div > div > strong')
    PRICE_ON_PAGE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    MESSAGE_PRICE_ON_BASKET = (By.CSS_SELECTOR, '#messages > div.alert-info > div.alertinner > p > strong')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')
    FILD_REGISTER_EMAIL = (By.ID, 'id_registration-email')
    FILD_REGISTER_PASSWORD = (By.ID, 'id_registration-password1')
    FILD_REGISTER_PASSWORD_CONFIRM = (By.ID, 'id_registration-password2')
    BUTTON_REGISTER = (By.NAME, 'registration_submit')

class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BaskePageLocators():
    ITEM_IN_BASKET = (By.CSS_SELECTOR, ".basket-items > div.row > div.col-sm-4 > h3 > a")
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")