from pages.base_page import BasePage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from data import TestData
import pytest
import allure


@allure.title('Тесты на проверку создания заказов')
class TestOrderPageOrder:

    @pytest.mark.parametrize('button, auth', [(MainPageLocators.ORDER_BUTTON_UPPER, TestData.order_1),
                                                   (MainPageLocators.ORDER_BUTTON_LOWER, TestData.order_2)])
    @allure.description('Делаем заказ самоката с разными данными из разных точек входа')
    def test_order_all_fields_success(self, driver, button, auth):
        order_page = OrderPage(driver)
        base_page = BasePage(driver)
        base_page.coockie_clicker(MainPageLocators.COOCKIE)
        base_page.scroll_to_element(button)
        base_page.click_to_element(button)
        order_page.data_entry_first_form(auth)
        order_page.data_entry_second_form(auth)
        assert order_page.check_status_order_displayed()
