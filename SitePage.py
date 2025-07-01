import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class SitePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Открытие страницы сайта")
    def open(self):
        self.driver.get("https://www.chitai-gorod.ru/?srsltid=AfmBOoprR19pGoqU9cfx5bhbOp5tTgikGPJBRfQlGeu_M1X0bT7w1E5k")

    @allure.step("Элемент эмблемы Читай-город присутствует на странице")
    def element(self):
        element = self.driver.find_element(
            By.CLASS_NAME, "header__logo-wrapper")
        assert element.is_displayed()

    @allure.step("Текст элемента соответствует ожидаемому значению")
    def element_text(self):
        element = self.driver.find_element(
            By.CLASS_NAME, "search-form__input-wrapper")
        assert element.text == "Что будем искать?"

    @allure.step("Элемент находится в нужном состоянии")
    def element_enabled(self):
        element = self.driver.find_element(
            By.CLASS_NAME, "header-controls__icon")
        assert element.is_enabled()

    @allure.step("Элемент Акции можно нажать")
    def click_element(self):
        element = self.driver.find_element(
            By.CLASS_NAME, "header-bottom-item")
        element.click()

    @allure.step("Пользователь может перемещаться по страницам приложения")
    def navigation(self):
        self.driver.get(
            "https://www.chitai-gorod.ru/?srsltid=AfmBOooyTgGQijnRDEEumkuRbhn74zHsHALIZcriOA80oNT34Z_N0Z4a")
        search_box = self.driver.find_element(
            By.CLASS_NAME, "search-form__input search-form__input--search")
        search_box.send_keys("Война и мир")
        search_box.send_keys(Keys.RETURN)
        self.driver.find_element(
            By.CLASS_NAME, "chg-app-pagination__item").click()
        assert self.driver.current_url == "https://www.chitai-gorod.ru/search?phrase=%D0%B2%D0%BE%D0%B9%D0%BD%D0%B0+%D0%B8+%D0%BC%D0%B8%D1%80&page=2"
