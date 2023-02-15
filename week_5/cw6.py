class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b


r1 = Rectangle(1, 2)
print(r1.area)
