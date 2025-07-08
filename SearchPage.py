import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Проверка отображения результатов по запросу")
    def display_result(self, search_letters):
        search_letters.lower()
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//h1[contains(text(), 'Показываем результаты по запросу «{search_letters}»')]")))
