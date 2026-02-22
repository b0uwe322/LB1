from math import pi

def circle_area(r):
    return pi*r**2



if __name__ == "__main__":
    r_list = [2, 0, -14, True, [24], 'ergeg']
    for i in r_list:
        res = circle_area(i)
        print(f"Исходные данные: {i} Результат: {res}")