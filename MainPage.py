import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Открытие страницы сайта")
    def open_main_page(self):
        self.driver.get("https://www.chitai-gorod.ru/")

    @allure.step("Закрытие всплывающего окна с выбором города")
    def close_city_window(self):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, '//div[text()="Да, я здесь "]/..'))).click()

    @allure.step("Проверка отображения логотипа")
    def wait_logo_is_present(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "header__logo-wrapper")))

    @allure.step("Проверка отображения поиска")
    def wait_search_field_is_present(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "app-search__form")))

    @allure.step("Проверка отображения верхнего поля хедера")
    def wait_header_top_margin_is_present(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "header-top__container")))

    @allure.step("Проверка отображения хедера под «Поиском»")
    def wait_header_bottom_margin_is_present(self):
        self.wait.until(
            EC.visibility_of_element_located(
                ((By.XPATH, "//div[@Class='header-bottom__container']"))))

    @allure.step("Проверка ввода в поле Поиска название и автора книги")
    def input_into_field(self, search_letters: str):
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//form[contains(@class, 'search-form')]"))).click()
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//form[contains(@class, 'search-form--opened')]"))).click()
        search_field = self.driver.find_element(By.XPATH, "//input[@class='search-form__input search-form__input--search']")
        search_field.send_keys(search_letters)

    @allure.step("Отображение результата поиска")
    def display_result(self, search_letters):
        search_letters.lower()
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//h1[contains(text(), 'Показываем результаты по запросу «{search_letters}»')]")))

    @allure.step("Проверка нажатия кнопки Лупа")
    def click_on_search_button(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "search-form__icon-search"))).click()

    @allure.step("Проверка отображения Акции")
    def wait_promotion_is_present(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "header-bottom__link-item"))).click()

    @allure.step("Переход в корзину")
    def go_to_cart_page(self):
        self.driver.find_element(
           By.XPATH, "//span[text()=' Корзина ']").click()

    @allure.step("Отображение локатора Обратная связь")
    def wait_feedback_button_is_present(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[text()='Обратная связь ']"))).click()
