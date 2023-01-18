class Enemy:
    def __init__(self, weapon, enemy_type, is_boss):
        self.hp = 100
        self.mana = 100
        self.weapon = weapon
        self.type = enemy_type
        self.is_boss = is_boss

    def get_hp(self):
        return self.hp

    def get_weapon(self):
        return self.weapon

    def set_weapon(self, new_weapon):
        self.weapon = new_weapon


enemy_1 = Enemy("ak47", "soldier", False)
enemy_2 = Enemy("mk", "soldier", False)

print(enemy_1.get_weapon())
enemy_1.set_weapon("pistol")
print(enemy_1.get_weapon())