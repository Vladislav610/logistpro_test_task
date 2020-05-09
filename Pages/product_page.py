from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def selected_offer_should_be_added_to_cart(self):
        offer_name_in_page = self.browser.find_element (By.CSS_SELECTOR, 'div.col>h1')
        offer_name_in_page = offer_name_in_page.text
        add_to_cart_button = self.browser.find_element(By.CLASS_NAME, "btn-outline-success")
        add_to_cart_button.click()
        go_to_cart_link = self.browser.find_element(By.XPATH, '//tbody/tr[1]/td[4]/a')
        go_to_cart_link = go_to_cart_link.get_attribute('href')
        self.browser.get(go_to_cart_link)
        offer_name_in_cart = self.browser.find_element(By.CSS_SELECTOR, 'td:nth-child(1)>a')
        offer_name_in_cart = offer_name_in_cart.text
        assert offer_name_in_page == offer_name_in_cart,\
            'Выбранное предложение не добавилось в корзину'