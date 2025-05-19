def town_of_countries():
    my_dict = {}
    for i in range(0, 4):
        country = input("Страна: ")
        town = input("Город: ")
        my_dict[town] = country
    print(my_dict)

town_of_countries()


def search_value(elem, my_dict):
    for key, value in my_dict.items():
        if key == elem:
            return "Значение:", my_dict[key]
        elif isinstance(value, dict):
            res = search_value(elem, value)
            return res

a = {'html': {'head': {'link': 'text.css',
                       'body':
                    {'div': 'Это блок',
                     'h1': 'Here one text',
                     'p':{
                    'h2':'Here other text'}}}}}
print(search_value(input(": "), a))


def queue(my_list):
    print(my_list)
    my_list = my_list[::-1]
    for i in range(1, len(my_list) + 1):
        a = my_list.pop()
        print(a)
    print(my_list)

queue([i for i in range(1,10)])