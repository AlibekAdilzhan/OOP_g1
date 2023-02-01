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

    def __lt__(self, v):
        d1 = (self.a**2 + self.b**2 + self.c**2)**(0.5)
        d2 = (v.a**2 + v.b**2 + v.c**2)**(0.5)
        if d1 < d2:
            return True
        else:
            return False

    def __le__(self, v):
        d1 = (self.a**2 + self.b**2 + self.c**2)**(0.5)
        d2 = (v.a**2 + v.b**2 + v.c**2)**(0.5)
        if d1 <= d2:
            return True
        else:
            return False

# a1 = int(input())
# b1 = int(input())
# c1 = int(input())
# a2 = int(input())
# b2 = int(input())
# c2 = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

v1 = Vector3(*a)
v2 = Vector3(*b)
print(v1 <= v2)