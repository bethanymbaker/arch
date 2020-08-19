class Parent:
    def __init__(self, value):
        self._value = value

    def describe(self):
        print(f"Parent: value is {self._value}")


class Child(Parent):
    pass


cld = Child(5)
print(cld._value)
cld.describe()
