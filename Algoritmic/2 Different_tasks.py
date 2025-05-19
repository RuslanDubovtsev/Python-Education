# func = lambda x, y: x **y
# print(func(2,3))

# my_list = [1, 2, 3, 4, 5]
# new_list = []

# for elem in my_list:
#     elem += 10
#     new_list.append(elem)
# print(new_list)

generator1 = map(lambda x: x + 10, my_list)
print(list(generator1))
# def summ(number):
#     return number + 10
# generator = map(summ, my_list)

# my_list = [1,2,3,4,5,6,7,8,9,10]
# sorted_list = [x for x in my_list if x % 2 == 0]
# print(sorted_list)
# sorted_list = filter(lambda x: x % 2 == 0, my_list)
# print(list(sorted_list))

# ______________________________
# f = lambda x, y, z: x + y + z
# print(f(2,3,10))

# my_list = [1,2,3,4,5,6,7,8]
# generator = map(lambda x: x + 4, my_list)
# print(list(generator))

# my_list1 = [1,2,3,4]
# my_list2 = [5,6,7,8]
# def summ(number1, number2):
#     return number1 + number2
#
# sum = map(summ, my_list1, my_list2)
# print(list(sum))

# my_list = [3,4,5,-8,6,-9,5,-1,-78,7,6]
# filter = filter(lambda x: x > 0, my_list)
# print(list(filter)


# def dicts(my_dict):
#     print("Добавить ключ;")
#     print("Изменить ключ;")
#     print("Найти ключ;")
#     what_the_doing = input('Что выбрать? ')
#     if what_the_doing == 'Добавить ключ' or what_the_doing == "1" or what_the_doing == "добавить ключ":
#         new_dict = input("Введите ваш ключ: ")
#         new_value = input("Введите значение: ")
#         the_dict2 = dict()
#         the_dict2[new_dict] = new_value
#         my_dict.update(the_dict2)
#         print(my_dict)
#     elif what_the_doing == "Изменить ключ" or what_the_doing == "2" or what_the_doing == "изменить ключ":
#         what_key_change = input("Какой ключ вы хотите заменить?: ")
#         try:
#             my_dict.pop(what_key_change)
#             print(my_dict)
#         except KeyError as error:
#             print(error)
#         add_new_key = input("Назовите новый ключ: ")
#         my_dict[add_new_key] = value
#         print(the_dict)
#         print(my_dict)
#
#
# dicts({"Пирог": "яблочный"})


# 1
# def task1():
#     my_string = input().split(' ')
#     my_list = []
#     longer_word = 0
#     for st in my_string:
#         length = len(st)
#         my_list.append(length)
#         if length > longer_word:
#             longer_word = length
#     return "Самое длинное слово, букв:", longer_word
# a = task1()
# print(a)

# def task2():
#     stoil = input()
#     number = 0
#     summ = 0
#     for elem in stoil:
#         if elem == 'b':
#             number += 2
#             summ += number
#     return summ

# b = task2()
# print(b)'


# def task3():
#     false = False
#     guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
#     while True:
#         print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
#         leave_or_come = input("Гость ушел или пришел?: ")
#         if len(guests) < 6:
#             if leave_or_come == "пришел":
#                 what_name = input("Имя гостя: ")
#                 # if len(guests) < 6:
#                 guests.append(what_name)
#                 print("Привет, ", what_name, "!")
#
#             elif leave_or_come == "ушел":
#                 what_name2 = input("Имя гостя: ")
#                 guests.remove(what_name2)
#                 print("Пока, ", what_name2, "!")
#         elif len(guests)
#
# d = task3()
# print(d)


# def task6():
#     first_list = [1, 2, 3]
#     second_list = [1, 2, 3, 4, 3, 2, 6]
#     first_list.extend(second_list)
#     # first_list = set(first_list)
#     # print(first_list)
#     new_list = []
#     for elem in first_list:
#         while first_list.count(elem) > 1:
#             first_list.remove(elem)
#     print(first_list)
#
#
# e = task6()
# print(e)


# def one_upper_word(list):
#     for elem in list:
#         if elem.isupper():
#             return True
#     return False
#
# def three_numbers(list):
#     count = 0
#     for elem in list:
#         if elem.isdigit() == True:
#             count += 1
#     if count >= 3:
#         return True
#
# # a = three_numbers(my_list)
# # print(a)
# while True:
#     password = input("Введите пароль: ")
#     my_list = list(password)
#     if len(my_list) >= 8:
#         pass
#     else:
#         print("Мало символов. Попробуйте еще раз")
#         continue
#     if one_upper_word(my_list) == True:
#         pass
#     else:
#         print("Нужна как минимум одна заглавная буква. Попробуйте еще раз")
#         continue
#     if three_numbers(my_list) == True:
#         pass
#     else:
#         print("Нужны как минимум 3 цифры. Попробуйте еще раз")
#         continue
#     print("Это надежный пароль!")
#     break


# my_list = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
# new_list = []
# for elem in my_list:
#     a = my_list.index(elem) + 1
#     if a % 2 == 0:
#          new_list.append(my_list.index(elem) + 1)
# print(new_list)


# the_word = input("Введите слово: ")
# if the_word[::-1] == the_word:
#     print("Это палиндром")
# else:
#     print("Это не палиндром")


# a = [10, 3, 5, 1, 0, 9, 6, 7, 3, 1, 2]
#
# for i in range(len(a) - 1, 0, -1):
#     for j in range(i):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print(a)

# import subprocess
# file = subprocess.run(['python', 'pythonProject1'])

# Перевод в двоичный код
# number = int(input("Введите число: "))
# result = ""
# while number > 0.9:
#     if number % 2 == 0:
#         result += str(0)
#     elif number % 2 != 0:
#         result += str(1)
#     number //= 2
#     # print(number)
#
# print("Число в двоичной системе счисления:", result[::-1])
#
#
# print("Число в восьмеричной системе счисления:", result[::-1])
number = input("Двоичное число: ")
result = 0
count = len(number) - 1
# print(count)
for i in number:
    # print(count)
    result += int(i) * 2**count
    count -= 1
print(result)