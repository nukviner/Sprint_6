import pytest
from selenium import webdriver
from data import TestData


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(TestData.BASE_URL)
    yield driver
    driver.quit()