from .Pages.product_page import ProductPage
from .Pages.basket_page import BasketPage
import pytest
import time


class TestguestAddToBasketFromProductPage:
    def test_guest_cant_see_success_message(self, browser, link):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_not_be_success_message()