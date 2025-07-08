import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PromotionPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Проверка открытия страницы акций")
    def check_promotion_page_is_open(self):
        self.wait.until(
            EC.presence_of_element_located((
                By.XPATH, "//h1[text()='Скидки и акции']")))
