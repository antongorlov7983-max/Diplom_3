import random
import string


def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


TEST_EMAIL = f"test_{generate_random_string()}@ya.com"
TEST_PASSWORD = "UniqueBurger2024!"

BASE_URL = "https://stellarburgers.education-services.ru"
MAIN_PAGE_URL = f"{BASE_URL}/"
LOGIN_PAGE_URL = f"{BASE_URL}/login"
FEED_PAGE_URL = f"{BASE_URL}/feed"
REGISTER_URL = f"{BASE_URL}/api/auth/register"
DELETE_USER_URL = f"{BASE_URL}/api/auth/user"