import allure
import pytest
from selenium import webdriver
from pages.MainPage import MainPage
from pages.SearchPage import SearchPage
from pages.PromotionPage import PromotionPage
from pages.CartPage import CartPage
from pages.ContactsPage import ContactsPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка пользовательского интерфейса")
@allure.description("UI тестирование")
@allure.feature("Электронный магазин")
@allure.severity("Critical")
def test_ui(driver):
    main_page = MainPage(driver)
    with allure.step("Открытие сайта"):
        main_page.open()
    with allure.step("Логотип Читай-город находится на сайте"):
        main_page.logo()
    with allure.step("Строка поиска отображается на сайте"):
        main_page.search()
    with allure.step("Верхнее поле хедера отоьражается на сайте"):
        main_page.header_top_margin()
    with allure.step("Поле хедера под строкой Поиск отображается на сайте"):
        main_page.header_bottom_margin()
    with allure.step("Открытие сайта"):
        main_page.reopening()
    with allure.step("Строка поиска отображается на сайте"):
        main_page.re_display()
    with allure.step("Вввод в строку Поиска необходимых данных"):
        main_page.input_into_field()
    with allure.step("Кнопка Лупа"):
        main_page.result()
    with allure.step("Открытие сайта"):
        main_page.go_to_website()
    with allure.step("Акция отображается на странице"):
        main_page.displayed()
    with allure.step("Кнопка Акция"):
        main_page.promotion()
    with allure.step("Отображение локатора Новинки литературы"):
        main_page.new()
    with allure.step("Проверка возможности добавить товар к Корзину"):
        main_page.add_product()
    with allure.step("Корзина"):
        main_page.add_cart()
    with allure.step("Открытие сайта"):
        main_page.open_page_new()
    with allure.step("Отображение локатора Обратная связь"):
        main_page.feedback()
    with allure.step("Кнопка Обратная связь"):
        main_page.press_the_button()

    search_page = SearchPage(driver)
    with allure.step("Отображение результатат поиска"):
        search_page.display_result()
    with allure.step("Результат поиска содержит наименование книги и автора"):
        search_page.fill_form()

    promotion_page = PromotionPage(driver)
    with allure.step("Отображенеи локатора Акции"):
        promotion_page.stock_locator()
    with allure.step("Результат поиска Акции"):
        promotion_page.stock()
    with allure.step("Проверка, что цена до акции больше"):
        promotion_page.prices()

    cart_page = CartPage(driver)
    with allure.step("Отображение выбранного товара в Корзине"):
        cart_page.cart()

    contacts_page = ContactsPage(driver)
    with allure.step("Отправить обращение"):
        contacts_page.send_a_request()
    with allure.step("Отображенеи номера телефона"):
        contacts_page.send_a_request()
