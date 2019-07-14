from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import pytest

LINK = "http://selenium1py.pythonanywhere.com/"
LINK2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"


# тест - гость может перейти на страницу с логином
class TestLoginFromMainPage(object):
    def test_guest_can_go_to_login_page(self,browser):
        page = MainPage(browser,LINK)
        page.open()
        page.go_to_login_page()
        pagelog= LoginPage(browser, browser.current_url)
        pagelog.should_be_login_page()
        page.should_be_login_link()


    def test_guest_cant_see_product_in_cart_opened_from_main_page(self,browser):
        page = MainPage(browser,LINK)
        page.open()
        page.go_to_cart()
        cartpage=CartPage(browser, browser.current_url)
        cartpage.should_be_cart_is_emtpy()
        cartpage.should_be_cart_have_text()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.go_to_login_page()
        pagelog = LoginPage(browser, browser.current_url)
        pagelog.should_be_login_link()





