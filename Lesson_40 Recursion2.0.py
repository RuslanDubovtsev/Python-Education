# def test():
#     password = int(input('Введите пароль: '))
#     if password == 1321:
#         return password
#     else:
#         print('Неверный пароль!')
#     test()
#
# test()

#
# num = int(input('Enter number: '))
# fact = 1
# for x in range(1, num + 1):
#     print(x)
#     fact *= x
# print(fact)


# def sum_list(seq):
#     if seq == []:
#         return 0
#     print(seq[1:])
#     return seq[0] + sum_list(seq[1:])
#
# sum_list([1,2,3,4,5])


# Решение циклом
# def factorial(number):
#     fact = 1
#     for elem in range(1, number + 1):
#         fact *= elem
#     return fact
#
# print(factorial(3))

# Решение рекурсией
# def factorial(number):
#     if number == 1:
#         return 1
#     else:
#         return number * factorial(number - 1)
#
# print(factorial(3))

# def box(seq):
#     for elem in seq:
#         print(seq)
#         if not isinstance(elem, list):
#             if elem == "ключ":
#                 return "Ключ найден"
#         else:
#             return box(elem)
#
# print(box([[['ключ']  ], [], [[[]]]]))


# def foo(x):
#     if x <= 0:
#         return 0
#     else:
#         new_result = foo(x-1)
#         result = x + new_result
#         return result
# res = foo(5)
# print(res)


# def foo(x):
#     if x <= 0:
#         return 0
#     else:
#         new_result = foo( x-1)
#         result = x+new_result
#         return result
# print(foo(2))

# def foo_sum(num):
#     if num == 1:
#         return 1
#     else:
#         result = num + foo_sum(num - 1)
#         return result
#
# print(foo_sum(5))