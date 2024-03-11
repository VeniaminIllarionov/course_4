import json

from src.requests_hh import Request_HH


class Vacansy(Request_HH):

    def __init__(self, name: str, salary: int, city: str):
        """Инициализируем с атрибутами:
        name: str - Наименование профессии,
        salary - Зарплата,
        city - Город"""
        super().__init__(name)
        self.constr_vacansy = []
        self.count = 0
        self.salary = salary
        self.city = city
        self.found_vacansy = []  # Наденные вакансии
        self.top_salary = 0  # Наибольшая зарплата

    def vacansy(self):
        if len(self.all_vacansy) >= 1:
            for vacansy in self.all_vacansy:
                if vacansy["salary"] is not None and vacansy["salary"]["from"] is not None:
                    if vacansy['area']['name'] == self.city:
                        if vacansy['salary']['from'] >= self.salary and vacansy['salary']['from'] is not None:
                            self.found_vacansy.append(vacansy)
            return self.found_vacansy
        else:
            self.message = "Вакансии не найдены"
            return self.message

    def construction(self):
        for i in self.found_vacansy:
            if i['salary']['to'] is None:
                i['salary']['to'] = 0
            self.constr_vacansy.append(f"{self.count + 1}.{i['name']}, \nЗарплата от: {i['salary']['from']}, "
                                       f"\nЗарплата до: {i['salary']['to']}, "
                                       f"\nТребование: {i['snippet']['requirement']}, "
                                       f"\nТребуется: {i['snippet']['responsibility']}, "
                                       f"\nГород: {i['area']['name']}, "
                                       f"\nСсылка на вакансию: {i['alternate_url']}")
            self.count += 1
        return self.constr_vacansy

    def __str__(self):
        """Вывод подобранных вакансий"""
        if self.count > 0:
            print(f'Найдены вакансии в колличестве {self.count}, с максимальной зарплатой {self.top_salary} :\n')
            for v in self.constr_vacansy:
                print(f'{v}\n')
        else:
            self.message = "Вакансии не найдены."
            print(self.message)

    def top_vacansy(self):
        """Переборка зарплаты и выбор наибольшей зарблаты"""
        for i in self.found_vacansy:
            if i['salary']['from'] > self.top_salary:
                self.top_salary = i['salary']['from']
        return self.top_salary
