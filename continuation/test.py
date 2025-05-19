# n = [1,4,5]
# h = [4,3,1]
# a = map(lambda x, y: x * y, n, h)
# print(list(a))

# x = 5
# a = lambda x: x * 3
# print(a(x))

# a = '1'
# b = map(int, a)
# print(list(b))

# a = map(lambda x, y: x ** y, [1,2,3], [1,2,3])
# print(list(a))


def filter_(num):
    if num > 0:
        return True
    else:
        return False


a = list(filter(filter_, [1, 2, 3, -4, 4]))
a = list(filter(lambda x: x > 0, [1, 2, 3, -4, 4]))
a = [x for x in [1, 2, 3, -4, 4] if x > 0]
print(a)
