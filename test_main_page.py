from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


# тест - гость может перейти на страницу с логином
def test_guest_can_go_to_login_page(browser): #гость может перейти на страницу с логином
    page = MainPage(browser,link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()