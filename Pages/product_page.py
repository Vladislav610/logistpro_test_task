from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def selected_offer_should_be_added_to_cart(self):
        offer_name_in_page = self.browser.find_element (By.CSS_SELECTOR, ProductPageLocators.OFFER_NAME_ON_PAGE)
        offer_name_in_page = offer_name_in_page.text
        add_to_cart_button = self.browser.find_element(By.CLASS_NAME, ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
        go_to_cart_link = self.browser.find_element(By.XPATH, ProductPageLocators.GO_TO_CART_LINK_BODY)
        go_to_cart_link = go_to_cart_link.get_attribute('href')
        self.browser.get(go_to_cart_link)
        offer_name_in_cart = self.browser.find_element(By.CSS_SELECTOR, ProductPageLocators.OFFER_NAME_IN_CART)
        offer_name_in_cart = offer_name_in_cart.text
        assert offer_name_in_page == offer_name_in_cart,\
            'Выбранное предложение не добавилось в корзину'