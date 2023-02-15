class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age > 100:
            self.__age = 100
        elif new_age < 0:
            self.__age = 0
        else:
            self.__age = new_age
        print("age was set!")


p1 = Person("Jack", 31)
print(p1.age)
p1.age = 150
print(p1.age)