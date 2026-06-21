from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Ожидание видимости элемента")
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента")
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Клик через JavaScript")
    def click_with_js(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Перетащить элемент через JavaScript")
    def drag_and_drop_js(self, source_locator, target_locator):
        source = self.wait_visible(source_locator)
        target = self.wait_visible(target_locator)
        script = """
            function createEvent(type) {
                return new DragEvent(type, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: new DataTransfer()
                });
            }
            arguments[0].dispatchEvent(createEvent('dragstart'));
            arguments[1].dispatchEvent(createEvent('drop'));
            arguments[0].dispatchEvent(createEvent('dragend'));
        """
        self.driver.execute_script(script, source, target)

    @allure.step("Принудительно удалить все оверлеи через JS")
    def remove_overlays(self):
        self.driver.execute_script("""
            document.querySelectorAll('[class*="Modal_modal_overlay"]').forEach(el => el.remove());
        """)

    @allure.step("Открыть страницу")
    def open_page(self, url):
        self.driver.get(url)