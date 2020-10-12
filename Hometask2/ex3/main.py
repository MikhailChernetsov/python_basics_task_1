'''3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

print('*** ВАРИАНТ РЕШЕНИЯ ЧЕРЕЗ СПИСОК ***')
user_month = input('Введите число от 1 до 12 ')

winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
full = [9, 10, 11]

while user_month.isdigit() == False or int(user_month) > 12 or user_month == '0':
    print('Необходимо вводить данные целыми положительными числами!')
    user_month = input('Введите месяц в виде целого числа от 1 до 12: ')

user_month = int(user_month)
if user_month in winter:
    print('Ваш месяц ЗИМА')
elif user_month in spring:
    print('Ваш месяц ВЕСНА')
elif user_month in summer:
    print('Ваш месяц ЛЕТО')
else:
    print('Ваш месяц ОСЕНЬ')


print('*** ВАРИАНТ РЕШЕНИЯ ЧЕРЕЗ СЛОВАРЬ ***')

user_month = input('Введите месяц в виде целого числа от 1 до 12: ')

while user_month.isdigit() == False or int(user_month) > 12 or user_month == '0':
    print('Необходимо вводить данные целыми положительными числами!')
    user_month = input('Введите месяц в виде целого числа от 1 до 12: ')

my_dict = {
    1: 'зима',
    2: 'зима',
    3: 'весна',
    4: 'весна',
    5: 'весна',
    6: 'лето',
    7: 'лето',
    8: 'лето',
    9: 'осень',
    10: 'осень',
    11: 'осень',
    12: 'зима'
}
result = my_dict.get(int(user_month))
print(f'Ваш месяц {result}')
