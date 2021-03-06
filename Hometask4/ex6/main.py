'''
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а
при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть
условие, при котором повторение элементов списка будет прекращено.

'''

from itertools import cycle


def iterator(min_el, max_el):
    from itertools import count
    list = []

    for el in count(min_el):
        if el > max_el:
            break
        else:
            list.append(el)
    return list


my_list = iterator(3, 10)
print(my_list)

num_iter = 0
for el in cycle(my_list):
    if num_iter >= 15:
        break
    print(el)
    num_iter += 1

