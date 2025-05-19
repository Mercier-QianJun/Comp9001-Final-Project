import random

def dragon_attack():
    dragon_damage = random.randint(5,15)
    return dragon_damage

def guess_right(guess, target):
    if guess == target:
        return True
    else:
        return False

