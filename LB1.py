from math import pi


def circle_area(r):
    if r < 0:
        raise ValueError("Значение радиуса должно быть > 0")
    if type(r) not in (float, int):
        raise TypeError("Тип данных должен быть int или float!")
    return pi*r**2


if __name__ == "__main__":
    r_list = [2, 0, -14, True, [24], 'string']
    for i in r_list:
        res = circle_area(i)
        print(f"Исходные данные: {i} Результат: {res}")
