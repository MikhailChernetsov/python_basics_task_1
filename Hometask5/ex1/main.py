'''
1. Создать программно файл в текстовом формате, записать в него
построчно данные, вводимые пользователем. Об окончании ввода
данных свидетельствует пустая строка.

'''
try:
    with open('new_text_1.txt', 'w', encoding='utf-8') as file:
        user_string = True
        while user_string:
            user_string = input('Введите строку для записи в файл:')
            file.writelines(user_string)
            file.writelines('\n')
except IOError:
    print('Произошла ошибка ввода-вывода')

