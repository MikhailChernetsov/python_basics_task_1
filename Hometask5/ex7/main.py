'''
7. Создать (не программно) текстовый файл, в котором каждая строка
должна содержать данные о фирме: название, форма собственности, выручка,
издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней
прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их
прибылями, а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
{“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.

'''
import json

firms = {}
total_profit = 0
number_of_firms = 0
with open('text_7.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        line = line.split()
        profit = float(line[2]) - float(line[3])
        firms[line[0]] = profit
        if profit > 0:
            total_profit += profit
            number_of_firms += 1

average_profit = total_profit / number_of_firms

result = [firms, {'average_profit': average_profit}]
print(result)

with open('exercise_7.json', 'w') as file_json:
    json.dump(result, file_json)



