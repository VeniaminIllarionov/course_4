import json

from typing import Any

from src.abstract_hh import Abstr_HH
import requests

from src.confing import DATA


class Request_HH(Abstr_HH):

    def __init__(self, name: str):
        self.name = name
        self.message = 'Вакансии найдены'
        self.all_vacansy = self.get_url()

    def get_url(self) -> str | Any:
        """Поиск по названию"""

        if isinstance(self.name, str):
            keys_response = {'text': f'NAME:{self.name}', 'area': 113, 'per_page': 100, }
            info = requests.get(f'https://api.hh.ru/vacancies', keys_response)
            return json.loads(info.text)['items']

    def save_info(self) -> str or list:
        """Создание json файла с найдеными вакансиями"""

        if self.__len__() == 0:
            self.message = "Вакансии не найдены"
            return self.message
        else:
            with open(DATA, 'w', encoding='utf-8') as file:
                file.write(json.dumps(self.all_vacansy, ensure_ascii=False))
            return self.all_vacansy

    def __repr__(self):
        return self.all_vacansy

    def __len__(self):
        return len(self.all_vacansy)






