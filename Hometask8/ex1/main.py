'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.

'''


class Date:
    def __init__(self, date):
        self.date = date
        # self.input_date = input('Введите дату в фодмате "дд-мм-гггг": ')

    @property
    def true_date(self):
        day, month, year = self.formating(self.date)
        if self.validation(day, month, year):
            print(f'{day} число {month} месяца {year} года')
        else:
            print('Неверный ввод данных')

    @classmethod
    def formating(cls, date):
        day, month, year = map(int, date.split('-'))
        return day, month, year

    @staticmethod
    def validation(day, month, year):
        days = {
                    1: 31,
                    2: 29,
                    3: 31,
                    4: 30,
                    5: 31,
                    6: 30,
                    7: 31,
                    8: 31,
                    9: 30,
                    10: 31,
                    11: 30,
                    12: 31

                }
        return True if 0 < month < 12 and 0 < day <= days[month] and 1790 < year <= 2025 else False



info = input('Введите дату в формате дд-мм-гггг: ')
obj_1 = Date(info)
obj_1.true_date


