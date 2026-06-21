from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import POPUP, CLOSE_BUTTON, ORDER_NUMBER
import allure


class IngredientPopup(BasePage):

    @allure.step("Проверить, что попап отображается")
    def is_popup_displayed(self):
        return self.wait_visible(POPUP).is_displayed()

    @allure.step("Проверить, что попап не отображается")
    def is_popup_not_displayed(self):
        return self.wait.until(EC.invisibility_of_element_located(POPUP))

    @allure.step("Закрыть попап по крестику")
    def close_popup(self):
        self.wait_clickable(CLOSE_BUTTON).click()
        self.remove_overlays()

    @allure.step("Получить номер созданного заказа")
    def get_order_number(self):
        order_element = self.wait_visible(ORDER_NUMBER)
        self.wait.until(lambda d: order_element.text != "9999")
        return order_element.text