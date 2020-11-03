'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное
название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды
существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть
обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов
на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом
уроке знания: реализовать абстрактные классы для основных классов проекта, проверить
на практике работу декоратора @property.

'''
from abc import ABC, abstractmethod


class Clothes(ABC):
    name = None

    @abstractmethod
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return f'Расход ткани на {self.name}: {self.consumption}'

    def __add__(self, other):
        return self.consumption + other.consumption

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    name = 'пальто'

    def __init__(self, h):
        super().__init__(param=h)

    @property
    def consumption(self):
        return 2 * self.param + 0.3


class Suite(Clothes):
    name = 'костюм'

    def __init__(self, v):
        super().__init__(param=v)

    @property
    def consumption(self):
        return self.param / 6.5 + 0.5


my_coat = Coat(1)
print(my_coat.consumption)

my_suite = Suite(13)
print(my_suite.consumption)

print(my_coat)
print(my_suite)
print(my_coat + my_suite)

