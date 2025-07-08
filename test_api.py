import pytest
import allure
from selenium import webdriver
from pages.BooksPage import BooksPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование работы электронного магазина")
@allure.description("Тест проверяет коррекность работы сайта заказов")
@allure.feature("Электронный магазин")
@allure.severity("Criticall")
def test_search(driver):
    books_page = BooksPage(driver)
    with allure.step("Поиск на кириллице"):
        books_page.book_search()
    with allure.step("Поиск на латинице"):
        books_page.search_english()
    with allure.step("поиск с пустой формой"):
        books_page.empty()
    with allure.step("Поиск с названием с цифрами"):
        books_page.search_numbers()
    with allure.step("Поиск с символами"):
        books_page.search_symbols()
