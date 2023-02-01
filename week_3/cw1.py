class Vector3:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"{self.a} {self.b} {self.c}"

    def __add__(self, v):
        new_v = Vector3(self.a + v.a, self.b + v.b, self.c + v.c)
        return new_v

    def __eq__(self, v):
        if self.a == v.a and self.b == v.b and self.c == v.c:
            return True
        else:
            return False


v1 = Vector3(1, 0, 2)
v2 = Vector3(1, 0, 2)
print(v1 == v2)