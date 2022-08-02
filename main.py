from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
def run():
    while True:
        print(datetime.date(2022,8,2))
        command = input('Введите команду: ')
        if command == 'c':
            print(calculate_salary(3, '+', 4))
        elif command == 'e':
            print(get_employees(input('Введите имя: ')))
        elif command == 'ex':
            break
if __name__ == '__main__':
  run()
