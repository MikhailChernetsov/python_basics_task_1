'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и
считывающую построчно данные. При этом английские числительные
должны заменяться на русские. Новый блок строк должен записываться
в новый текстовый файл.

'''
translate = {'one': 'один',
             'two': 'два',
             'three': 'три',
             'four': 'четыре'
             }

with open('text_4.txt', 'r', encoding='utf-8') as my_file:
    with open('text_4_2.txt', 'w', encoding='utf-8') as my_file_2:
        for line in my_file:
            line = line.split()
            line[0] = translate[line[0].lower()]
            line = ' '.join(line)
            print(line)
            my_file_2.writelines(line)
            my_file_2.writelines('\n')

