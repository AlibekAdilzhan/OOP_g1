class Person:
    def __init__(self, name, age, height):
        self.p_name = name
        self.p_age = age
        self.p_height = height
        self.hp = 100

    def get_hp(self):
        print(self.hp)

    def get_info(self):
        print(self.hp, self.p_name, self.p_age, self.p_height)

    # getter
    def get_name(self):
        return self.p_name

    def set_name(self, new_name):
        self.p_name = new_name

p1 = Person("Kag", 19, 189)
p2 = Person("Potter", 18, 180)


print(p1.get_name())
p1.set_name("ksjfd")
print(p1.get_name())