class Dog:
    """#class variables, not in side of one of your method
    don't have to initialize e.g. self.dogs = dogs
    not specific to Jim and Tim
    only specific to the entire class"""
    dogs = []
    xc = 5

    def __init__(self, name):
        self.name = name  # regular variables, reference later: self.name
        self.dogs.append(self)  # appending every single dog object that we create into the list dogs

    """classmethod: can call it on simply the name of the class"""

    @classmethod  # decorator: you are creating a class method
    def num_dogs(cls):  # cls means the name of the class
        return len(cls.dogs)

    """staticmethod: don't a class to be called
    it doesn't pass in the class
    you can not reference anything in the class
    we only pass whatever parameters we want
    don't need parameters
    don't touch any attributes, and any class methods
    can not call length of dogs since there is not a self"""

    """just using them as a function"""
    @staticmethod
    def bark(n):
        """barks n times"""
        for _ in range(n):
            print("Bark!")


class Math:
    @staticmethod
    def add(x, x2):
        return x + x2


tim = Dog("Tim")
jim = Dog('Jim')
# for class variables, you can call using tim.dogs and also using actual class name: Dog.dogs
# don't have to have an instance to call that
print(Dog.dogs)
print(Dog.num_dogs())
print(tim.num_dogs())

Dog.bark(5)

# do not have to create an instance of math e.g. m = Math() x
print(Math.add(1, 3))

