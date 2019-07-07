from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


import pytest

def pytest_addoption(parser):
    parser.addoption('--browser_name',action='store',default ="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language',action='store',default='ru', help="Choose languages for browser")

# Выбор языка реализовано только для  только Chrome
@pytest.fixture(scope ="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    u_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': u_language})
    if browser_name == "chrome":
        browser=webdriver.Chrome(options=options)
        browser.implicitly_wait(4)
        print("Start browser Chrome")
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
        print("start browser firefox")
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield  browser
    print("close browser")
    browser.quit()