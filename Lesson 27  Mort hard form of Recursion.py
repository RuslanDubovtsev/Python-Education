box = [[[[[[[[]]]]]]], [[[[[[[[[[[[[[]]]]]]]]]]]]]], [[[[[[[[[[]]]]]]]]]], [[[[['key']]]]]]
box_1 = ['key']


def change_list(some_list):
    new_list = []
    for elem in some_list:
        if not isinstance(elem, list):
            new_list.append(elem)
        else:
            new_list.extend(change_list(elem))
    return new_list


def search_key(some_list_1, key):
    new_list = change_list(some_list_1)
    if key in new_list:
        return f'{key} in {some_list_1}'
    else:
        return f'{key} is not in {some_list_1}'


print(search_key(box, 'key'))