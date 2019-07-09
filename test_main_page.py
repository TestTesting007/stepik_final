from .pages.main_page import MainPage
from .pages.login_page import LoginPage

LINK = "http://selenium1py.pythonanywhere.com/"
LINK2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"


# тест - гость может перейти на страницу с логином
def test_guest_can_go_to_login_page(browser): #гость может перейти на страницу с логином
    page = MainPage(browser,LINK)
    page.open()
    page.go_to_login_page()
    pagelog= LoginPage(browser, browser.current_url)
    pagelog.should_be_login_page()
    page.should_be_login_link()