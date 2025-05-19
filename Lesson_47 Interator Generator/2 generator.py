def infinity():
    count = 1000000000000000000000000000000000000000000000000000000000000
    for i in range(count):
        if count > 1:
            yield i
        else:
            count += 1000000000000000000000000000000000000000000000000000000000000

# for elem in infinity():
#     print(elem)


class Interator:
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.counter += 1
            return self.counter

# a = Interator()
# for i in a:
#     print(i)


# Homework
def checkSimpleNumber(number):
    for num in range(2, number):
        if number % num == 0:
            return True
        print(num)
    return False
# print(checkSimpleNumber(6))


def is_prime(number):
    counter = 0
    for num in range(2, number):
        if number % num == 0:
            counter += 1
            break
        if counter == 0:
            return True
        return False

# if is_prime(5):
#     print("Число простое")
# else:
#     print("Число составное")


class PrimeInterator:
    def __init__(self, number):
        self.start = 2
        self.number = number
        self.prime_list = []

    def __iter__(self):
        return self

    def __next__(self):
        for elem in range(self.start, self.number):
            for num in self.prime_list:
                if elem % num == 0:
                    break

            else:
                self.start = elem
                self.prime_list.append(elem)
                return self.start
        raise StopIteration


primes_num = PrimeInterator(50)
for elem in primes_num:
    print(elem, end=" ")


def primeGenerator(number):
    prime_list = []
    start = 2
    for elem in range(start, number):
        for num in prime_list:
            if elem % num == 0:
                break
        else:
            start = elem
            prime_list.append(elem)
            yield start

for i in primeGenerator(50):
    print(i)


def checkSimpleNumber2(number):
    if number <= 2:
        yield f"Простое число {number}"
    for num in range(2, number):
        if number % num == 0:
            yield f"Составное число {num}"
            # return f"Составное число {num}"

        else:
            yield f"Простое число {num}"

number = int(input(": "))
for elem in checkSimpleNumber2(number):
    print(elem)