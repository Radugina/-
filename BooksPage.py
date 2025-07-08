import allure
import requests
from config import BASE_URL


class BooksApi:
    def __init__(self, url):
        self.url = url
        self.headers = {"Authorization": f"Bearer {token}"}

    @allure.step("Поиск по названию товара на русском языке")
    def book_search(self, params):
        params = {
            "customerCityId": 10748,
            "phrase": "Вино из одуванчиков",
            "products[page]": 1,
            "products[per-page]": 60
            }
        resp = requests.get(
            self.url + 'search/product', params=params, headers=self.headers)
        return resp.json()

    @allure.step("Поиск по названию товара на английском языке")
    def search_english(self, params):
        params = {
            "customerCityId": 10748,
            "phrase": "bronte",
            "products[page]": 1,
            "products[per-page]": 60
            }
        resp = requests.get(
            self.url + 'search/product', params=params, headers=self.headers)
        return resp.json()

    @allure.step("Пустой запрос")
    def empty(self, params):
        params = {
            "customerCityId": 10748,
            "phrase": "",
            "products[page]": 1,
            "products[per-page]": 60
            }
        resp = requests.get(
            self.url + 'search/product', params=params, headers=self.headers)
        return resp.json()

    @allure.step("Поиск по названию с цифрами")
    def search_numbers(self, params):
        params = {
            "customerCityId": 10748,
            "phrase": "99 франков",
            "products[page]": 1,
            "products[per-page]": 60
            }
        resp = requests.get(
            self.url + 'search/product', params=params, headers=self.headers)
        return resp.json()

    @allure.step("Поиск по символовам")
    def search_symbols(self, params):
        params = {
            "customerCityId": 10748,
            "phrase": "^&^&^^%%%%",
            "products[page]": 1,
            "products[per-page]": 60
            }
        resp = requests.get(
            self.url + 'search/product', params=params, headers=self.headers)
        return resp.json()
