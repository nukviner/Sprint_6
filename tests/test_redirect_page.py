from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import TestData
import time
import allure


@allure.title('Тесты на проверку переходов между страницами по кликам на лого')
class TestLogoRedirect:

    @allure.description('Проверяем переход на главную страницу по клику на лого Самоката')
    def test_logo_redirect_to_main_page(self, driver):
        base_page = BasePage(driver)
        base_page.coockie_clicker(MainPageLocators.COOCKIE)
        base_page.click_to_element(MainPageLocators.ORDER_BUTTON_UPPER)
        base_page.click_to_element(MainPageLocators.LOGO_SCOOTER)
        assert base_page.get_current_url() == TestData.BASE_URL

    @allure.description('Проверяем переход на страницу Дзена по клику на лого Яндекса')
    def test_logo_redirect_to_dzen(self, driver):
        base_page = BasePage(driver)
        base_page.coockie_clicker(MainPageLocators.COOCKIE)
        base_page.click_to_element(MainPageLocators.LOGO_YANDEX)
        time.sleep(3)
        base_page.switch_to_next_tab()
        time.sleep(3)
        assert 'dzen' in base_page.get_current_url()
