from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Страница "Для кого самокат"
    NAME_FIELD = By.XPATH, "//input[@placeholder='* Имя']"
    LASTNAME_FIELD = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS_FIELD = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_FIELD = By.XPATH, "//input[@placeholder='* Станция метро']"
    METRO_SELECTOR = By.XPATH, "//button[@value='1']"
    PHONE_FIELD = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = By.XPATH, "//button[text()='Далее']"

    # Страница "Про аренду"
    DATE_FIELD = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    DATE_SELECTOR = By.XPATH, "//*[@class='react-datepicker-popper']"
    DAY_SELECT = By.XPATH, "//div[text()='28']"
    RENT_PERIOD_FIELD = By.XPATH, ".//div[text()='* Срок аренды']"
    RENT_DAY = By.XPATH, "//div[@class = 'Dropdown-menu']/div[text() ='сутки']"
    CHECKBOX = By.XPATH, "//input[@id='grey']"
    COMMENT_FIELD = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']"

    # Подтверждение заказа
    CONFIRM_BUTTON = By.XPATH, "//button[text()='Да']"
    BUTTON_STATUS_ORDER = By.XPATH, ".//button[text()='Посмотреть статус']"

