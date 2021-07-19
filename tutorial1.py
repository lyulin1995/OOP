import OOP5  # import all of the classes and functions that are within this file
from OOP5 import NotPrivate  # from OOP5 importing not private

test = NotPrivate('tim')
#  without from OOP5..., you should type: test = OOP5.NotPrivate('tim')
test.display()
test._display()

