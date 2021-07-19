# import turtle

x = 5  # x is equal to an instance of the int class, x is an object of type int
y = 'string'  # y is equal to an instance of the STR class


#
# # creating a new instance of a turtle object.
# # In the turtle module, there is a class name Turtle.
# # creating a new turtle object and storing it in a variable tim.
# tim = turtle.Turtle()
#
# def func(x):
#     return x + 1
#
# print(func(5))

# # a method is what you call with the dot operator.
# tim = turtle.Turtle()
# # is a method that creates a new turtle object.
# print(y.upper())
# # upper()is not a function. it's actually a method. Only apply to String data type.
# print(y.replace('s', ''))
# # y is the instance, replace is the method.


# Creating class
class Dog(object):
    def __init__(self, name, age):  # constructor method
        """attributes are kind of like variables that belong to a certain object
        using self keyword to create an attribute
        self stands for the instance that you are calling
        self actually represents the instance"""
        self.name = name  # create this initialization
        self.age = age
        # self.li = [1, 3, 4]
        # print('nice you made a dog')

    def speak(self):  # method are created using def, have to call them using an object
        print("Hi, I am", self.name, 'and i am', self.age, 'years old')

    def talk(self):
        print('Bark!')
    #
    # def change_age(self, age):
    #     self.age = age
    #
    # def add_weight(self, weight):
    #     self.weight = weight  # create a new instance attribute


# # __init__ is automatically going to happen
# # tim is know as an instance of type Dog or Class Dog
# # tim is what's being passed into this self parameter
# tim = Dog('Tim', 53)
# # self.name = name -> tim.name is equal to whatever name we put in ''
# fred = Dog('Fred', 3)  # fred is another instance of type Dog
# tim.change_age(5)
# tim.add_weight(70)
# tim.speak()
# fred.speak()
#
# print(tim.name)
# print(tim.age)
# print(tim.li)
# print(tim.weight)

# Benefit of class:
# you can create multiple objects of a class

# Inheritance:
# # copy it -> not good
# class Cat(object):
#     def __init__(self, name, age, color):  # constructor method
#         self.name = name  # create this initialization
#         self.age = age
#         self.color = color
#
#     def speak(self):  # method are created using def, have to call them using an object
#         print("Hi, I am", self.name, 'and i am', self.age, 'years old')

class Cat(Dog):  # Parent in the bracket
    """Cat is going to inherit from Dog.
    Dog is the parent class, and Cat is the child class.
    Cat inherits all properties and attributes and method of that Class.
    """

    def __init__(self, name, age, color):
        """the initialization of Dog and add it to Cat object of tim"""
        super().__init__(name, age)
        self.color = color  # unique to cat
        """we are gonna change whatever happen in the Dog class. e.g. name"""
        self.name = 'tech'

    def talk(self):
        """Override the talk method to change things."""
        print('Meow!')


jim = Dog("Jim", 70)
jim.talk()

tim = Cat('Tim', 5, 'blue')
tim.speak()
tim.talk()
