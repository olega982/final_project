import pytest

from .pages.product_page import ProductPage


# задание на параметризацию
@pytest.mark.parametrize('promo_number',
                         ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_number}"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    # page.item_prize_in_basket_correct()
    page.item_name_in_basket_correct()
