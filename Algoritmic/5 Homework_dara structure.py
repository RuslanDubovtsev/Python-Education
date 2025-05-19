from collections import deque
import random
# chose = int(input("Какой вариант очереди, последний пришел-первый вышел или последний пришел-последний вышел?: "))
# a = []
# if chose == 2:
#
#     a.append('first')
#     print(a)
#     a.append('second')
#     print(a)
#     a.append('third')
#     print(a)
#     print(a.pop())
# elif chose == 1:
#     a = deque()
#     a.appendleft('first')
#     print(a)
#     a.appendleft('second')
#     print(a)
#     a.appendleft('third')
#     print(a)
#     print(a.popleft())
#
# print(a)

#
# def func_make_array():
#     my_list = []
#     for elem in range(100):
#         num = random.randint(1, 100)
#         my_list.append(num)
#     return my_list
#
# def sort_func(numbers):
#     numbers = set(numbers)
#     return numbers
#
# def sealing(new_list):
#     new_list = tuple(new_list)
#     return new_list
#
# a = func_make_array()
# print(a)
# b = sort_func(a)
# print(b)
# print(sealing(b))

a = deque()
a.appendleft('first')
print(a)
a.appendleft('second')
