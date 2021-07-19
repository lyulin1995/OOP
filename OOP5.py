class _Private: # for private, we have one underscore at the beginning of the class name
    """within something like it's not accessible outside of that
    _ + class name"""
    def __init__(self, name):
        self.name = name


class NotPrivate:
    """public means it is accessible everywhere"""
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(self):  # private method: _ + method name
        print('Hello')

    def display(self):
        print('Hi')

#  Private classes typcially can only be used within the same file or within a certain scope.
#  Public classes are accessed or can be accessed by everyone.
#  for private: not use them and not mess them
