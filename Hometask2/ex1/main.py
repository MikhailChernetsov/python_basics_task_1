'''
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать
функцию type() для проверки типа. Элементы списка можно не запрашивать
у пользователя, а указать явно, в программе.

'''
my_list = [8, 25.3, 'some string', True, [1, 3, 5], ('element', 16), {'key': 62}, None]
for elem in my_list:
    print(type(elem))
