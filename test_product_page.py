from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import time
import pytest

#LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
LINK="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
"""@pytest.mark.parametrize('LINK', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
"""

@pytest.mark.skip
def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser,LINK)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.check_item_name()
    page.check_item_price()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser,LINK)
    page.open()
    page.go_to_login_page()
    pagelog = LoginPage(browser, browser.current_url)
    pagelog.should_be_login_page()

@pytest.mark.skip
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_cart()
    cartpage = CartPage(browser, browser.current_url)
    cartpage.should_be_cart_have_text()
    cartpage.should_be_cart_is_emtpy()


def test_guest_add_item_to_cart(browser):
    link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-robot-novels_25/"
    page=ProductPage(browser,link)
    page.open()
    page.add_item_to_basket()
    page.go_to_cart()
    cartpage = CartPage(browser,browser.current_url)
    cartpage.should_be_cart_have_text()
    #cartpage.should_be_cart_is_emtpy()