import random

class Character:
    def __init__(self, name, hp, min_damage, max_damage):
        self.name = name
        self.hp = hp
        self.min_damage = min_damage
        self.max_damage = max_damage

    def attack(self):
        damage = random.randint(self.min_damage, self.max_damage)
        critical_attack_rate = 0.4
        if random.random() < critical_attack_rate:
            damage *= 2
            print("Critical Attack! Double damage!!!")
        return damage

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False



