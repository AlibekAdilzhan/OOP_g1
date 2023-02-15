class Car:
    def __init__(self, mark, owner):
        self.__mark = mark
        self.owner = owner

    @property
    def mark(self):
        return f"Mark is {self.__mark}"

    @mark.setter
    def mark(self, new_mark):
        print("you can't change mark")
        return
        self.__mark = new_mark


c1 = Car("Mersedes", "Nurik")
c1.mark = "BMW"
print(c1.mark)
