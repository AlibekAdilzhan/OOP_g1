class Fruit:
    counter = 0
    def __init__(self, name, price):
        self.__name = name
        self.price = price
        type(self).counter += 1

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

f = Fruit("banana", 200)
# f.set_name("apple")
g = Fruit("apple", 400)
print(Fruit.counter)
print(g.counter)