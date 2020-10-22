'''
2. Создать текстовый файл (не программно), сохранить в нем
несколько строк, выполнить подсчет количества строк, количества
слов в каждой строке.

'''
with open('text_2.txt', 'r', encoding='utf-8') as my_file:
    number_of_strings = 0
    for line in my_file:
        line = line.split()
        print(f'Количество слов в строке {number_of_strings+1}: {len(line)} слов(а)')

        number_of_strings += 1
print(f'Общее количество строк в файле: {number_of_strings}')
