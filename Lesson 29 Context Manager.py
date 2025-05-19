# with open('with_file.txt', 'a') as my_file:
#     for _ in range(5):
#         my_file.write('      4   ')
#         my_file.write('\n')
#         my_file.write('    2  ')
#         my_file.write('\n')
#
#
#
# def search_sum_file(file):
#     summ = 0
#     with open(file, 'r') as sum_file:
#         for elem in sum_file:
#             for elem1 in elem:
#                 if elem1.isdigit():
#                     summ += int(elem1)
#
#
#     return summ
#
#
#
# print(search_sum_file('with_file.txt'))

#
# ______ДЗ______
# def write_file():
#     with open('test', 'w') as file:
#         new_file = input("Пишите: ")
#         file.write(new_file)
#         file.write("\v")
#
#
# def read_file():
#     with open('test', 'r') as text:
#         print(text.read())
#
#
#
# def main_file():
#     question = input("Что вы хотите сделать?: ")
#     if question == "Запись":
#         write_file()
#     elif question == "Чтение":
#         read_file()
#     elif question != "Запись" or "Чтение":
#         return
#     return main_file( )
#
#
# main_file()

# test = 0
# my_dict = {
#         "Проном": '23',
#         "Фпараяв": '21',
#         "Дамбаков": '24'
# }
#
# list_dict = list(my_dict.items())
#
# print(list_dict)
# print('('.join(list_dict))
# with open("data", 'a') as text:
#         text.write(list_dict)
#         text.write('\n')
# for _ in my_dict:









