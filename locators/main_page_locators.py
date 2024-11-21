from selenium.webdriver.common.by import By


class MainPageLocators:

    #Список вопросов о важном
    QUESTION_LIST = By.XPATH, "//*[@aria-controls='accordion__panel-{}']"

    #Список ответов на вопросы
    ANSWER = By.XPATH, "//*[@id='accordion__panel-{}']"

    #Последний вопрос в списке (для скролла)
    LAST_QUESTION = By.XPATH, "//*[@aria-controls='accordion__panel-7']"

    #Верхняя кнопка заказать
    ORDER_BUTTON_UPPER = By.XPATH, "//*[@class='Button_Button__ra12g']"

    # Нижняя кнопка заказать
    ORDER_BUTTON_LOWER = By.XPATH, "//*[@class='Button_Button__ra12g Button_Middle__1CSJM']"

    #Лого Самоката
    LOGO_SCOOTER = By.XPATH, "//a[@href='/' and contains(@class, 'Header_LogoScooter')]"

    #Лого Яндекса
    LOGO_YANDEX = By.XPATH, "//a[@href='//yandex.ru' and contains(@class, 'Header_LogoYandex')]"

    #Кнопка убрать куки
    COOCKIE = (By.XPATH, "//button[text()='да все привыкли']")
