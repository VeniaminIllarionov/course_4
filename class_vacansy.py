from requests_hh import Request_HH


class Vacansy(Request_HH):
    def __init__(self, name: str, from_salary: float, to_salary: float, city: str):
        """Инициализируем с атрибутами:
        name: str - Наименование профессии,
        from_salary - Начальная зарплата,
        to_salary - До Зарплата,
        city - Страна"""
        super().__init__()
        self.name = name
        self.from_salary = from_salary
        self.city = city
        self.to_salary = to_salary


