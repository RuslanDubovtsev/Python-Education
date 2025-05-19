from random import randint
# ________Д14_________
# /____1____\
# def food_supplu():
#     a = int(input())
#     b = int(input())
#     print("Всего", a + b, "шт.")
#
# print("Сколько мешков рыбы и мяса?")
# food_supplu()
# print("Сколько буханок белого и чёрного хлеба?")
# food_supplu()
# print("Сколько вёдер воды и молока?")
# food_supplu()

# /____2____\
import math
# def math_func(choose):
#     if choose == 1:
#         num = int(input("Число: "))
#         print(num ** 2)
#     elif choose == 2:
#         sin = int(input("Угол: "))
#         print(math.sin(sin))
#     elif choose == 3:
#         cos = int(input("Угол: "))
#         print(math.cos(cos))
#
# print("Выбор операции: 1 - квадратный корень, 2 - нахождение синуса, 3 - нахождение косинуса")
# math_func(int(input("Сделайте выбор 1, 2 или 3: ")))

# /____3____\
# def greetings(name, age, address):
#     print(f'{name}, {age}, {address}')
#
# greetings(input('Введите ваше имя: '), int(input("Введите ваш возраст: ")), input("Введите ваш адрес: "))

# /____4____\
# def aboutWater(price):
#     print("КлирВотер", "ВодЗавод", price)
#
# aboutWater(200)
# aboutWater(250)
# aboutWater(230)

# /____5____\
# def summa_n(n):
#     summ = 0
#     for i in range(1, n + 1):
#         summ += i
#         print(summ)
#
# summa_n(5)

# /____6____\
# def search_coin(x, y):
#     if x <= 1 or x <= -1: # if -1 <= x <= 1
#         if y <= 1 or y <= -1:
#             return "Монетка где-то рядом"
#         else:
#             return "Монетки в области нет"
#     else:
#         "Монетки в области нет"
#
# print(search_coin(float(input(": ")), float(input(": "))))


# ________Д16_________
# /____1____\
# quantity_numbers = int(input("Enter the quantity of numbers: "))
# my_list = []
# for i in range(1, quantity_numbers + 1):
#     temporay = int(input("Введите число: "))
#     my_list.append(temporay)
#
# for num in my_list:
#     print(num ** 2)

#  /____2____\
# numbers = [3,7,5]
#
# while True:
#     number = int(input('Новое число: '))
#     numbers.append(number)
#     print('Текущий список чисел:', numbers)
#     for i in numbers:
#         print(i ** 2, i ** 3, i ** 4)
#         print()

# /____3____\
# books = [12, 1, 23, -134, -15, 56, 123, 54, -18]
# shelf = []
# kept_by_readers = []
# for book in books:
#     if book < 0:
#         kept_by_readers.append(book)
#     elif book > 0:
#         shelf.append(book)
#
# print("ID книг на руках читателей: ", kept_by_readers)
# print("ID книг на полках: ", shelf)

# /____4____\
# circle = 5
# players = []
# quantity_of_players = int(input("Введите количество игроков: "))
# for _ in range(1, quantity_of_players + 1):
#     players.append(0)
# print("Изначальные очки: ", players)
# while circle != 0:
#     points_for_player = int(input("Игроку на какой позиции начислить очки: "))
#     quantity_of_points = int(input("Количество очков: "))
#     players[points_for_player] += quantity_of_points
#     print(players)
#     circle -= 1

# /____5____\

# original_string = input("Введите строку: ")
# position = int(input("Введите позицию символа, который нужно заменить: "))
# new_symbol = input("Введите новый символ: ")
# print(original_string[:position-1] + new_symbol + original_string[position:])

# /____6____\
# nums_list = []
# N = int(input('Кол-во чисел в списке: '))
#
# for _ in range(N):
#     num = int(input('Очередное число: '))
#     nums_list.append(num)
#
# maximum = 0
# minimum = 1
#
# for i in nums_list:
#     if maximum < i:
#         maximum = i
#     if i == -1:
#         maximum = i
#     if minimum > i:
#         minimum = i
#
# print('Максимальное число в списке:', maximum)
# print('Минимальное число в списке:', minimum)


# ________Д17_________
# /____1____\
# def tax(income, people):
#     tax_database = []
#     tax_database2 = {
#     }
#     if income < 1000:
#         the_tax = income * 5 / 100
#         tax_database.append(the_tax)
#         print("Налог:", tax_database)
#
#         for i in range(1, people):
#             tax_database2[i] = the_tax
#         print("Налог2:", tax_database2)
#
#     elif income > 1000:
#         the_tax = income * 15 / 100
#         tax_database.append(the_tax)
#         print("Налог:", tax_database)
#
#         for i in range(1, people):
#             tax_database2[i] = the_tax
#         print("Налог2:", tax_database2)
#
#     else:
#         the_tax = income * 50 / 100
#         tax_database.append(the_tax)
#         print("Налог:", tax_database)
#
#         for i in range(1, people):
#             tax_database2[i] = the_tax
#         print("Налог2:", tax_database2)
#
# print(tax(17500, 10))

# /____2____\
# def degree_of_importance_of_tasks(data):
#     print(data)
#     new_string = ""
#     new_string2 = ""
#     task_number = input("Введите первую задачу: ")
#     task_number2 = input("Введите вторую задачу: ")
#     keys = list(data.keys())
#     for elem in keys:
#         if elem == task_number:
#             new_string = elem
#         if elem == task_number2:
#             new_string2 = elem
#     if len(new_string2) < len(new_string):
#             print(new_string, "важнее", new_string2)
#     elif len(new_string2) > len(new_string):
#             print(new_string2, "важнее", new_string)
#     else:
#         print("Обнуляем результат")
#         print("Обнуляем результат")
#         print("Задачи равны")
#
# def data():
#     my_dict = {}
#     for _ in range(1, 10):
#         integers = [i for i in range(1, random.randint(2, 6))]
#         data = ''.join(str(num) for num in integers)
#         my_dict[data] = 'Какая-то информация'
#     return my_dict
#
# degree_of_importance_of_tasks(data())

# /____3____\
# def summa_n(number):
#     sum_number = 0
#     sum_number2 = 0
#     for num in range(1, number + 1):
#         sum_number += num
#     for num in range(1, sum_number + 1):
#         sum_number2 += num
#     print(f"Сумма от 1 до {number} = {sum_number}")
#     print(f"Сумма от 1 до {sum_number} = {sum_number2}")
#
# summa_n(int(input("Введиет число: ")))

# /____4____\
# def comparison_of_quantity(quantity_symbol):
#     first_list = []
#     second_list = []
#     for i in range(1, quantity_symbol + 1):
#         first_list.append(random.randint(1, 10))
#     print("first_list: ", first_list)
#     create_list = int(input("Создайте список: "))
#
#     for i in range(1, create_list + 1):
#         second_list.append(random.randint(1, 10))
#     print("second_list: ", second_list)
#
#     if len(first_list) > len(second_list):
#         print("first_list длинНее second_list")
#     elif len(first_list) < len(second_list):
#         print("second_list длиннее first_list")
#
# comparison_of_quantity(int(input("Создайте список: ")))

# /____5____\
# def numeral_count(quantity_tasks):
#     my_list = [[1], [3222], [644]]
#     buffer = ""
#     # for _ in range(1, quantity_tasks + 1):
#     #     numbers = int(input("Введите число: "))
#     #     my_list.append(numbers)
#     #     print(my_list)
#     for elem in my_list:
#         print(f"Буффер: {buffer}, длина буффера: {len(buffer)}\n"
#               f"Элемент: {str(elem)}, длина элемента: {len(str(elem))}\n"
#               f"_____________________________")
#         if len(buffer) < len(str(elem)):
#             buffer = str(elem)
#     return "Первая задача на обработку: ", buffer
#
# print(numeral_count(int(input("Введите кол-во задач: "))))


# ________Д17_________
# /____1____\
# arr = []
# for i in range(10):
#     arr.append(randint(1, 99))
# print(arr)

# arr = [7,4,10,5,2,1,6]
# N = len(arr)
# i = 0
# while i < N - 1:
#     m = i
#     j = i + 1
#     while j < N:
#         if arr[j] < arr[m]:
#             m = j
#         j += 1
#
#     arr[i], arr[m] = arr[m], arr[i]
#     print(arr[i], arr[m], arr[m], arr[i])
#     print(arr)
#
#     i += 1
#
# print(arr)

# def sorting_alg(arr):
#     N = len(arr)
#     for i in range(N-1):
#         m = i
#         for j in range(N):
#             if arr[m] > arr[j]:
#                 m = j
#         arr[i], arr[m] = arr[m], arr[i]
#     print(arr)
#
# print(sorting_alg([7,4,10,5,2,1,6]))

# ________Д19_________
# /____1____\
# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
# a = zoo.index('lion')
# zoo.insert(a + 1, 'bear')
# print(zoo)
# zoo.remove('elephant')
# print("Лев сидит под номером", zoo.index('lion'))

# /____3____\
# quantity = int(input("Количество участников: "))
# quantity2 = int(input("Количество человек в команде: "))
# my_list = []
# n = 1
# for i in range(quantity // quantity2):
#     my_list.append([i for i in range(n, quantity2 + n)])
#     n += quantity2
# print(my_list)

# /____4____\
