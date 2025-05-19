import math

# x**2-5x+4=0
# 4x**2+5x-6=0
# equation = 'x**2-7x+1=0'
# equation = list(equation)
# print(equation)
#
# if "-" in [i for i in equation[3:]]:
#     print(True)
# else:
#     print(False)
#
#

def quadratic_equation():
    equation = input("Введите квадратное уравнение без пробелов: ")
    equation = list(equation)
    print(equation)
    minus_index = equation[1:].index('-') + 1 if '-' in equation else 100 # Для защиты от нахождения минуса вначале мы
    # заранее пропускаем его предполагаемое место и добавляем недостающую единицу
    plus_index = equation.index('+') if '+' in equation else 100
    min_value = min(minus_index, plus_index)

    print(min_value, minus_index, plus_index)


    if equation[0] != "-" and equation[0] != "x":
        a = int(equation[0])

        if min_value == minus_index:
            i = minus_index + 1
            some_digit_number = ''

            while equation[i].isdigit():
                some_digit_number += equation[i]
                i += 1
            b = - int(some_digit_number)
            print(b)
        else:
            i = plus_index + 1
            some_digit_number = ''
            while equation[i].isdigit():
                some_digit_number += equation[i]
                i += 1
            b = int(some_digit_number)
            print(b)

        if '-' in equation[min_value + 1:]:
            quantity = len(equation[:min_value]) + 1
            i = equation[min_value + 1:].index('-') + quantity + 1
            some_digit_number = ''
            while equation[i].isdigit():
                some_digit_number += equation[i]
                i += 1
            c = - int(some_digit_number)
            print(c)
        else:
            quantity = len(equation[:min_value]) + 1
            i = equation[min_value + 1:].index('+') + quantity + 1
            some_digit_number = ''
            while equation[i].isdigit():
                some_digit_number += equation[i]
                i += 1
            c = int(some_digit_number)
            print(c)

    elif equation[0] == "-" and equation[1] != "x":
        a = - int(equation[1])

        if min_value == minus_index:
            i = minus_index + 1
            some_digit_number = ''

            while equation[i].isdigit():
                some_digit_number += equation[i]
                i += 1
            b = - int(some_digit_number)
            print(b)
        else:
            i = plus_index + 1
            some_digit_number = ''
            while equation[i].isdigit():
                some_digit_number += equation[i]
                i += 1
            b = int(some_digit_number)
            print(b)

        if '-' in equation[min_value + 1:]:
            quantity = len(equation[:min_value]) + 1
            i = equation[min_value + 1:].index('-') + quantity + 1
            some_digit_number = ''
            while equation[i].isdigit():
                some_digit_number += equation[i]
                i += 1
            c = - int(some_digit_number)
            print(c)
        else:
            quantity = len(equation[:min_value]) + 1
            i = equation[min_value + 1:].index('+') + quantity + 1
            some_digit_number = ''
            while equation[i].isdigit():
                some_digit_number += equation[i]
                i += 1
            c = int(some_digit_number)
            print(c)

    elif equation[0] != "-" and equation[0] == "x":
        a = 1

        if min_value == minus_index:
            i = minus_index + 1
            some_digit_number = ''
            print(equation[i])
            while equation[i].isdigit():
                print(i)
                print(equation[i])
                some_digit_number += equation[i]
                i += 1
            b = - int(some_digit_number)
            print(b)
        else:
            i = plus_index + 1
            some_digit_number = ''
            while equation[i].isdigit():
                some_digit_number += equation[i]
                i += 1
            b = int(some_digit_number)
            print(b)

        if '-' in equation[min_value + 1:]:
            quantity = len(equation[:min_value]) + 1
            i = equation[min_value + 1:].index('-') + quantity + 1
            some_digit_number = ''
            while equation[i].isdigit():
                some_digit_number += equation[i]
                i += 1
            c = - int(some_digit_number)
            print(c)
        else:
            quantity = len(equation[:min_value]) + 1
            i = equation[min_value + 1:].index('+') + quantity + 1
            some_digit_number = ''
            while equation[i].isdigit():
                some_digit_number += equation[i]
                i += 1
            c = int(some_digit_number)
            print(c)

    elif equation[0] == "-" and equation[1] == "x":
        a = - 1

        if min_value == minus_index:
            i = minus_index + 1
            some_digit_number = ''

            while equation[i].isdigit():
                some_digit_number += equation[i]
                i += 1
            b = - int(some_digit_number)
            print(b)
        else:
            i = plus_index + 1
            some_digit_number = ''
            while equation[i].isdigit():
                some_digit_number += equation[i]
                i += 1
            b = int(some_digit_number)
            print(b)

        if '-' in equation[min_value + 1:]:
            quantity = len(equation[:min_value]) + 1
            i = equation[min_value + 1:].index('-') + quantity + 1
            some_digit_number = ''
            while equation[i].isdigit():
                some_digit_number += equation[i]
                i += 1
            c = - int(some_digit_number)
            print(c)
        else:
            quantity = len(equation[:min_value]) + 1
            i = equation[min_value + 1:].index('+') + quantity + 1
            some_digit_number = ''
            while equation[i].isdigit():
                some_digit_number += equation[i]
                i += 1
            c = int(some_digit_number)
            print(c)

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

def logarithm(a, b):
    for i in range(1, b):
        # print(i)
        if a ** i == b:
            print(f"Done: log{a} {b} = {i}")
            break
        print(f"log{a} {b} = {i}")
    print("Wrong logarithm")

logarithm(6, 238)




# equation = 'x**2-7x+12=0'
# equation = list(equation)
# print(equation)

# if equation[0] != "-" and equation[0] == "x":
#     a = 1
#
#     minus_index = equation.index('-') if '-' in equation else 100  # Для того чтобы отсутствующий символ не вызывал
#     # ошибок от метода index и не мешал существующему символу, который точно будет иметь более маленький индекс
#     plus_index = equation.index('+') if '+' in equation else 100
#     min_value = min(minus_index, plus_index) # В min_value гарантировано попадет индекс существующего символа благодаря
#     # слишком большого значения несуществующего символа
#     print(min_value, minus_index, plus_index)
#     if min_value == minus_index:
#         i = minus_index + 1
#         some_digit_number = ''
#
#         while equation[i].isdigit():
#             some_digit_number += equation[i]
#             i += 1
#         b = - int(some_digit_number)
#         print(b)
#     else:
#         i = plus_index + 1
#         some_digit_number = ''
#         while equation[i].isdigit():
#             some_digit_number += equation[i]
#             i += 1
#         b = int(some_digit_number)
#         print(b)
#         #  +1 потому что он начинает с предыдущего плюса и выдает его индекс как 0
#     if '-' in equation[min_value + 1:]: # Выставлен +1 т.к он сразу находил минус, ведь срез начинался именно с минуса
#         quantity = len(equation[:min_value]) + 1
#         i = equation[min_value + 1:].index('-') + quantity + 1 # Находим символ плюса во второй части уравнения, отрезая от
#         # нее первую, так как индекс находит плюс только в первой части. Прибавляем к урезанному уравнению количество
#         # символов прошлой части, ведь индекс возвращается исходя из урезанного, а не полного уравнения. Добавляем еще
#         # единичку для того, чтобы цикл начался с цифры, иначе он не запустится
#         # print("Индекс: ", i, "Значение: ", equation[i])
#         some_digit_number = ''
#         while equation[i].isdigit():
#             some_digit_number += equation[i]
#             i += 1
#         c = - int(some_digit_number)
#         print(c)
#     else:
#         quantity = len(equation[:min_value]) + 1
#         i = equation[min_value + 1:].index('+') + quantity + 1
#         some_digit_number = ''
#         while equation[i].isdigit():
#             some_digit_number += equation[i]
#             i += 1
#         c = int(some_digit_number)
#         print(c)

