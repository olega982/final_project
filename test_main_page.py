import pytest

from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.shoud_be_login_page()



def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_busket()
    page.basket_is_empty()
    page.basket_empty_basket_text()
