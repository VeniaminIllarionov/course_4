from src.class_vacansy import Vacansy


def main():
    print("Введите пожалуйста, вакансию которую хотели бы найти")
    user_name = input().title()
    while True:
        print("Введите пожалуйста, зарплату которую хотели бы получать")
        user_salary = int(input())
        if type(user_salary) is int:
            break
        print("Попробуйте еще!")

    while True:
        print(("Введите пожалуйста, город где хотели бы найти работу"))
        user_city = input().title()
        if type(user_city) is str:
            break
        print("Попробуйте еще!")
    user = Vacansy(name=user_name, salary=user_salary, city=user_city)
    user.vacansy()
    user.top_salary
    user.__str__()


if __name__ == '__main__':
    main()
