'''
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка
из слов, разделенных пробелом. Каждое слово состоит из латинских букв
в нижнем регистре. Сделать вывод исходной строки, но каждое слово
должно начинаться с заглавной буквы. Необходимо использовать
написанную ранее функцию int_func().
'''


def int_func(some_word):
    some_word = list(some_word)
    some_word[0] = chr(ord(some_word[0]) - 32)
    some_word = "".join(some_word)
    return some_word


some_string = input('Введите строку: ')

print(f'Из "{some_string}" ', end=' ')

some_string = some_string.split()
for i in range(len(some_string)):
    if some_string[i].isdigit():
        continue
    else:
        some_string[i] = int_func(some_string[i])


some_string = ' '.join(some_string)
print(f'получилось "{some_string}"')
