import json

from src.requests_hh import Request_HH


class Vacansy(Request_HH):
    def __init__(self, name: str, salary: int, city: str):
        """Инициализируем с атрибутами:
        name: str - Наименование профессии,
        salary - Зарплата,
        city - Город"""
        super().__init__(name)
        self.salary = salary
        self.city = city
        self.found_vacansy = []  # Наденные вакансии
        self.top_salary = 0  # Наибольшая зарплата

    def vacansy(self):
        for vacansy in self.all_vacansy:
            if vacansy["salary"] is not None and vacansy["salary"]["from"] is not None:
                if vacansy['area']['name'] == self.city:
                    if vacansy['salary']['from'] >= self.salary and vacansy['salary']['from'] is not None:
                        self.found_vacansy.append(vacansy)
        return self.found_vacansy

    def top_vacansy(self):
        """Переборка зарплаты и выбор наибольшей зарблаты"""
        for i in self.found_vacansy:
            if i['salary']['from'] > self.top_salary:
                self.top_salary = i['salary']['from']
        return self.top_salary

    def __str__(self):
        """Вывод подобранных вакансий"""
        vacs = []
        count = 1
        if len(self.all_vacansy) >= 1:
            for i in self.found_vacansy:
                if i['salary']['to'] is None:
                    i['salary']['to'] = 0
                vacs.append(f"{count}.{i['name']}, Зарплата от: {i['salary']['from']}, "
                            f"Зарплата до: {i['salary']['to']}, "
                            f"Город: {i['area']['name']}, "
                            f"Ссылка на вакансию: {i['alternate_url']}")
                count += 1
            print(f'Найдены вакансии в колличестве {count}, с максимальной зарплатой: {self.top_vacansy()}:')
            for v in vacs:
                print(v)
        else:
            self.message = "Вакансии не найдены"
            print(self.message)



