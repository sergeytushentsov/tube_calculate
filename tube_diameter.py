"""Расчет диаметра трубопровода, скорости потока или расхода.

Функции:
    calc_diameter(velocity, volume)
    calc_velocity(volume, diameter)
    calc_volume(velocity, diameter)
 """
import math


def calc_diameter(velocity, volume):
    """Расчет диаметра трубопровода."""
    return math.sqrt(volume / (0.785 * velocity * 3600)) * 1000


def calc_velocity(volume, diameter):
    """Расчет скорости потока в трубопроводе."""
    return volume / ((diameter / 1000) ** 2 * 0.785 * 3600)


def calc_volume(velocity, diameter):
    """Расчет расхода в трубопроводе."""
    return (diameter / 1000) ** 2 * 0.785 * 3600 * velocity


parameter = 1

parameters = ["d", "v", "w"]

while parameter:
    parameter = input("Введите параметр, который Вы хотите посчитать: "
                      "d - диаметр; v - расход; w - скорость; "
                      "0 - для выхода из программы: ")

    if parameter == "0":
        break
    elif parameter not in parameters:
        print("Параметр введен некорректно. Повторите ввод параметра.")
    else:
        if parameter == "d":
            velocity_1 = float(input("Введите скорость, м/с: "))
            volume_1 = float(input("Введите расход, м3/ч: "))
            print("Диаметр равен ", calc_diameter(velocity_1, volume_1), "мм")
        elif parameter == "v":
            velocity_2 = float(input("Введите скорость, м/с: "))
            diameter_2 = float(input("Введите диаметр, мм: "))
            print("Расход равен ", calc_volume(velocity_2, diameter_2), "м3/ч")
        else:
            diameter_3 = float(input("Введите диаметр, мм: "))
            volume_3 = float(input("Введите расход, м3/ч: "))
            print("Скорость равна ", calc_velocity(volume_3, diameter_3),
                  "м/с")
