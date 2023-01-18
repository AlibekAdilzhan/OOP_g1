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



p1 = Person("Kag", 19, 189)
p2 = Person("Potter", 18, 180)

p1.hp -= 50
p1.get_hp()
p2.get_hp()
p1.get_info()