from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def item_name_in_basket_correct(self):
        item_name_on_product_page = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        item_name_in_busket = self.browser.find_element(*ProductPageLocators.ITEM_NAME_ACC_PAGE).text
        assert item_name_on_product_page == item_name_in_busket, f"You have an error on {self.browser.current_url}"

    def item_prize_in_basket_correct(self):
        item_prize_on_product_page = self.browser.find_element(*ProductPageLocators.ITEM_PRIZE).text
        item_prize_in_busket = self.browser.find_element(*ProductPageLocators.ITEM_PRIZE_ACC_PAGE).text
        assert item_prize_in_busket == item_prize_on_product_page, f"Prizes in basket and on product page are not the same"

    def click_add_to_basket_button(self):
        find_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BUTTON)
        find_button.click()
