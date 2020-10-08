'''Спортсмен занимается ежедневными пробежками. В первый день его результат
составил a километров. Каждый день спортсмен увеличивал результат на 10 %
относительно предыдущего. Требуется определить номер дня, на который общий результат
спортсмена составить не менее b километров. Программа должна принимать значения
параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.'''

first_day_score = int(input("Сколько вы пробежали в первый день ?  "))
goal_score = int(input("К какому результату вы стремитесь ?  "))
#increase = 10
day = 1

while first_day_score < goal_score:
    first_day_score = first_day_score * 1.1
    print(f'{day}-й день: {first_day_score:.2f}')
    day += 1
print(f'На {day} день вы достигнете результата - не мение {goal_score} км.')

