# 1)
# def fact(number):
#     if number == 1:
#         return 1
#     else:
#         print(f"Вызов fact({number - 1}) начинается и добавляется в стек")
#         result = number * fact(number - 1)
#         print(f"Вызов fact({number - 1}) завершился и удаляется из стека")
#         return result
# print(f"Вызов fact(5) начинается и добавляется в стек")
# result = fact(5)
# print(f"Вызов fact(5) завершился и удаляется из стека")
# print("Итог - ", result)

# 2)
# def power(a, n):
#     if n == 0:
#         return 1
#     else:
#         print(f"Вызов power({a, n-1}) начинается и добавляется в стек")
#         result = a * power(a, n-1)
#         print(f"Вызов power({a, n - 1}) завершился и удаляется из стека")
#         return result
#
#
# float_num = float(input('Введите вещественное число: '))
# int_num = int(input('Введите степень числа: '))
#
# print(f"Вызов power {float_num, int_num} начинается и добавляется в стек")
# result = float_num, '**', int_num, '=', power(float_num, int_num)
# print(f"Вызов fact {float_num, int_num} завершился и удаляется из стека")
# print(result)

# 3)
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}
#
def rec_dict(sequence, tag):
    if tag in sequence:
        return sequence[tag]
    for key, value in sequence.items():
        if isinstance(value, dict):
            print(key, ":", value)
            result = rec_dict(value, tag)
            if result:
                return result
    return None


print(rec_dict(site, 'div'))

# list = []
# def output_num(num):
#     if num == 1:
#         list.append(num)
#         return list
#     else:
#         list.append(num)
#         # print(list)
#         # print(num)
#         return output_num(num - 1)
#
# number = int(input(": "))
# res = output_num(number)
#
# l = len(res)-1
#
# for x in range(l, -1, -1):
#     print(res[x])