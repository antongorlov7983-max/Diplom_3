import pytest
import requests
import pages.locators as loc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.main_page import MainPage
from pages.login_page import LoginPage
import data_test as DT

""""вставленный"""
def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browsers in headless mode"
    )

@pytest.fixture(scope="session")
def headless_mode(request):
    """Возвращает True, если передан флаг --headless"""
    return request.config.getoption("--headless")
""""вставленный"""

def get_chrome_driver(headless=False):
    options = ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    if headless:
        options.add_argument("--headless=new")   # новый движок
        # Опции для CI (можно закомментировать для локальных прогонов)
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=ChromeService(), options=options)


def get_firefox_driver(headless=False):
    options = FirefoxOptions()
    options.add_argument("--window-size=1920,1080")
    if headless:
        options.add_argument("--headless")  # для Firefox используется просто --headless
    return webdriver.Firefox(service=FirefoxService(), options=options)


def create_user_via_api():
    payload = {
        "email": DT.TEST_EMAIL,
        "password": DT.TEST_PASSWORD,
        "name": "TestUser"
    }
    response = requests.post(DT.REGISTER_URL, json=payload)
    if response.status_code == 200:
        return response.json().get("accessToken")
    return None


def delete_user_via_api(token):
    requests.delete(DT.DELETE_USER_URL, headers={"Authorization": token})


@pytest.fixture(scope="session")
def register_user():
    token = create_user_via_api()
    yield
    if token:
        delete_user_via_api(token)


@pytest.fixture(params=["chrome", "firefox"])
def driver(request, register_user, headless_mode):
    if request.param == "chrome":
        drv = get_chrome_driver(headless=headless_mode)
    else:
        drv = get_firefox_driver(headless=headless_mode)
    drv.get(DT.MAIN_PAGE_URL)
    yield drv
    drv.quit()


@pytest.fixture
def login_user(driver):
    main_page = MainPage(driver)
    main_page.go_to_login()
    login_page = LoginPage(driver)
    login_page.login(DT.TEST_EMAIL, DT.TEST_PASSWORD)
    main_page.wait_clickable(loc.ORDER_BUTTON)
    main_page.remove_overlays()
    return driver