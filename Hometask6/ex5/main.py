'''
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.

'''


class Stationery:
    def __init__(self, title=''):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Ручка рисует {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Карандаш рисует {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Маркер рисует {self.title}')


stat1 = Stationery()
stat1.draw()

pen = Pen('домик')
pen.draw()

pencil = Pencil('дерево')
pencil.draw()

handle = Handle('озеро')
handle.draw()



'''
# еще один вариант, зачем нужен title. Название атрибута не очень подошло здесь, зато его использование в классе вроде логично


class Stationery:
    title = 'черный'

    def draw(self,):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self, thing):
        print(f'Ручка рисует {self.title} {thing}')


class Pencil(Stationery):
    def draw(self, thing):
        print(f'Карандаш рисует {self.title} {thing}')


class Handle(Stationery):
    def draw(self, thing):
        print(f'Маркер рисует {self.title} {thing}')


stat1 = Stationery()
stat1.draw()

pen = Pen()
pen.title = 'синий'
pen.draw('кружок')

pencil = Pencil()
pencil.draw('дом')

handle = Handle()
handle.title = 'красный'
handle.draw('воздушный шар')'''


