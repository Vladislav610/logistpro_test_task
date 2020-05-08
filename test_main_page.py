from .Pages.main_page import MainPage
from pytest import mark


@mark.testcase1
def test_all_cards_have_images(browser):
    """У каждой карточки должно быть изображение."""
    link = "https://bamboo.dev.sozvezdie-tour.ru/cat/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_all_images_on_page()

@mark.testcase1
def test_all_images_code_200(browser):
    """" Все изображения должны загружаться с кодом 200."""
    link = "https://bamboo.dev.sozvezdie-tour.ru/cat/"
    page = MainPage(browser, link)
    page.open()
    page.should_not_be_404_images_on_page()