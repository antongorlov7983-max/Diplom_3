from pages.base_page import BasePage
from pages.locators import CONSTRUCTOR_TAB, ORDER_FEED_TAB, FIRST_INGREDIENT, BASKET, ORDER_BUTTON, INGREDIENT_COUNTER
import allure
import data_test as DT


class MainPage(BasePage):

    @allure.step("Кликнуть на «Конструктор»")
    def click_constructor(self):
        self.click_with_js(CONSTRUCTOR_TAB)

    @allure.step("Кликнуть на «Лента заказов»")
    def click_order_feed(self):
        self.click_with_js(ORDER_FEED_TAB)

    @allure.step("Перейти в конструктор и очистить оверлеи")
    def go_to_constructor(self):
        self.click_constructor()
        self.remove_overlays()

    @allure.step("Перейти в ленту заказов и очистить оверлеи")
    def go_to_order_feed(self):
        self.click_order_feed()
        self.remove_overlays()

    @allure.step("Кликнуть на первый ингредиент")
    def click_first_ingredient(self):
        self.wait_clickable(FIRST_INGREDIENT).click()

    @allure.step("Перетащить первый ингредиент в корзину")
    def drag_first_ingredient_to_basket(self):
        source = self.wait_clickable(FIRST_INGREDIENT)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", source)
        self.drag_and_drop_js(FIRST_INGREDIENT, BASKET)

    @allure.step("Нажать «Оформить заказ»")
    def click_create_order(self):
        self.wait_clickable(ORDER_BUTTON).click()

    @allure.step("Получить счётчик ингредиента")
    def get_ingredient_counter(self):
        return self.wait_visible(INGREDIENT_COUNTER).text

    @allure.step("Создать заказ: перетащить ингредиент и нажать «Оформить заказ»")
    def create_order(self):
        self.drag_first_ingredient_to_basket()
        self.click_create_order()

    @allure.step("Перейти на страницу логина через конструктор")
    def go_to_login(self):
        self.click_constructor()
        self.open_page(DT.LOGIN_PAGE_URL)