import allure
from pages.main_page import MainPage as MP
from pages.feed_page import FeedPage as FP
from pages.ingredient_popup import IngredientPopup as IP


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("При создании заказа счётчик «Выполнено за всё время» увеличивается")
    def test_new_order_increases_total_counter(self, login_user):
        driver = login_user
        main = MP(driver)
        feed = FP(driver)

        main.go_to_order_feed()
        initial = feed.get_total_orders()

        main.go_to_constructor()
        main.create_order()
        IP(driver).close_popup()

        main.go_to_order_feed()
        assert int(feed.get_total_orders()) > int(initial)

    @allure.title("При создании заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_new_order_increases_today_counter(self, login_user):
        driver = login_user
        main = MP(driver)
        feed = FP(driver)

        main.go_to_order_feed()
        initial = feed.get_today_orders()

        main.go_to_constructor()
        main.create_order()
        IP(driver).close_popup()

        main.go_to_order_feed()
        assert int(feed.get_today_orders()) > int(initial)

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_new_order_appears_in_progress(self, login_user):
        driver = login_user
        main = MP(driver)
        feed = FP(driver)

        main.go_to_constructor()
        main.create_order()

        popup = IP(driver)
        popup.get_order_number()
        popup.close_popup()

        main.go_to_order_feed()
        order_number_in_feed = feed.get_order_in_progress()
        assert order_number_in_feed is not None
        assert order_number_in_feed != ""