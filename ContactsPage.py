import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Проверка отображения кнопки «Отправить обращение»")
    def wait_send_request_button_is_present(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "chg-app-button__content")))
