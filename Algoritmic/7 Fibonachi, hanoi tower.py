from functools import lru_cache
# html
# html = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
# def search_element(my_dict, element):
#     if element in my_dict:
#         return my_dict[element]
#     for key, value in my_dict.items():
#         if isinstance(value, dict):
#             # print(key, ":", value)
#             result = search_element(value, element)
#             if result:
#                 return result
#     return None
#
#
#
# print(search_element(html, 'h2'))


# Fibonachi
# my_list = []
# my_list.append(0)
# def number_Fibonachi(int1, int2):
#     if int2 > 17711:
#         print(my_list)
#         return 'stop'
#     res = int1 + int2
#     my_list.append(int2)
#     # my_list.append(res)
#     # print(int2, res)
#     result = number_Fibonachi(int2, res)
#
#     return result
# #
# print(number_Fibonachi(0, 1))
# Fibonachi2

# def Fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return Fib(n-1) + Fib(n-2)
#
# a = Fib(int(input("Введите позицию: ")))
# print(a)
# Hanoi_town

def hanoi(n, i, k):
    if n == 1:
        print(f'Move disk 1 from pin {i} to {k}')
    else:
        tmp = 6 - i - k
        hanoi(n-1, i, tmp)
        print(f"Move disk {n} from pin {i} to {k}")
        hanoi(n-1, tmp, k)

hanoi(3, 1, 2)