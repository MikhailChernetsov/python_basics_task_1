'''Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.'''

proceeds = int(input('Введите прибыль  '))
cost = int(input('Введите издержки фирмы '))

if proceeds < cost:
        losses = cost - proceed
        print('Ваши убытки составили: ', losses)
elif proceeds > cost:
        profit = proceeds - cost
        print('Ваша прибль составила: ', profit)
        profitability = profit / proceeds
        print('Рентабильность фирмы составляет: ', profitability)
        worker_amount = int(input('Введите колличество сотрудников '))
        profit_one_worker = profit / worker_amount
        print('Прибыль на каждого сотрудника составляет ', profit_one_worker)
else:
    print('Вы вышли в ноль')

