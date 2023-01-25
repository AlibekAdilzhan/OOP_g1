class Adam:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)


class Soldier(Adam):
    def __init__(self, sold_name, sold_age, rank):
        super().__init__(sold_name, sold_age)
        self.sold_rank = rank

    def upgrade_rank(self, new_rank):
        self.sold_rank = new_rank
        print(self.name, "was upgraded to", self.sold_rank)


a1 = Adam("Ermek", 20)
s1 = Soldier("Mike", 19, "leutenant")
s1.upgrade_rank("kalash")
print(s1.name)