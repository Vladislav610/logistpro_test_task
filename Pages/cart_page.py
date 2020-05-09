from .base_page import BasePage
from .locators import CartPageLocators
from selenium.webdriver.common.by import By
from time import time


class CartPage(BasePage):
    def can_buy_offer_added_to_cart(self):
        name = str(time())
        email = name + '@' + name + '.test'
        temp = self.browser.find_element(By.ID, "name")
        temp.send_keys(name)
        temp = self.browser.find_element(By.ID, "email")
        temp.send_keys(email)
        temp = self.browser.find_element(By.ID, "password")
        temp.send_keys('VLADISLAV')
        temp = self.browser.find_element(By.ID, "cardNumber")
        temp.send_keys('0000000000000000')
        temp = self.browser.find_element(By.ID, "cardName")
        temp.send_keys('VLADISLAV')
        temp = self.browser.find_element(By.ID, "cardExpiry")
        temp.send_keys('12/99')
        temp = self.browser.find_element(By.ID, "cardCvc")
        temp.send_keys('777')
        self.browser.find_element(By.CSS_SELECTOR, "div.mt-4.text-center > button").click()
        table_of_orders = BasePage.is_element_present(self, By.XPATH, "//table/thead")
        assert table_of_orders, "Что-то пошло не так. Покупка не произошла."
