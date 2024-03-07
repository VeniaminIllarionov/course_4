import json

from abstract_hh import Abstr_HH
import requests

from confing import DATA


class Request_HH(Abstr_HH):
    def __init__(self):
        self.url_get = "https://api.hh.ru/vacancies"  # используемый адрес для отправки запроса
        self.all_vacansy = []

    def get_url(self):
        response = requests.get(self.url_get)  # отправка GET-запроса
        return response.json()

    def write_json(self):
        with open(DATA, 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.all_vacancy, ensure_ascii=False))
            return self.all_vacancy

    def __repr__(self):
        return self.all_vacansy



