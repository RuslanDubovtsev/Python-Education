def div_num(number):
    res = 10 / number
    return f'{10}/{number} = {res}'

result = div_num(11)

file = open("math.txt", 'a')
file.write(result)
file.write('\n')
file.close()

# file_1 = open("math.txt", 'r')
# data = file_1.read()
# print(data)
# file_1.close()


#
# my_string = 'Алина дай списать контрольную'
#
# buffer_list = []
#
# for elem in my_string:
#     buffer_list.append(ord(elem) + 200)
#
#
# new_string = ''
#
# for elem in buffer_list:
#     new_string += chr(elem)
#
# print(new_string)
#
# buffer_list_1 = []
#
# for elem in new_string:
#     buffer_list_1.append(ord(elem) - 200)
#
# alina_string = ''
#
# for elem in buffer_list_1:
#     alina_string += chr(elem)
#
# print(alina_string)

#
# def enter_in_debt_list(file):
#     number_of_user = int(input("Сколько человек вы знакосите в список: "))
#     text = open(file, 'a')
#     for _ in range(number_of_user):
#         user_info = input('Введите фамилия, имя и сумму задолженности через пробел: ')
#         text.write(user_info)
#         text.write('\n')
#     text.close()
#
#
# enter_in_debt_list('bank_file.txt')
#
#
# def sum_of_debt(file):
#     sum_debt = 0
#     text = open(file, 'r')
#     for elem in text:
#         data = elem.split()
#         sum_debt += int(data[2])
#     return sum_debt
#
#
# print(sum_of_debt('bank_file.txt'))