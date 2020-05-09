from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class ProductPage(BasePage):
    def selected_offer_should_be_added_to_cart(self):
        add_to_cart_button = self.browser.find_element(By.CLASS_NAME, "btn-outline-success")
        add_to_cart_button.click()
        self.browser.get('https://bamboo.dev.sozvezdie-tour.ru/cart/')
        offer_name = self.browser.find_element (By.XPATH, '//*/h1')
        offer_name = offer_name.get_attribute('text')
        link = self.browser.find_element(By.XPATH, '//table//a')
        link = link.get_attribute('href')
        self.browser.get(link)
        ok = self.browser.find_element(By.XPATH, '//table//a')
        ok = ok.get_attribute('text')
        assert ok, 'Выбранное предложение не добавилось в корзину'
