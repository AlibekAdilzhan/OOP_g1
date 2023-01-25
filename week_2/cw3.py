from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__()

    @abstractmethod
    def kill(self):
        pass


class Doctor(Person):
    def __init__(self, name, age, work_place):
        super().__init__(name, age)
        self.work_place = work_place

    def kill(self):
        print(self.name, "was killed in", self.work_place)

d1 = Doctor("Aman", 34, 19)
