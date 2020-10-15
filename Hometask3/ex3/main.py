'''
3. Реализовать функцию my_func(), которая принимает
три позиционных аргумента, и возвращает сумму
наибольших двух аргументов.

'''


def my_func(arg1, arg2, arg3):
    result = arg1 + arg2 + arg3 - min(arg1, arg2, arg3)
    return result


print(my_func(1, 2, 3))

