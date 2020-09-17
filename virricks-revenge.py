import random
import char_classes 
import textwrap

## Class for charaters in the game
class toon:
## Assing attributes from char_class file
    def __init__(self, attribs):
        self.name = attribs["name"] 
        self.toon_class = attribs["class"]
        self.health = attribs["health"]
        self.mana = attribs["mana"] 
        self.attack_power = attribs["attack"]
        self.armor_class = attribs["armor"]

## Known Spells
# Not sure how to handle the spell list
    spells = {"heal_less": "char_classes.heal_less"} ##Not used at the moment
    
## Check if char is dead
    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False

## Spell Casting function
    def cast_spell(self, spl_amount, mana):
        if self.mana < mana:
            return True
        else:
            min_amount = spl_amount / 2
            max_amount = spl_amount + 5 
            spell_amount = random.randint(min_amount, max_amount) 
            self.mana -= mana
            return spell_amount 

## Calculate if hit or miss. If hit then return damage
    def attack_dmg(self, ar_class):
        hit_check = random.randint(1, 20)
        min_amount = int(self.attack_power / 2)
        if hit_check >= ar_class:
            attack_dmg = random.randint(min_amount, self.attack_power)
            return attack_dmg
        else:
            return False

### Status window. ToDo: Create a file for all status windows.
def status_box():
    print(f"""
------------------------------------------------
|  Name: {player.name}   Class: {player.toon_class}   |
|----------------------------------------------|
|  Health: {player.health}  Mana: {player.mana}       |
|-----------------------------------------------
           """) 
def attack_box():
    print("Enter a selection:")
    print("""
           1: Attack
           2: Cast Magic 
           3: Exit Game""")


## Battle Loop
def battle():
## Generate random monster
    random_monster = random.randint(1, 3)
    if random_monster == 1:
        monster = toon(char_classes.nargath)
    elif random_monster == 2:
        monster = toon(char_classes.acid_slime)
    else:
        monster = toon(char_classes.red_dragon)
    print(f"You have encountered a {monster.name}!")

## Start battle Loop
    while player.is_dead() == False and monster.is_dead() == False: 
        status_box()
        attack_box()
        sel = int(input("Selection: "))

## Attack Monster and do a hit check
        if sel == 1:
            print(f"You attack the {monster.name}!")
            hit_check = player.attack_dmg(monster.armor_class) 
            if hit_check == False:
                print("You miss!")
            else:
                print(f"You hit the {monster.name} for {hit_check} hit points!")
                monster.health -= hit_check

## Monster attacks and do a hit check
            print(f"The {monster.name} attacks back!")
            hit_check = monster.attack_dmg(player.armor_class)
            if hit_check == False:
                print(f"The {monster.name} misses you!")
            else:
                print(f"The {monster.name} hits you for {hit_check} hit points!")
                player.health -= hit_check

## Heal Spell. ToDo: Create a spell list depending on class.
        elif sel == 2:
            mana_check = player.cast_spell(char_classes.heal_less["heal_amount"], char_classes.heal_less["mana_cost"])
            if mana_check == True:
                print("You are too low on mana to cast that spell!") 
            else:
                player.health += mana_check 
                print(f"You healed for {mana_check}! Your hit points are now {player.health}")

 ##Check to see if dead
        if player.is_dead() == True:
            print(f"The {monster.name} has defeated you!")
        elif monster.is_dead() == True:
            print(f"You have defeated the {monster.name}!")
########################################################################                 

### Char creation screen
char_name = input("Enter your char name: ")
print(f"Welcome {char_name}!")
print("Select the class you would like to be.")
print("""
        1: Warrior
        2: Wizard""")
char_class = int(input("Selection?  "))
if char_class == 1:
    player = toon(char_classes.warrior) 
    player.name = char_name
else:
    player = toon(char_classes.wizard)
    player.name = char_name

## Start Battle   
battle()
