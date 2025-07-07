import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("проверка отображения выбранного товара в корзине")
    def cart(self):
        self.wait.until(
            EC.presence_of_element_located(
                By.CLASS_NAME, "cart-page__title"))
