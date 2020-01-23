import numpy as np


class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return self.length * 4


square = Square(length=3)

print(square.__class__)
print(f'length = {square.length}')
print(f'area = {square.area()}')
