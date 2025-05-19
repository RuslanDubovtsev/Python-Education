import inspect

def gen():
    for i in range(3):
        try:
            yield i
        except GeneratorExit as e:
            print(f"{i} - stopped")
            return

def gen2():
    while True:
        something = yield
        print(f"something - {something}")

def gen3():
    item = 0
    while True:
        send_item = yield item
        print(f"item = {item}")
        print(f"send_item = {send_item}")
        item += 1

# g = gen()
# print(inspect.getgeneratorstate(g))
# next(g)
# print(inspect.getgeneratorstate(g))
# g.close()
# print(inspect.getgeneratorstate(g))

# g2 = gen2()
# print(inspect.getgeneratorstate(g2))
# next(g2)
# g2.send("Hello")
# g2.send("World")

# g3 = gen3()
# print(inspect.getgeneratorstate(g3))
# next(g3)
# g3.send(5)
# g3.send(24)
# g3.send(467)
# g3.send(57)

# ______Homework

# def generator1():
#     elem = 0
#     while True:
#         number = yield
#         elem += number
#         print(f"Получено - {number}. Отправлено - {elem}")
#
# g = generator1()
# next(g)
# g.send(5)
# g.send(7)
# g.send(5)
# g.send(7)
# g.send(5)
# g.send(7)
# g.send(5)
# g.send(7)
#
# def generator2():
#     while True:
#         number = yield
#         if number >= 0:
#             print(number ** 2)
#         else:
#             print('')
#
# g = generator2()
# next(g)
# g.send(0)

# -----------------------
def sub_gen():
    elem = 0
    while True:
        number = yield
        if number == 0:
            return
        elem += number
        print(f"Получено - { number}. Отправлено - {elem}")




def main_gen():
    g = sub_gen()
    print(main_gen().__name__, "активирован\n--------------------")
    yield from g


# def addition_numbers(main):
#     next(main)
#     while True:
#         num = int(input("Какое число вы хотите добавить?: "))
#         try:
#             main.send(num)
#         except StopIteration as e:
#             print("Stopped in addition_numbers")
#             break

# addition_numbers(main_gen())


def generator(password):
    count = 0
    while True:
        text = yield
        if str(text) != password:
            print("Пароль был введен неверно")
            count += 1
            if count > 5:
                print("Пароль был введен неверно свыше 5 раз")
                break
        else:
            print(f"Пароль {text} соответствует паролю {password} и был введен за {count} количество попыток")
            break



def pass_generator():
    g = generator('123')
    print(pass_generator().__name__, "активирован\n--------------------")
    yield from g

def addition_numbers(main):
    next(main)
    while True:
        password = input("Какой пароль?: ")
        main.send(password)

addition_numbers(pass_generator())