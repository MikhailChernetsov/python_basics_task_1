'''Пользователь вводит целое положительное число. Найдите самую большую
 цифру в числе. Для решения используйте цикл while и арифметические операции.'''

n = int(input('Введите  многозначное число: '))
max_number = 0
while n != 0:
    last_number = n % 10
    if max_number < last_number:
        max_number = last_number
    else:
        n = n // 10
print('Наибольшая цифра в числе  ', max_number)
