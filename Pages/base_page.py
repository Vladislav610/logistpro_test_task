from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators, MainPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
#        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def cards_in_catalog_counter(self):
        number_of_cards = len(
            self.browser.find_elements(
                By.XPATH, f"//*[@id='page-content']/div/div/a"))
        return number_of_cards
