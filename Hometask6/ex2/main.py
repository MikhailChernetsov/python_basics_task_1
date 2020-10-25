'''
2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого
для покрытия всего дорожного полотна. Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т

'''


class Road:
    _length = None
    _width = None

    def __init__(self):
        Road._length, Road._width = map(int, input('Введите длину и ширину дороги через пробел: ').split())

    def mass(self, mas_1_layer, layers):
        massa = self._length * self._width * mas_1_layer * layers
        print(f'Понадобится {round(massa/1000)} тонн асфальта')


road_1 = Road()
road_1.mass(mas_1_layer=int(input('Введите массу одного слоя: ')), layers=int(input('Введите количество слоев: ')))

