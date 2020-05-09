class BasePageLocators:
    OFFER_CARD = "//*[@id='page-content']/div/div/a"


class MainPageLocators:
    pass


class ProductPageLocators:
    OFFER_NAME_ON_PAGE = 'div.col>h1'
    ADD_TO_CART_BUTTON = "btn-outline-success"
    GO_TO_CART_LINK_BODY = '//tbody/tr[1]/td[4]/a'
    OFFER_NAME_IN_CART = 'td:nth-child(1)>a'

class CartPageLocators:
    PAY_BUTTON = "div.mt-4.text-center > button"
    USER_NAME_TOP = "//nav/div[2]/div[1]/a"