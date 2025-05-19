# try:
#     name = input("Your name: ")
#     age = int(input("Your age: "))
#     email = input("Your email")
#     print(name, age, email)
# except ValueError as error:
#     print("Неверно введенные данные (У тебя не получится сломать сайт ;)")
#
# print("Даже не пытайся.")
#

# try:
#     my_file = open("not_exists", "r")
#     data = my_file.read()
# except FileNotFoundError:
#     print("Чел, такого файла не существует. Соберись.")
# print('')
# print("Ну и что? Я продолжу работать, подумаешь ошибка")


# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Иди учить математику! Неуч, на ноль делить нельзя!")

# while True:
#     try:
#         name = input("Your name: ")
#         age = int(input("Your age: "))
#         email = input("Your email: ")
#
#     except ValueError as error:
#         print("Неверно введенные данные (У тебя не получится сломать сайт ;)")
#
#     else:
#         print(name, age, email)
#         break

# _______ДЗ_______
# try:
#     number = int(input("Введите число: "))
#     number2 = int(input("Введите второе число: "))
#     print(number / number2)
# except ValueError:
#     print("Посиди и подумай, в чем ошибка")
# except ZeroDivisionError:
#     print("Посиди и подумай, в чем ошибка")

# try:
#     name = input("Твое имя: ")
#     password = int(input("Пароль: "))
#     gmail = input("Электронный адрес: ")
#     print(name, password, gmail)
# except ValueError:s
#     print("Перечитай код. Пременная пассворд ждет от тебя числа, а не другие значения")


# my_list = []
# try:
#     with open("file", "w") as file:
#         file.write("Python > Java, JavaScript and C++")
#     file2 = open("file", "r")
#     my_file = file2.read()
#     for element in my_file:
#         my_list.append(element)
#     print((''.join(my_list)))
# except FileNotFoundError:
#     print("Тупое ты существо, ты хочешь что-то сделать с несуществующим файлом")

try:
    my_dict = dict()
    print(my_dict['aaaa'])
except KeyError:
    print("Возможно, в вашем словаре нет ключа")




def binary_search_number(number, my_list):
    new_list = sorted(my_list)
    print(new_list)
    max_num = len(new_list)
    min_num = 0

    while min_num <= max_num:
        average = (max_num + min_num) // 2
        mid = new_list[average]
        if average == number:
            return "Число найдено:", new_list.index(average)
        elif mid < number:
            min_num = average
        else:
            max_num = average

    return False


binary_search = binary_search_number(90, res)
print(binary_search)
