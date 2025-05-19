from Character import Character
from attack import dragon_attack, guess_right
import random

print("Welcome to <Number vs Dragon>")
print("Please choose your character: ")
print("1. King Arthur(With high hp but low damage)")
print("2. Magician Merlin(With low hp but high damage )")
choose_char = input("Choose from 1 and 2: ")

if choose_char == "1":
    player = Character("Arthur", 300, 10, 20)
    print("Salute to you, my king Arthur!")
elif choose_char == "2":
    player = Character("Merlin", 250, 15, 40)
    print("Glad to see you, big magician Merlin!")
else:
    print("Unknown character, coming soon....")

run = True
while run:
    level = 1
    dragon_count = 0

    while player.is_alive():
        print(f"---Level {level}---")
        dragon_hp = 50 + level*10
        max_number = 20 + level*10
        target = random.randint(1, max_number)
        dragon = Character("Dragon", dragon_hp, 5, 10)

        print("Dragon coming...\n")
        print(f"Guess number from 1~{max_number} to attack it!")

        while player.is_alive() and dragon.is_alive():
            try:
                guess = int(input(f"Pick a nunber from 1 to {max_number}: "))
            except ValueError:
                print(f"Please type a number from 1 to {max_number}")
                continue
            
            if guess_right(guess, target):
                damage = player.attack()
                dragon.hp -= damage
                dragon.hp = max(0, dragon.hp)
                print(f"Nice! You got it! Dragon lose {damage} hp")
                target = random.randint(1, max_number)
            else:
                damage = dragon_attack()
                player.hp -= damage
                player.hp = max(0, player.hp)
                print(f"Wrong number, dragon attack ^n^, you lose {damage} hp")

                if guess < target:
                    print(f"Maybe larger than {guess}")
                else:
                    print(f"Maybe smaller than {guess}")
            
            print(f"Player HP: {player.hp} | Dragon HP: {dragon.hp}")
            print("")

        if not player.is_alive():
            run = False
        
        if not dragon.is_alive():
            print(f"Congratulations, you beat the dragon of level {level}")
            print("")
            level += 1
            dragon_count +=1

print("\nGame Over")
print(f"You totally beat {dragon_count} dragons, end at level {level}")
    
     

                
        


