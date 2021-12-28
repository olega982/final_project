from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators():
    ADD_TO_BUSKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    ITEM_PRIZE = (By.CSS_SELECTOR, ".product_main> .price_color")
    ITEM_NAME_ACC_PAGE = (By.CSS_SELECTOR, "#messages >div:nth-child(1)>.alertinner>strong")
    ITEM_PRIZE_ACC_PAGE = (By.CSS_SELECTOR, "#messages >div:nth-child(3)>.alertinner>p>strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
