from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):

    @allure.step('Выбор станции метро')
    def select_station(self):
        self.click_to_element(OrderPageLocators.METRO_FIELD)
        self.click_to_element(OrderPageLocators.METRO_SELECTOR)

    @allure.step('Выбор даты в календаре')
    def select_date_in_calendar(self):
        self.click_to_element(OrderPageLocators.DATE_FIELD)
        self.click_to_element(OrderPageLocators.DAY_SELECT)

    @allure.step('Проверка статуса заказа')
    def check_status_order_displayed(self):
        return self.check_displaying_of_element(OrderPageLocators.BUTTON_STATUS_ORDER)

    @allure.step('Заполнение первой формы')
    def data_entry_first_form(self, test_data):
        self.click_to_element(OrderPageLocators.NAME_FIELD)
        self.send_keys_to_input(OrderPageLocators.NAME_FIELD, test_data[0])
        self.click_to_element(OrderPageLocators.LASTNAME_FIELD)
        self.send_keys_to_input(OrderPageLocators.LASTNAME_FIELD, test_data[1])
        self.click_to_element(OrderPageLocators.ADDRESS_FIELD)
        self.send_keys_to_input(OrderPageLocators.ADDRESS_FIELD, test_data[2])
        self.select_station()
        self.click_to_element(OrderPageLocators.PHONE_FIELD)
        self.send_keys_to_input(OrderPageLocators.PHONE_FIELD, test_data[3])
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнение второй формы')
    def data_entry_second_form(self, test_data):
        self.select_date_in_calendar()
        self.click_to_element(OrderPageLocators.RENT_PERIOD_FIELD)
        self.click_to_element(OrderPageLocators.RENT_DAY)
        self.click_to_element(OrderPageLocators.CHECKBOX)
        self.click_to_element(OrderPageLocators.COMMENT_FIELD)
        self.send_keys_to_input(OrderPageLocators.COMMENT_FIELD, test_data[-1])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.CONFIRM_BUTTON)
