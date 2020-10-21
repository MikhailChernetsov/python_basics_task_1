'''
5. Создать (программно) текстовый файл, записать в него программно
набор чисел, разделенных пробелами. Программа должна подсчитывать
сумму чисел в файле и выводить ее на экран.

'''
with open('new_text_5.txt', 'w+', encoding='utf-8') as my_file:
    user_string = input('Введите строку чисел через пробелы для записи в файл:')
    my_file.writelines(user_string)
    user_string = user_string.split()
    my_file.seek(0)
    summa = sum(map(int, user_string))
    print(summa)


