def squaring_generator(num, limit):
    c = 0
    num2 = num
    while c <= limit:
        num2 = num2 ** 2
        yield num2
        c += 1


# func = squaring_generator(10, 5)
# for i in func:
#     print(i)

# class Squaring_Interator:
#     def __init__(self, number, limit):
#         self.number = number
#         self.counter = 0
#         self.limit = limit
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.counter >= self.limit:
#             raise StopIteration
#         self.number = self.number ** 2
#         self.counter += 1
#         return self.number

# func = Squaring_Interator(10, 5)
# for i in func:
#     print(i)

class Squaring_Interator:
    def __init__(self, number):
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.number:
            raise StopIteration
        else:
            self.counter += 1
            return self.counter ** 2

func = Squaring_Interator(10)
print(next(func))
# for i in func:
#     print(i)


limit = 5
# func = (i**2 for i in range(0, limit + 1))
# for i in func:
#     print(i)
print(func)