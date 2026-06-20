import allure
import data_test as DT
from pages.main_page import MainPage as MP
from pages.ingredient_popup import IngredientPopup as IP


@allure.feature("Конструктор")
class TestConstructor:

    @allure.title("Переход по клику на «Конструктор»")
    def test_click_constructor(self, driver):
        main = MP(driver)
        main.click_constructor()
        assert main.get_current_url() == DT.MAIN_PAGE_URL

    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_order_feed(self, driver):
        main = MP(driver)
        main.click_order_feed()
        assert main.get_current_url() == DT.FEED_PAGE_URL

    @allure.title("Клик на ингредиент открывает всплывающее окно")
    def test_click_ingredient_opens_popup(self, driver):
        main = MP(driver)
        main.click_first_ingredient()
        popup = IP(driver)
        assert popup.is_popup_displayed()

    @allure.title("Закрытие всплывающего окна по крестику")
    def test_close_popup_by_cross(self, driver):
        main = MP(driver)
        main.click_first_ingredient()
        popup = IP(driver)
        popup.close_popup()
        assert popup.is_popup_not_displayed()

    @allure.title("Счётчик ингредиента увеличивается при добавлении в заказ")
    def test_drag_ingredient_increases_counter(self, driver):
        main = MP(driver)
        initial = main.get_ingredient_counter()
        main.drag_first_ingredient_to_basket()
        updated = main.get_ingredient_counter()
        assert int(updated) > int(initial)