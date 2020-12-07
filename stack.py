# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# Ian Snyder

class Stack:

    def __init__(self):
        self.items = []
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty() is True:
            raise IndexError
        else:
            x = self.items.pop(self.size - 1)
            self.size -= 1
            return x

    def peek(self):
        if self.is_empty() is True:
            raise IndexError
        else:
            return self.items[self.size - 1]

    def push(self, item):
        self.items.append(item)
        self.size += 1