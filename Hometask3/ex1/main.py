'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.

'''
# Вариант 1 - через исключения


def division(dividend, divisor):
    try:
        result = dividend / divisor
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    except ValueError:
        return 'Некорректный ввод данных'
    else:
        return result


# Вариант 2


def division2(dividend, divisor):
    if divisor == 0:
        return 'На ноль делить нельзя'
    else:
        return dividend / divisor


my_dividend = input('Введите делимое: ')
my_divisor = input('Введите делитель: ')

while not my_dividend.isdigit() or not my_divisor.isdigit():
    print('Данные необходимо вводить числами! Повторите ввод!')
    my_dividend = input('Введите делимое: ')
    my_divisor = input('Введите делитель: ')

my_dividend = int(my_dividend)
my_divisor = int(my_divisor)

print('Результат работы первой функции:', end=' ')
print(division(my_dividend, my_divisor))

print('Результат работы второй функции:', end=' ')
print(division2(my_dividend, my_divisor))
