class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


square = Square(3)
print(f'area = {square.area()}')
print(f'perimeter = {square.perimeter()}')
# print(dir(square))
print(square.__class__.__bases__)
