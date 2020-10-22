'''
3. Создать текстовый файл (не программно), построчно записать
фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников.

'''
poore_stuff = []
summ = 0
number_of_stuff = 0
with open('text_3.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        line = line.split()
        print(f'{line[0]} - оклад {line[1]} р')
        summ += float(line[1])
        number_of_stuff += 1
        if float(line[1]) < 20000:
            poore_stuff.append(line[0])

print('Список сотрудников с окладом менее 20 т.р.: ')
for num, surname in enumerate(poore_stuff, 1):
    print(num, surname)
summ = summ/number_of_stuff
print(f'Средняя величина дохода сотрудников составляет {summ}')

