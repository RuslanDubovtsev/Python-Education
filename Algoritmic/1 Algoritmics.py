import time
import random

def time1(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f'Функция {func} стартовала в {start}')
        res = func(*args, **kwargs)
        print(f'Функция {func} отработал за время {time.time() - start}')
        return res
    return wrapper


# @time1
def func_make_array():
    my_list = []
    for elem in range(100):
        num = random.randint(1, 100)
        my_list.append(num)
        # my_list = sorted(my_list)
    # print(my_list)
    return my_list

# res = func_make_array()

# @time1
# def line_search(find_element, my_list):
#     # my_list = list()
#     # for _ in range(1000):
#     #     number = random.randint(1, 100)
#     #     my_list.append(number)
#     for elem in my_list:
#         if elem == find_element:
#             return my_list.index(elem)
#     return False
#
# find = line_search(2, res)
# print(find)

# def max_num():
#     my_list = []
#     new_list = []
#     for _ in range(100):
#         number = random.randint(1, 100)
#         my_list.append(number)
#     for elem in my_list:
#         if elem % 2 == 0:
#             new_list.append(elem)
#
#     return new_list
# # O(2n)
# func = max_num()
# print(func)


# def combinations():
#     my_list = [1, 7, 8, 12, 2, 5, 5]
#     number = 3
#     element1 = []
#     element2 = []
#     reserve = []
#     for elem in my_list:
#         # print(elem)
#         for elem2 in my_list:
#             if elem + elem2 == number:
#                 element1.append(elem)
#                 element1.append(elem2)
#                 return element1
# a = combinations()
# print(a)


# a = "kasiwoeqjl;saKEHFUIAHEMASLKFLUHQoksoi;jrp2 kdiobdscFKOP"
# my_dict = {}
# new_dict = {}
# for elem in a:
#     my_dict[elem] = my_dict.get(elem, 0) + 1
#     if my_dict.get(elem) >= 2:
#         new_dict[elem] = my_dict[elem]
#
# print(my_dict)
# print(new_dict)

# @time1
# def search_number(number, mylist):
#     print(mylist)
#     for elem in mylist:
#         if number == elem:
#             return "Число найдено:", mylist.index(elem)
#     return False
#
#
# search = search_number(5, res)
# print(search)



# def binary_search(list, number):
#     min_num = 0
#     max_num = len(list) - 1
#
#     while min_num <= max_num:
#         mid = (min_num + max_num) // 2
#         print(mid)
#         mid_value = list[mid]
#
#         if mid_value == number:
#             return mid_value
#         elif mid_value < number:
#             min_num = mid
#         else:
#             max_num = mid
#
#     return -1  # Элемент не найден

# Пример использования
# my_list = []
# for elem in range(100):
#     num = random.randint(1, 100)
#     my_list.append(num)
# print(sorted(my_list))

# result = binary_search(my_list, 7)
# print(result)

# def Google(some_list, num):
#     new_list = []
#     for i in range(len(some_list)):
#         for j in range(i + 1, len(some_list)):
#             res = some_list[i] + some_list[j]
#             if res == num:
#                 new_list.append(some_list[i])
#                 new_list.append(some_list[j])
#     print(new_list)
#
#
# Google([1, 2, 3, 6], number)


# def New_Solution(some_list, number):
#     my_set = set()
#     new_list = []
#     for i in range(len(some_list)):
#         res = number - some_list[i]
#         print(my_set)
#         if res in my_set:
#             new_list.append(res)
#             new_list.append(some_list[i])
#         my_set.add(some_list[i])
# number = int(input(": "))
# New_Solution([1, 2, 3, 6], number)

# def func_make_array():
#     my_list = []
#     for elem in range(100):
#         num = random.randint(1, 100)
#         my_list.append(num)
#         # my_list = sorted(my_list)
#     # print(my_list)
#     return my_list
#
def max_num(my_list):
    count = 0
    new_list = []
    max = 0
    while count < len(my_list):
        print(my_list[count])
        if max < my_list[count]:
            max = my_list[count]
        count += 1
    print('Максимум:', max)




max_num(func_make_array())

