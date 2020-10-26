'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color
(цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках
метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго
(желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между
режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.

'''

import time
from itertools import cycle


class TrafficLight:
    __colour = {'red': 7,
                'yellow': 2,
                'green': 10
                }

    def running(self):
        c = 0
        for light, value in cycle(self.__colour.items()):
            if c > 12:
                break
            print(light)
            time.sleep(value)
            c += 1


traffic_light = TrafficLight()
traffic_light.running()

'''
# если надо желтый 2 раза повторять:

import time
from itertools import cycle


class TrafficLight:
    colour = {1: ['red', 7],
              2: ['yellow', 2],
              3: ['green', 10],
              4: ['yellow', 2],
              }

    def switch_colour(self):
        c = 0
        for value in cycle(self.colour.values()):
            if c > 12:
                break
            print(value[0])
            time.sleep(value[1])
            c += 1


traffic_light = TrafficLight()
traffic_light.switch_colour()'''

