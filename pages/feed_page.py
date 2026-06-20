from pages.base_page import BasePage
from pages.locators import TOTAL_ORDERS, TODAY_ORDERS, ORDER_IN_PROGRESS
import allure


class FeedPage(BasePage):

    @allure.step("Получить счётчик «Выполнено за всё время»")
    def get_total_orders(self):
        return self.wait_visible(TOTAL_ORDERS).text

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def get_today_orders(self):
        return self.wait_visible(TODAY_ORDERS).text

    @allure.step("Получить номер заказа в разделе «В работе»")
    def get_order_in_progress(self):
        return self.wait_visible(ORDER_IN_PROGRESS).text