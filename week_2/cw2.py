class Animal:
    def __init__(self, food, location):
        self.food = food
        self.location = location

    def make_noise(self):
        print("animal is making noise")

    def eat(self):
        print("animal is eating", self.food)

    def sleep(self):
        print("animal is sleeping")


class Dog(Animal):
    def __init__(self, name, food, location):
        super().__init__(food, location)
        self.name = name

    def make_noise(self):
        print(self.name, "is barking")


class Vet:
    def __init__(self, name):
        self.name = name

    def treat_animal(self, animal):
        print(animal.food, animal.location)


dog_1 = Dog("Tuzik", "korm", "butka")
dog_1.make_noise()
vet1 = Vet("Dulittle")
vet1.treat_animal(dog_1)