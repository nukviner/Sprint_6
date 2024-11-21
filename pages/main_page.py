from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step('Клик на вопрос')
    def click_to_question(self, locator_q_formatted):
        self.scroll_to_element(MainPageLocators.LAST_QUESTION)
        self.click_to_element(locator_q_formatted)

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, number_of_question):
        formatted_question_list = self.format_locators(MainPageLocators.QUESTION_LIST, number_of_question)
        formatted_answer_button = self.format_locators(MainPageLocators.ANSWER, number_of_question)

        self.scroll_to_element(MainPageLocators.LAST_QUESTION)
        self.click_to_question(formatted_question_list)
        return self.get_text_from_element(formatted_answer_button)
