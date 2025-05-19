a = [1,2,3,[[[4]]]]
def search_recursion(my_list, element):
    for elem in my_list:
        print(elem)
        if elem == element:
            return True
        if isinstance(elem, list):
            return search_recursion(elem, element)
    return False
print(search_recursion(a, 4))