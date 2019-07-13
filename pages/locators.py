from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

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
    MESSAGESUCCESS = (By.CSS_SELECTOR, "#messages .alert-success:first-child")

class CartPageLocators(object):
    GOTOCART=(By.CSS_SELECTOR,".btn-group>a.btn.btn-default")
    CARTISEMPTY = (By.CSS_SELECTOR,"#content_inner >p")
    LISTITEMS=(By.CSS_SELECTOR,".basket-items")