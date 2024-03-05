from abstract_hh import Abstr_HH
import requests


class Request_HH(Abstr_HH):
    def __init__(self):
        pass
    def get_url(self):
        url_get = "https://api.hh.ru/vacancies"  # используемый адрес для отправки запроса

        response = requests.get(url_get)  # отправка GET-запроса

        print(response)  # вывод объекта класса Response
        # Вывод:
        # >> <Response [200]>
        print(response.json())
