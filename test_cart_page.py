from .Pages.cart_page import CartPage
from .Pages.product_page import ProductPage
from pytest import mark


@mark.testcase4
@mark.testcase5
def test_can_buy_offer_added_to_cart(browser):
    """
    Проверка возможности купить предложение, добавленное
    в корзину. После покупки пользователь должен быть
    зарегистрирован.
    """
    link = "https://bamboo.dev.sozvezdie-tour.ru/tour/0"
    page = ProductPage(browser, link)
    page.open()
    page.selected_offer_should_be_added_to_cart()
    link = "https://bamboo.dev.sozvezdie-tour.ru/cart/"
    page = CartPage(browser, link)
    page.open()
    page.can_buy_offer_added_to_cart()
    page.should_be_registered_after_payment()