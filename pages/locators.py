from selenium.webdriver.common.by import By

# MainPage
CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']/parent::a")
ORDER_FEED_TAB = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
FIRST_INGREDIENT = (By.XPATH, "(//a[contains(@class,'BurgerIngredient_ingredient__')])[1]")
BASKET = (By.XPATH, "//ul[contains(@class,'BurgerConstructor_basket__list')]")
ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
INGREDIENT_COUNTER = (By.XPATH, "(//a[contains(@class,'BurgerIngredient_ingredient__')])[1]//p[contains(@class,'counter_counter__num')]")

# LoginPage
EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

# FeedPage
TOTAL_ORDERS = (By.XPATH, "//p[contains(text(),'Выполнено за все время')]/following-sibling::p[contains(@class,'OrderFeed_number')]")
TODAY_ORDERS = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p[contains(@class,'OrderFeed_number')]")
ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady')]//li[contains(@class,'text_type_digits-default')]")

# IngredientPopup
POPUP = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]")
CLOSE_BUTTON = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//button")
ORDER_NUMBER = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//h2")