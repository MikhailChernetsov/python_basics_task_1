'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий
склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках
реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.

'''


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse: # склад
    def __init__(self):
        self.things = []
        self.output = {}

    def to_take(self, subj, quantity):
        thing = {'тип': subj.name, 'фирма': subj.firm, 'модель': subj.model, 'цветной': 'да' if subj.is_colour else 'нет',
                 'количество': quantity}
        self.things.append(thing)

    def watch(self):
        print('В наличии на складе следующая оргтехника:')
        for i, obj in enumerate(self.things, 1):
            print(i, obj)

    def give_out(self, number, quantity, subdivision):
        element = self.things[number-1]
        quantity_now = element["количество"]
        if element['количество'] > quantity:
            element['количество'] -= quantity
        else:
            print(f'В наличии {element["количество"]} единиц данной позиции.')
            self.things.remove(element)
        print(f'{quantity if quantity_now >= quantity else element["количество"]} {element["тип"]}(а) отправлено в подразделение "{subdivision}"')


class OfficeEquipment: # оргтехника
    def __init__(self, firm, model):
        self.firm = firm
        self.model = model


class Printer(OfficeEquipment):
    name = 'принтер'

    def __init__(self, firm, model, is_colour=False):
        super().__init__(firm, model)
        self.is_colour = is_colour


class Scanner(OfficeEquipment):
    name = 'сканер'

    def __init__(self, firm, model, is_colour=True):
        super().__init__(firm, model)
        self.is_colour = is_colour


class Xerox(OfficeEquipment):
    name = 'ксерокс'


# добавили пару принтеров на склад, чтоб не был пустой
printer1 = Printer('Philips', 'Ph-252')
printer2 = Printer('HP', 'One', True)

warehouse = Warehouse()
warehouse.to_take(printer1, 5)
warehouse.to_take(printer2, 15)
warehouse.watch()
print()

# отправили несколько принтеров в бухгалтерию (тест программы)
warehouse.give_out(1, 3, "бухгалтерия")
warehouse.watch()
print()

# menu
tips = 'Справка:\nВведите 1, чтоб посмотреть список оргтехники, хранящейся на складе.\n' \
       'Введите 2, чтобы добавить новую единицу на склад\nВведите 3, чтоб выдать оргтехнику со склада в подразделение' \
       '\nВведите # для выхода из программы\nНаберите help для вывода справки'
print(tips)
while True:
    user_answer = input('Ввод: ')
    if user_answer == '1': # посмотреть, что есть
        warehouse.watch()
    elif user_answer == '2': # добавить
        user_answer = input('Какое устройство необходимо добавить на склад? Если принтер - нажмите 1, '
                            'если сканер - 2, если ксерокс - 3\nДля возвращения в главное меню введите # ')
        while not (user_answer == '1' or user_answer == '2' or user_answer == '3' or user_answer == '#'):
            print('Неверный ввод!')
            user_answer = input('Какое устройство необходимо добавить на склад? Если принтер - нажмите 1, '
                                'если сканер - 2, если ксерокс - 3\nДля возвращения в главное меню введите #')
        if user_answer != '#':
            print('Введите следующие параметры:')
            firm = input('Введите фирму: ')
            model = input('Введите модель устройства: ')
            colour = input('Цветное ли устройство? Если да - введите любой текст, если нет - оставьте пустую строку ')
            colour = True if colour else False
            if user_answer == '1':
                device = Printer(firm, model, colour)
            elif user_answer == '2':
                device = Printer(firm, model, colour)
            elif user_answer == '3':
                device = Printer(firm, model, colour)
            while True:
                try:
                    n = int(input('Введите количество: '))
                    if n == 0:
                        raise OwnError('Количество не может быть нулевым')
                except ValueError:
                    print('Неверный ввод данных!')
                except OwnError as err:
                    print(err)
                else:
                    break
            warehouse.to_take(device, n)
            print('Добавлено!')

    elif user_answer == '3': # выдать куда-то
        warehouse.watch()
        n_position = input('Введите текущий номер позиции товара, который необходимо выдать.(для выхода нажмите #) ')
        if n_position != '#':
            while True:
                try:
                    n_position = int(n_position)
                except ValueError:
                    print('Данные необходимо вводить числами!')
                else:
                    break
            while True:
                try:
                    quantity = int(input('Количество выдаваемых устройств: '))
                    if quantity == 0:
                        raise OwnError('Количество не может быть нулевым')
                except ValueError:
                    print('Данные необходимо вводить числами!')
                except OwnError as err:
                    print(err)
                else:
                    break
            subdivision = input('Подразделение, куда выдаем устройства: ')
            warehouse.give_out(n_position, quantity, subdivision)
    elif user_answer == 'help':
        print(tips)
    elif user_answer == '#':
        print('Выход из программы')
        break
    else:
        print('Неверный ввод!\n', tips)




