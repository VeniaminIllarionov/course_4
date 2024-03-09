from src.class_vacansy import Vacansy


def main():
    user_name = input("Введите пожалуйста, вакансию которую хотели бы найти")
    while True:
        user_salary = int(input("Введите пожалуйста, зарплату которую хотели бы получать"))
        if type(user_salary) is int:
            break
    while True:
        user_city = input("Введите пожалуйста, город где хотели бы найти работу").title()
        if user_city.isalpha():
            break
    user = Vacansy(name=user_name, salary=user_salary, city=user_city)
    user.vacansy()
    user.top_salary
    user.__str__()


if __name__ == '__main__':
    main()
