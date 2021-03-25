"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение
и завершать скрипт.
"""

import time


class TrafficLight:

    def __init__(self, colors):
        self.__colors = colors

    __color = ""
    __colors = dict()

    def running(self):
        i = 0
        while True:
            color_object = self.__colors[i % len(self.__colors)]
            self.set_color(color_object["name"])
            time.sleep(color_object["timeout"])
            i += 1

    def set_color(self, color):
        print(f"Новый цвет: {color}")
        self.__color = color


traffic = TrafficLight({
    0: {
        "name": "red",
        "timeout": 7
    },
    1: {
        "name": "yellow",
        "timeout": 2
    },
    2: {
        "name": "green",
        "timeout": 5
    }
})
traffic.running()
