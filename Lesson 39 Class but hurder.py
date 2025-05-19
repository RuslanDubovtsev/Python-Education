# class People:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def say(self):
#         print(f'hello, my name is {self.name}, my age - {self.age} ')
#
#
# class Person(People):
#     def say_personal(self):
#         print('I am worker')
#
# class Person2(People):
#     def some(self):
#         print('GoodBye')
#
# person1 = Person(name='Rustam', age=32, gender='man')
#
# person1.say()
# person1.say_personal()
# person1.say()


# class Math:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#
#
# class Plus(Math):
#     def plus(self):
#         return self.num1 + self.num2
#
#
# class Pow(Math):
#     def pow(self):
#         return self.num1 ** self.num2
#
# plus1 = Plus(num1=1232323, num2=3483430)
#
# print(plus1.plus())
#
# pow1 = Pow(num2=23, num1=4394)
#
# print(pow1.pow())



# class Player:
#     def __init__(self, gender, age, color):
#         self.gender = gender
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         return f"{self.gender}, {self.age}, {self.color}"
#
#
# class Police(Player):
#     def conversation(self):
#         return 'Stop now!!!'
#     def damage(self):
#         return "'-50hp police'"
#     def shoot(self):
#         return "'Звуки стрельбы'"
#
# class player(Player):
#     def player_angry(self):
#         return "NO!!! GO AWAY"
#     def hit(self):
#         return 'hit'
#     def miss(self):
#         return "Miss"
#
#
#
#
# police1 = Police(gender='man', age=28, color='white')
#
# player1 = player(gender='man', age=29, color='white')
#
# print(police1)
# print(police1.conversation())
# print(player1)
# print(player1.player_angry())
# print(player1.hit())
# print(police1.damage())
# print(police1.shoot())
# print(player1.miss())
#


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} - {self.age}"
    def say(self):
        return f"My name is {self.name}. Who are you"



class Employers(Person):
    def __init__(self, name, age, job, rise, firm):
        Person.__init__(self, name, age)
        self.job = job
        self.rise = rise
        self.firm = firm
    def say(self):
        print(f"My name is {self.name}. I work {self.job} in {self.firm}. I get {self.rise} tenge in month")


class Unemployed(Person):
    def __init__(self, name, age, time_no_working):
        Person.__init__(self, name, age)
        self.time_no_working = time_no_working
    def say(self):
        return f"My name is {self.name}. I don't work {self.time_no_working} months"

person1 = Person(name="Ruslan", age=20)
employers1 = Employers(name="Ruslan", age=20, job="RPA-developer", rise=1200000, firm="Beeline")
unemployed1 = Unemployed(name='Valera', age=23, time_no_working=7)
print(person1)
print(person1.say())
print(employers1.say())
print(unemployed1.say())