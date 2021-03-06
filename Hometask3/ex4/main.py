'''
4. Программа принимает действительное положительное число
x и целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо
реализовать в виде функции my_func(x, y). При решении
задания необходимо обойтись без встроенной функции
возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.
'''

# СПОСОБ 1 - возведение в степень с помощью оператора **


def my_func(x, y):
    return x**y


print(my_func(2, -3))

# способ 2 - реализация без оператора **


def my_func1(x, y):
    y = -y
    result = 1
    for i in range(y):
        result /= x
    return result


print(my_func1(2, -3))

# способ 3 - рекурсия


def my_func_recursive(x, y):
    if y > 0:
        return 'Степень должна быть отрицательной!'
    elif y == 0:
        return 1
    else:
        return 1/x * my_func_recursive(x, y+1)


print(my_func_recursive(2, -3))

