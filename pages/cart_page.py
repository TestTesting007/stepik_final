from .base_page import BasePage
from .locators import CartPageLocators
from selenium.common.exceptions import NoSuchElementException

class CartPage(BasePage):

    def should_be_cart_have_text(self):
        assert self.is_element_present(*CartPageLocators.CARTISEMPTY),"Not found element"
        text = self.browser.find_element(*CartPageLocators.CARTISEMPTY).text
        assert "Your basket is empty. Continue shopping" == text,"Cart is not empty, two assert"

    def should_be_cart_is_emtpy(self):
       assert self.is_not_element_present(*CartPageLocators.LISTITEMS), "Cart is not empty"
