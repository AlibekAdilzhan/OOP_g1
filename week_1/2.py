class Person:
    def __init__(self, name, age):
        self.p_name = name
        self.p_age = age
        self.married = False

    def get_age(self):
        return self.p_age

    def set_age(self, new_age):
        self.p_age = new_age


p1 = Person("Hannah", 15)
print(p1.get_age()) # 15
p1.set_age(25)
print(p1.get_age()) # 25






