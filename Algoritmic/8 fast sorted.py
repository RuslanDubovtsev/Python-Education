import random


# def sum(array):
#     if len(array) < 1:
#         return 0
#     print(array[0])
#     return array[0] + sum(array[1:])
# print(sum([1,2,3,4,5]))
#

def quik(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[len(array) // 2]
        less = [i for i in array if i < pivot]
        greatest = [i for i in array if i > pivot]
        # a = less + [pivot] + greatest
        # print("Не рекурсия", a)
        print("Рекурсия less", less)
        print("Рекурсия pivot", pivot)
        print("Рекурсия greatest", greatest)
        return quik(less) + [pivot] + quik(greatest)

print(quik([1,10,5,-7,80,94,2]))

# def quik_sort(array):
#     if len(array) < 2:
#         return array
#
#     mid = array[random.randint(0, len(array) -1)]
#     print("length:", len(array))
#     less = [i for i in array if i < mid]
#     bigger = [i for i in array if i > mid]
#     print("Рекурсия less", less)
#     print("Рекурсия pivot", mid)
#     print("Рекурсия greatest", bigger)
#     return quik_sort(less) + [mid] + quik_sort(bigger)
#
# random_array = [random.randint(1, 99) for i in range(10)]
# print(quik_sort(random_array))
#
# def quik_sort(my_list):
#     if len(my_list) < 2:
#         return my_list
#
#     middle = my_list[len(my_list) // 2]
#     small = [i for i in my_list if i < middle]
#     big = [i for i in my_list if i > middle]
#     return quik_sort(small) + [middle] + quik_sort(big)
#
# a = [random.randint(1,100) for i in range(10)]
# print(a)
# print(quik_sort(a))

def usual_sort(array):
    quantity = len(array)
    i = 0
    while i < quantity - 1:
        m = i
        j = i + 1
        while j < quantity:
            if array[m] > array[j]:
                m = j
            j += 1
        array[i], array[m] = array[m], array[i]

        i += 1
    return array
print([7,4,10,5,2,1,6])
print(usual_sort([7,4,10,5,2,1,6]))
#
# arr = [7,4,10,5,2,1,6]
# N = len(arr)
# i = 0
# while i < N - 1:
#     m = i
#     j = i + 1
#     while j < N:
#         if arr[j] < arr[m]:
#             m = j
#         j += 1
#
#     arr[i], arr[m] = arr[m], arr[i]
#     print(arr[i], arr[m], arr[m], arr[i])
#     print(arr)
#
#     i += 1
#