def work_with_the_integer():
    calculation_options = int(input('''Выберите функцию числом: 1 - сложение 2 - вычитание, 3 - умножение, 4 - деление,"
 5 - возведение в квадрат, 6 - возведение в куб: '''))

    if calculation_options == 1:
        number_one = int(input("Первое число: "))
        number_two = int(input("Второе число: "))
        print("Ответ", number_one + number_two)

    elif calculation_options == 2:
        number_one = int(input("Первое число: "))
        number_two = int(input("Второе число: "))
        print("Ответ", number_one - number_two)

    elif calculation_options == 3:
        number_one = int(input("Первое число: "))
        number_two = int(input("Второе число: "))
        print("Ответ", number_one * number_two)

    elif calculation_options == 4:
        number_one = int(input("Первое число: "))
        number_two = int(input("Второе число: "))
        print("Ответ", number_one / number_two)

    elif calculation_options == 5:
        number_one = int(input("Число, которое вы хотите возвести в квадрат: "))
        print("Ответ", number_one ** 2)

    elif calculation_options == 6:
        number_one = int(input("Число, которое вы хотите возвести в куб: "))
        print("Ответ", number_one ** 3)


def work_with_the_strings():
    string = input("Введите вашу строку: ")
    function_options = int(input('''Выберите функцию для вашего текста числом:
     1 - Вычислить количество символов в вашей строке, 
     2 - Нахождение определенного символа в вашей строке,  
     3 - замена вашего символа в строке на новый желанный символ: '''))

    if function_options == 1:
        print("Количество символов в вашей строке - ", len(string), "символов")

    elif function_options == 2:
        find_the_symbol = input("Какой именно символ вы хотите найти?: ")
        print(f"Символ '{find_the_symbol}' находится в позиции {string.find(find_the_symbol)}")

    elif function_options == 3:
        place_symbol = input("Назовите символ, который вы хотите заменить: ")
        replace_the_symbol = input("Назовите желанный вам символ, который вы хотите вставить на замену: ")

        new_string = string.replace(place_symbol, replace_the_symbol)
        print(new_string)


def work_with_the_list():
    the_list = list(input("Введите ваш список: ").split(' '))
    function_options = int(input('''Выберите функцию для вашего списка числом:
     1 - Вычислить количество символов в вашем списке, 
     2 - Удаление определенного элемента в списке,  
     3 - Сортировка списка
     4 - Добавление чего-либо в список: '''))

    count = 0

    if function_options == 1:
        for elem in the_list:
            for elem2 in elem:
                len(elem2)
                count += 1
        print(count)

    elif function_options == 2:
        print(the_list)

        remove_element = int(input("Какой элемент вы хотите удалить?: "))
        new_list = the_list.pop(remove_element)

        print(new_list)


work_with_the_list()