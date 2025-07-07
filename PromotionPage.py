import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PromotionPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Ожидание появление локатора с акциями")
    def stock_locator(self):
        self.wait.until(
            EC.presence_of_element_located(
                By.CLASS_NAME, "constructor-promotions-page__title"))

    @allure.step("Нажатие на конкретную акцию")
    def stock(self):
        self.wait.until(
            EC.element_to_be_clickable((
                By.CLASS_NAME, "block-promotion-card__image ls-is-cached lazyloaded"))).click()

    @allure.step("Сравнение цен")
    def prices(self):
        price1 = driver.find_element(By.CLASS_NAME, "product-price__old")
        price2 = driver.find_element(
            By.CLASS_NAME, "product-price__value product-price__value--discount")
        assert price2 < price1
