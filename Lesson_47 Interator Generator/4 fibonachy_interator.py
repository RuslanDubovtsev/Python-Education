def fibonachi(num):
    res = []
    start = 0
    next = 1
    for _ in range(num):
        res.append(start)
        start, next = next, start + next
    return res

def fibonachi2(num):
    start = 0
    next = 1
    for _ in range(num):
        yield start
        start, next = next, start + next
        if start > 10 ** 6:
            return

fib = fibonachi2(1000)
print(fib)
print(next(fib))

for i in fib:
    print(i)

class Fibonachi:
    def __init__(self, number):
        self.counter = 0
        self.start = 0
        self.next = 1
        self.number = number

    def __iter__(self):
        self.counter = 0
        self.start = 0
        self.next = 1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > self.number:
            raise StopIteration
        self.start, self.next = self.next, self.start + self.next
        return self.start


fib = Fibonachi(10)

"""
for elem in fib:
    print(elem)
"""

