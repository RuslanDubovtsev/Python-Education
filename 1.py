# def factory_auto(color, price, model):
#     def bmw():
#         model = 'BMW'
#         return f'BMW {color} - {model}'
#
#     def lada():
#         model = 'LADA'
#         return f'lada {color} - {model}'
#
#     if price > 50000:
#         return bmw()
#     if price < 50000:
#         return lada()
#
# x3 = factory_auto('red', 100000, 'x3')
# print(x3)
# lada_kalina = factory_auto('red', 10000, 'kalina')
# print(lada_kalina)


# def example(func):
#     def wrapper(*args, **kwargs):
#         if args[1] > 16:
#
#             res = func(*args, **kwargs)
#             return res
#         if args[1] < 20:
#             return f'{args[0]} - goodbye'
#     return wrapper
#
# @example
# def func(name, age):
#     return f'{name} - {age}'
#
# a = func('Rus', 16)
#
# print(a)

# lips
# a = lambda x, y, z: x + y + z
#
# res = a(1, 2, 3)
# print(res)


# b = [1,2,3,4,5, 120, 110]
#
# c = map(lambda x: x ** 2, b)
# print(list(c))


# d = filter(lambda x: x > 100, b)
# print(list(d))

# _______________________________
# class FormMixin:
#     def some_method(self):
#         return f'I {self} am mixin'
#
#
# class CreateView:
#     def __init__(self, some1, some2):
#         self.some1 = some1
#         self.some2 = some2
#
#     def get_context_data(self):
#         return f'{self.some1}'
#
#     def suc_url(self):
#         return f'{self.some2}'
#
# class ChildView(CreateView, FormMixin):
#     def __init__(self, some1, some2, some3):
#         super().__init__(some1, some2)
#         self.some3 = some3
#
#     def get_context_data(self):
#         super().get_context_data()
#         return f'{self.some1} - {self.some2} - {self.some3}'
#
#     def suc_url(self):
#         super().suc_url()
#         return f'{self.some3}'
#
#     def some_method(self):
#         super().some_method()
#         return f'{self} i can make everything what i want'
#
# b = CreateView(some1='parent1', some2='parent2')
# print(b.get_context_data())
# a = ChildView(some1='test1', some2='test2', some3='test3')
# print(a.get_context_data())
# print(a.some_method())

class AUTO:
    def __init__(self, color):
        self.color = color
        self.model = None

class BMW(AUTO):
    def __init__(self, color):
        super().__init__(color)
        self.model = 'BMW'

    def get_BMW(self):
        return f'{self.model}'

class LADA(AUTO):
    def __init__(self, color):
        super().__init__(color)
        self.model = 'LADA'

    def get_LADA(self):
        return f'{self.model}'


class SHOP(BMW, LADA):
    def __init__(self, color, price, ):
        super().__init__(color)
        self.price = price

    def model_car(self):
        if self.price >= 50000:
            return f'{BMW(self.model)}'
        if self.price < 50000:
            return f'{LADA(self.model)}'

# a = SHOP(color='green', price=5001)
# print(a.model_car())
#
#
# a = SHOP(color='green', price=50001)
# b = LADA(color=a)
# c = BMW(color=a)
# if a.price >= 50000:
#     print(c.get_BMW())
# if a.price < 50000:
#     print(b.get_LADA())

class Auto:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f"{self.model}"

    def speed(self, maxspeed):
        print(f"{self.model} have a {maxspeed} km")



class BMW(Auto):
    def __init__(self,color, price, model='BWM'):
        super().__init__(model)
        self.color = color
        self.price = price

    def __str__(self):
        super().__str__()
        return f"{self.model} - {self.price} - {self.color}"

    def speed(self, maxspeed, oil):
        super().speed(maxspeed)
        print(f'{self.model} - {maxspeed} - {oil}')


class Lada(Auto):
    def __init__(self,color, price, model='Lada'):
        super().__init__(model)
        self.color = color
        self.price = price

    def __str__(self):
        super().__str__()
        return f"{self.model} - {self.price} - {self.color}"

    def speed(self, maxspeed, oil):
        super().speed(maxspeed)
        print(f'{self.model} - {maxspeed} - {oil}')

class Shop:
    def choise(self, price, color):
        if price > 100000:
            a = BMW(color=color, price=price)
        if  price < 100000:
            a = Lada(color=color, price=price)
        return a
# a = BMW(color='red', price=100000)
# print(a)
# a.speed(230, 'disiel')
#
# b = Shop()
# print(b.choise(color='red', price=200000))


class Person:
    def __init__(self, school):
        self.school = school

    def __str__(self):
        return f"{self.school}"


class Teacher(Person):
    def __init__(self, school, teacher_name, age, subject):
        super().__init__(school)
        self.age = age
        self.subject = subject
        self.teacher_name = teacher_name

    def __str__(self):
        super().__str__()
        return f"My name is {self.teacher_name}, i'm {self.age} old. I'm from {self.school} and i teach {self.subject}"

    def talk_teacher(self):
        return "Я поставлю тебе двойку"

class Student(Person):
    def __init__(self, school, student_class, type):
        super().__init__(school)
        self.student_class = student_class
        self.type = type

    def __str__(self):
        super().__str__()
        return f"I'm at {self.school} from is {self.student_class} and i am {self.type}"

    def talk_student(self):
        return "Я не сделал домашку"

class School:
    def student(self, school, student_class, type):
        st = Student(school=school, student_class=student_class, type=type)
        return st
    def teacher(self, school, teacher_name, age, subject):
        te = Teacher(school=school, teacher_name=teacher_name, age=age, subject=subject)
        return te


# t = Teacher(school='№144', teacher_name='Elena', age=21, subject='math')
# s = Student(school='№144', student_class='A', type='B-student')
# a = School()
# print(a.teacher(school='№144', teacher_name='Elena', age=21, subject='math'))
# print(t.talk_teacher())
# print(a.student(school='№144', student_class='A', type='B-student'))
# print(s.talk_student())
a = School()
b = a.student(school='№144', student_class='A', type='B-student')
c = a.teacher(school='№144', teacher_name='Elena', age=21, subject='math')
print(c.talk_teacher())
print(b.talk_student())
print(b)