from .base_page import BasePage
from .locators import CartPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "Items are presented, but should not be"