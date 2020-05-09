from .Pages.product_page import ProductPage
from pytest import mark

@mark.smoke
@mark.testcase3
def test_can_add_to_cart(browser):
    """
    Проверка корректности добавления
    в корзину предложения с его страницы
    """
    link = "https://bamboo.dev.sozvezdie-tour.ru/tour/0"
    page = ProductPage(browser, link)
    page.open()
    page.selected_offer_should_be_added_to_cart()