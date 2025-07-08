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
def test_header_elements_are_present(driver):
    main_page = MainPage(driver)
    with allure.step("Открытие сайта"):
        main_page.open_main_page()
    with allure.step("Закрытие всплывающего окна"):
        main_page.close_city_window()
    with allure.step("Логотип Читай-город находится на сайте"):
        main_page.wait_logo_is_present()
    with allure.step("Строка поиска отображается на сайте"):
        main_page.wait_search_field_is_present()
    with allure.step("Верхнее поле хедера отображается на сайте"):
        main_page.wait_header_top_margin_is_present()
    with allure.step("Поле хедера под строкой Поиск отображается на сайте"):
        main_page.wait_header_bottom_margin_is_present()


def test_search_field(driver):
    main_page = MainPage(driver)
    letters = "достоевский"
    with allure.step("Открытие сайта"):
        main_page.open_main_page()
    with allure.step("Закрытие всплывающего окна"):
        main_page.close_city_window()
    with allure.step("Вввод в строку Поиска необходимых данных"):
        main_page.input_into_field(search_letters=letters)
    with allure.step("Кнопка Лупа"):
        main_page.click_on_search_button()
    search_page = SearchPage(driver)
    with allure.step("Отображение результатат поиска"):
        search_page.display_result(search_letters=letters)


def test_send_message_contacts_page_present(driver):
    main_page = MainPage(driver)
    with allure.step("Открытие сайта"):
        main_page.open_main_page()
    with allure.step("Закрытие всплывающего окна"):
        main_page.close_city_window()
    with allure.step("Нажатие кнопки обратной связи"):
        main_page.wait_feedback_button_is_present()
    contacts_page = ContactsPage(driver)
    with allure.step("Отображается кнопка Отправить обращение"):
        contacts_page.wait_send_request_button_is_present()


def test_non_authorized_user_cart_is_empty(driver):
    main_page = MainPage(driver)
    with allure.step("Открытие сайта"):
        main_page.open_main_page()
    with allure.step("Закрытие всплывающего окна"):
        main_page.close_city_window()
    with allure.step("Переход в корзину"):
        main_page.go_to_cart_page()
    cart_page = CartPage(driver)
    with allure.step("Отображение теста В корзине ничего нет"):
        cart_page.wait_text_nothing_in_cart()


def test_go_to_promotion_page(driver):
    main_page = MainPage(driver)
    with allure.step("Открытие сайта"):
        main_page.open_main_page()
    with allure.step("Закрытие всплывающего окна"):
        main_page.close_city_window()
    with allure.step("Переход на страницу акции"):
        main_page.wait_promotion_is_present()
    promotion_page = PromotionPage(driver)
    with allure.step("Проверка перехода на страницу акции"):
        promotion_page.check_promotion_page_is_open()
