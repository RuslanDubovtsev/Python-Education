'''
def count(number):
    print(number)
    if number <= 0:
        return 0
    else:
        return count(number - 1)

count(6)
'''

'''
def sum(seq):
    summ = 0
    for elem in seq:
        summ += elem
    return summ
print(sum([1,2,3,4,5]))


def sum_list(seq):
    if seq == []:
        return 0
    print(seq[1:])
    return seq[0] + sum_list(seq[1:])

print(sum_list([1,2,3,4,5]))
'''

'''
def factorial(number):
    fact = 1
    for elem in range(1, number + 1):
        fact *= elem
    return fact
print(factorial(3))


def factorial2(number):
    if number == 1:
        return 1
    else:
        return number * factorial2(number - 1)
print(factorial2(3))
'''

'''
def box(seq):
    for elem in seq:
        print(seq)
        if not isinstance(elem, list):
            if elem == 'ключ':
                return "ключ найден"
        else:
            return box(elem)

print(box([[['ключ']], [], [[[]]]]))
'''

# ________ДЗ________
'''
def number(num):
    print(num)
    if num <= 0:
        return 0
    else:
        return number(num - 1)
number(6)
'''

'''
def factorial(number):
    fact = 1
    for elem in range(1,number + 1):
        fact *= elem
    return fact
print(factorial(3))
'''

'''
def summa(num):
    sum = 0
    for elem in num:
        sum += elem
    return sum
print(summa([1,2,3,4,5]))


def summa2(num):
    if num == []:
        return 0
    print(num[1:])
    return num[0] + summa2(num[1:])
print(summa2([1,2,3,4,5]))
'''


def dict1(site):
    string = input("Введите ключ: ")
    for elem in site:
        if not isinstance(elem, dict):
            if string == elem:
                print(site.get(string))
            else:
                return dict1(site)


print(dict1(site = {

    'html': {

        'head': {

            'title': 'Мой сайт'

        },

        'body': {

            'h2': 'Здесь будет мой заголовок',

            'div': 'Тут, наверное, какой-то блок',

            'p': 'А вот здесь новый абзац'

        }

    }

}))



