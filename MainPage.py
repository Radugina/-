import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Открытие страницы сайта")
    def open(self):
        self.driver.get("https://www.chitai-gorod.ru/")

    @allure.step("Проверка отображения логотипа")
    def logo(self):
        self.wait.until(
            EC.presence_of_element_located(
                By.CLASS_NAME, "header__logo-wrapper"))

    @allure.step("Проверка отображения поиска")
    def search(self):
        self.wait.until(
            EC.presence_of_element_located(
                By.CLASS_NAME, "app-search__form"))

    @allure.step("Проверка верхнего поля хедера")
    def header_top_margin(self):
        self.wait.until(
            EC.presence_of_element_located(
                By.CLASS_NAME, "header-top app-wrapper__header-top"))

    @allure.step("Проверка хедера под «Поиском»")
    def header_bottom_margin(self):
        self.wait.until(
            EC.presence_of_element_located(
                By.CLASS_NAME, "header-bottom app-wrapper__header-bottom"))

    @allure.step("Открытие страницы сайта")
    def reopening(self):
        self.driver.get("https://www.chitai-gorod.ru/")

    @allure.step("Проверка отображения поиска")
    def re_display(self):
        self.wait.until(
            EC.presence_of_element_located(
                By.CLASS_NAME, "app-search__form"))

    @allure.step("Ввод в поле Поиска название и автора книги")
    def input_into_field(self):
        self.wait.until(
            EC.presence_of_element_located(
                By.CLASS_NAME, "app-search__form")).send_keys(
                    "Кадавры Поляринов")

    @allure.step("Нажтие кнопки лупы")
    def result(self):
        self.wait.until(
            EC.element_to_be_clickable((
                By.CLASS_NAME, "search-form__icon-search"))).click()

    @allure.step("Открытие страницы сайта")
    def go_to_website(self):
        self.driver.get("https://www.chitai-gorod.ru/")

    @allure.step("Проверка отображения Акции")
    def displayed(self):
        self.wait.until(
            EC.presence_of_element_located(
                By.CLASS_NAME, "header-bottom__link-item"))

    @allure.step("Нажтие кнопки Акция")
    def promotion(self):
        self.wait.until(
            EC.element_to_be_clickable((
                By.CLASS_NAME, "header-bottom__link-item"))).click()

    @allure.step("Открытие страницы сайта")
    def open_page(self):
        self.driver.get("https://www.chitai-gorod.ru/")

    @allure.step("Новинки литературы")
    def new(self):
        self.wait.until(
            EC.presence_of_element_located(
                By.CLASS_NAME, "shelf-header__header-text shelf-header__header-text--link"))

    @allure.step("Добавление товара в корзину")
    def add_product(self):
        self.driver.find_element(
            By.CLASS_NAME, "chg-app-button__content").click()

    @allure.step("Переход в корзину")
    def add_cart(self):
        self.driver.find_element(
            By.CLASS_NAME, "header-controls__text").click()

    @allure.step("Открытие страницы сайта")
    def open_page_new(self):
        self.driver.get("https://www.chitai-gorod.ru/")

    @allure.step("Отображение локатора Обратная связь")
    def feedback(self):
        self.wait.until(
            EC.presence_of_element_located(
                By.CLASS_NAME, "header-top__feedback-link"))

    @allure.step("Нажать на кнопку Обратная связь")
    def press_the_button(self):
        self.driver.find_element(
            By.CLASS_NAME, "header-top__feedback-link").click()
