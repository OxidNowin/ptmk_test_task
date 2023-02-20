from db import *

import sys
import argparse
from datetime import datetime
import random


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('func', nargs=1, type=int)
    parser.add_argument('about', nargs='*')

    return parser


if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.func[0] == 1:
        create_table()
        print('Таблица успешно создана!')

    elif namespace.func[0] == 2:
        if len(namespace.about) < 3:
            print("Неверное количество переданных аргументов")
            sys.exit(1)
        try:
            birth_date = datetime.strptime(namespace.about[-2], '%d.%m.%Y')
        except ValueError:
            print("Неправильно указана дата")
            sys.exit(1)
        name = ' '.join(namespace.about[:-2])
        sex = namespace.about[-1]
        if len(name) >= 255 or len(sex) >= 255:
            print("Слишком большие значения аргументов")
            sys.exit(1)
        add_user([[name, birth_date, sex]])
        print('Пользователь успешно добавлен!')

    elif namespace.func[0] == 3:
        user_data = get_unique_user()
        print("    Name    |    birth_date    |    sex    |    year   |")
        for name, bd, sex, year in user_data:
            print(f"    {name}    |    {bd}    |    {sex}    |    {year}   |")

    elif namespace.func[0] == 4:
        data_to_load = []
        for _ in range(1000000):
            name = ''
            for i in range(3):
                len_name = random.randint(4, 7)
                name += chr(random.randint(65, 90))
                for ln in range(len_name-1):
                    name += chr(random.randint(97, 122))
                name += " "
            day = random.randint(1, 31)
            month = random.randint(1, 12)
            year = random.randint(1950, 2022)
            try:
                bd = datetime.strptime(f'{day}.{month}.{year}', '%d.%m.%Y')
            except ValueError:
                continue
            sex = 'female' if random.randint(0, 1) == 0 else 'male'
            data_to_load.append([name.rstrip(), bd, sex])
        add_user(data_to_load)
        print('Первый 1.000.000 загружен еще 100 на подходе!')

        another_data = []
        for _ in range(100):
            name = 'F'
            for i in range(3):
                len_name = random.randint(4, 7)
                name += chr(random.randint(65, 90))
                for ln in range(len_name-1):
                    name += chr(random.randint(97, 122))
                name += " "
            day = random.randint(1, 31)
            month = random.randint(1, 12)
            year = random.randint(1950, 2022)
            try:
                bd = datetime.strptime(f'{day}.{month}.{year}', '%d.%m.%Y')
            except ValueError:
                continue
            sex = 'male'
            another_data.append([name, bd, sex])
        add_user(another_data)
        print('Все данные загружены')

    elif namespace.func[0] == 5:
        time, user_data = get_f_users()
        print("    Name    |    birth_date    |    sex    |    year   |")
        for name, bd, sex, year in user_data:
            print(f"    {name}    |    {bd}    |    {sex}    |    {year}   |")
        print(f"Время выполнения запроса: {time} секунд")

    else:
        print(f"Неизвестное значение аргумента {namespace.func[0]}!")
        sys.exit(1)
