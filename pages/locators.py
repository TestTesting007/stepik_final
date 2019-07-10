from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR,"#login_link")

class LoginPageLocators(object):
    LOGINFORM = (By.CSS_SELECTOR,"#login_form")
    REGISTRFORM = (By.CSS_SELECTOR,"#register_form")

class ProductPageLocators(object):
    ADDTOBASKET = (By.CSS_SELECTOR,".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    ITEM_NAME_CART = (By.CSS_SELECTOR, ".alertinner>strong")
    PRICE_ITEM = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRICE_ITEM_CART = (By.CSS_SELECTOR, ".alertinner>p>strong")