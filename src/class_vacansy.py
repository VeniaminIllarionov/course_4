import json
from src.confing import DATA



class Vacansy:

    def __init__(self, salary: int, city: str):
        """Инициализируем с атрибутами:
        salary - Зарплата,
        city - Город"""
        self.constr_vacansy = []  # Пустой лист для сортировки вакансий по 'городу' и 'желаемой зарплаты'
        self.count = 0  # Счетчик количества найденных вакансий
        self.salary = salary
        self.city = city
        self.found_vacansy = []  # Наденные вакансии
        self.top_salary = 0  # Наибольшая зарплата
        self.message = 'Вакансии найдены'
        self.rd_vacansy = None

    def read_vacansy(self):
        """Чтение файла с поиском вакансий"""
        with open(DATA, encoding='utf-8') as f:
            self.rd_vacansy = (json.load(f))
            return self.rd_vacansy

    def vacansy(self):
        for vacansy_d in self.rd_vacansy:
            if vacansy_d["salary"] is not None and vacansy_d["salary"]["from"] is not None:
                if vacansy_d['area']['name'] == self.city:
                    if vacansy_d['salary']['from'] >= self.salary:
                        self.found_vacansy.append(vacansy_d)
        return self.found_vacansy

    def construction(self):
        """Функция для формирования полученной информации"""
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



