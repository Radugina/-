import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields = {
            "title": "Кадавры (Алексей Поляринов)"
        }

    @allure.step("Результаты по запросу")
    def display_result(self):
        self.wait.until(
            EC.presence_of_element_located(
                By.CLASS_NAME, "search-title"))

    @allure.step("Первая книга содержит параметры по запросу")
    def fill_form(self):
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)
