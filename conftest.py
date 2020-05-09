import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()