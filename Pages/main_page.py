from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests


class MainPage(BasePage):
    def should_be_all_images_on_page(self):
        counter = 0
        number_of_cards = self.cards_in_catalog_counter()
        for id in range(1, number_of_cards+1):
            ok = False
            ok = BasePage.is_element_present(
                self, By.XPATH, f"//div/div/a[{id}]/img[starts-with(@src, 'http')]")
            if ok:
                counter += 1
        assert counter == number_of_cards, \
            f"Отсутствует изображение на карточке(ах) в каталоге ({number_of_cards - counter} шт.)"


    def should_not_be_404_images_on_page(self):
        counter = 0
        number_of_cards = self.cards_in_catalog_counter()
        for id in range(1, number_of_cards+1):
            try:
                img = self.browser.find_element(
                    By.XPATH, f"//div/div/a[{id}]/img[starts-with(@src, 'http')]")
                img_src = img.get_attribute('src')
                response = requests.get(img_src)
                if response.status_code == 200:
                    counter += 1
            except (NoSuchElementException):
                continue
        assert counter == number_of_cards, \
            f'Битая ссылка на изображение на карточке(ах) в каталоге ({number_of_cards - counter} шт.)'


    def should_be_200_code_on_all_cards_links(self):
        counter = 0
        number_of_cards = self.cards_in_catalog_counter()
        for id in range(1, number_of_cards+1):
            try:
                detail_link = self.browser.find_element(
                    By.XPATH, f"//*[@id='page-content']/div/div/a[{id}][starts-with(@href, '/tour/')]")
                detail_link = detail_link.get_attribute('href')
                response = requests.get(detail_link)
                if response.status_code == 200:
                    counter += 1
            except (NoSuchElementException):
                continue
        assert counter == number_of_cards, \
            f'Битая ссылка на страницу предложения из каталога ({number_of_cards - counter} шт.)'
