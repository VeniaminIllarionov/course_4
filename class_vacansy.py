import json

from requests_hh import Request_HH


class Vacansy(Request_HH):
    def __init__(self, name: str, salary: int, city: str):
        """Инициализируем с атрибутами:
        name: str - Наименование профессии,
        salary - Зарплата,
        city - Город"""
        super().__init__(name)
        self.salary = salary
        self.city = city
        self.search_vacansy = []

    def vacansy(self):
        for vacansy in self.all_vacansy:
            if vacansy["salary"] is not None and vacansy["salary"]["from"] is not None:
                if vacansy['area']['name'] == self.city:
                    if vacansy['salary']['from'] >= self.salary and vacansy['salary']['from'] is not None:
                        self.search_vacansy.append(vacansy)
        return self.search_vacansy


ddd = Vacansy('Разработчик', 80_000, "Москва")

print(ddd.vacansy())
