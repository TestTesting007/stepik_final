from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegistrationUsers


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        link=self.browser.current_url
        assert "login" in link, "The link does not contain the word login"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGINFORM), "Login from is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRFORM), "Registr form is not present"

    def register_new_user(self, email, password):
        self.browser.find_element(*RegistrationUsers.EMAIL).send_keys(email)
        self.browser.find_element(*RegistrationUsers.PASSWORD1).send_keys(password)
        self.browser.find_element(*RegistrationUsers.PASSWORD2).send_keys(password)
        self.browser.find_element(*RegistrationUsers.BUTTON).click()
