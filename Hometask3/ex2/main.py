'''
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
'''
# Вариант 1
print('Первый вариант решения')


def one_string_info(**kwargs):
    print('Ваши данные:', end=' ')
    for key, item in kwargs.items():
        print(f'{key} - {item};', end=' ')
    print()


one_string_info(имя='Михаил', фамилия='Чернецов', возраст=27, родной_город = 'Москва')

# Вариант 2
print('Второй вариант решения')


def one_string_info2(name, second_name, birth_year, city, email):
    print(f'Ваши данные: имя - {name}, фамилия - {second_name}, год рождения - {birth_year}, город проживания - {city}, email - {email}')


one_string_info2(name='Михаил', second_name='Чернецов', birth_year=1991, city='Зеленоград', email='mixail2525@yandex.ru')

