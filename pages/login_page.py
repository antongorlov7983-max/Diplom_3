from pages.base_page import BasePage
from pages.locators import EMAIL_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
import allure


class LoginPage(BasePage):

    @allure.step("Ввести email")
    def set_email(self, email):
        self.wait_visible(EMAIL_FIELD).send_keys(email)

    @allure.step("Ввести пароль")
    def set_password(self, password):
        self.wait_visible(PASSWORD_FIELD).send_keys(password)

    @allure.step("Нажать кнопку «Войти»")
    def click_login_button(self):
        self.click_with_js(LOGIN_BUTTON)

    @allure.step("Заполнить форму и войти")
    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()