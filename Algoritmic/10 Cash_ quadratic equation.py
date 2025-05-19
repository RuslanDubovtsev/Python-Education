import requests
import math

# def support(a, b, c):
#     a =
def quadratic_equation():
    equation = input("Введите квадратное уравнение без пробелов: ")
    equation = list(equation)
    print(equation)
    # x**2-7x+12=0
    # 4x**2щзз+50000x-6=0
    if equation[0] != "-" and equation[0] != "x":
        a = int(equation[0])
        if equation[5] == "-":
            i = 6
            some_digit_number = ''
            while equation[i].isdigit():
                some_digit_number += equation[i]
                i += 1
            b = - int(some_digit_number)
        else:
            i = 6
            some_digit_number = ''
            while equation[i].isdigit():
                some_digit_number += equation[i]
                i += 1
            b = int(some_digit_number)
        if equation[8] == "-":
            c = - int(equation[9])
        else:
            c = int(equation[9])

    D = b**2 - 4*a*c
    print(a, b, c)
    print(D)
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return x1, x2
    elif D == 0:
        x = -b / 2*a
        return x
    elif D < 0:
        return "Решения нет"

# print(quadratic_equation())

name_site = input("Начать?: ")
URLS_DICT = {}
print(URLS_DICT)
while name_site != 'стоп':

    def URL(url):
        res = requests.get(url)
        print(res.text)

    def cash(name):

        if name in URLS_DICT:
            return URL(URLS_DICT[name])
        else:
            value = input("Введите адрес: ")
            URLS_DICT[name] = value
            return URL(URLS_DICT[name])

    name_site = input("Введите имя сайта: ").lower()

    cash(name_site)



# https://www.google.com/
# https://yandex.kz/
# https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html