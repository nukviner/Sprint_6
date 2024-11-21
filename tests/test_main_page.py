import pytest
from data import TestData
from pages.main_page import MainPage
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

@allure.title('Тесты на проверку вопросов о важном')
class TestMainPage:

    @pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, 7])
    @allure.description('Проверяем набор ответов на список вопросов о важном')
    def test_answers_from_questions_is_answers_from_answers_text(self, driver, num):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.coockie_clicker(MainPageLocators.COOCKIE)
        assert main_page.get_answer_text(num) == TestData.ANSWERS_TEXT[num]
