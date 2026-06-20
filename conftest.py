import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.main_page import MainPage
from pages.login_page import LoginPage
import data_test as DT


def get_chrome_driver():
    options = ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(service=ChromeService(), options=options)


def get_firefox_driver():
    options = FirefoxOptions()
    options.add_argument("--window-size=1920,1080")
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
def driver(request, register_user):
    if request.param == "chrome":
        drv = get_chrome_driver()
    else:
        drv = get_firefox_driver()
    drv.get(DT.MAIN_PAGE_URL)
    yield drv
    drv.quit()


@pytest.fixture
def login_user(driver):
    main_page = MainPage(driver)
    main_page.go_to_login()
    login_page = LoginPage(driver)
    login_page.login(DT.TEST_EMAIL, DT.TEST_PASSWORD)
    main_page.wait_clickable(main_page.ORDER_BUTTON)
    main_page.remove_overlays()
    return driver