import allure
import pytest
from selenium import webdriver
from pages.SitePage import SitePage


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
    
    site_page = SitePage(driver)

    with allure.step("Открытие сайта"):
    site_page.open()
    with allure.step("Эмблема"):
    site_page.element()
    with allure.step("Текс в поисковой строке"):
    site_page.element_text()
    with allure.step("Состояние элемента"):
    site_page.element_enabled()
    with allure.step("Акция"):
    site_page.click_element()
    with allure.step("Навигация по сайту"):
    site_page.navigation()
