from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_item_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADDTOBASKET).click()

    def check_item_name(self):
        name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        name_cart = self.browser.find_element(*ProductPageLocators.ITEM_NAME_CART).text
        assert name == name_cart, "Name item another = {}, need={}".format(name_cart, name)

    def check_item_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_ITEM).text
        price_cart = self.browser.find_element(*ProductPageLocators.PRICE_ITEM_CART).text
        assert price == price_cart, "price another ={}".format(price_cart)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGESUCCESS), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_d(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGESUCCESS), \
            "Success message is presented, but should not be"



