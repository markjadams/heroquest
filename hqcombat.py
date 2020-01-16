###############################################################
# Combat
###############################################################

#project imports
#from hqcore import roll_dice
#from hqcore import points_to_str

from random import randint
from hqchar import Character

###############################################################
# Roll a D6 dice
###############################################################

def roll_dice() -> int:
    return randint(1, 6)

###############################################################
# Roll attack dice
###############################################################

def get_hits(character: Character) -> int:
    hits = 0
    for a in range(character.get_attack_with_bonus()):
        diceResult = roll_dice()
        if diceResult > 3:
            hits +=1
    return hits

###############################################################
# Roll defense dice
###############################################################

def get_blocks(character: Character) -> int:
    hits = 0
    for a in range(character.get_defense_with_bonus()):
        diceResult = roll_dice()
        if diceResult <= (2 if character.is_hero else 1):
            hits +=1
    return hits

###############################################################
# Perform a single attack and block, reporting outocme
###############################################################

def attack(attacker: Character, defender: Character):
    # attack dice
    hits = get_hits(attacker)
    if hits == 0:
        print(attacker.format_name(True) + " attacked " + defender.format_name() + " but missed.")
        return
    # defense dice
    blocks = get_blocks(defender)
    if blocks >= hits:
        print(attacker.format_name(True) + " attacked but " + defender.format_name() + " blocked.")
        return
    # damage
    damage = hits - blocks
    print(attacker.format_name(True) + " inflicted " + str(damage) + " damange on " + defender.format_name() + ".")
    #body points
    defender.health_remaining -= damage
    if defender.health_remaining < 1:
        print(defender.format_name(True) + " was defeated by " + attacker.format_name() + ".")
    else:
        print(defender.format_name(True) + " has " + str(defender.health_remaining) + " health remaining.")

###############################################################
# Fight...to the death!
###############################################################

def fight(attacker: Character, defender: Character):

    print(attacker.format_name(True) + " is fighting " + defender.format_name() + ".")
    print(attacker.format_name(True) + " has " + str(attacker.health_remaining) + ". " + defender.format_name(True) + " has " + str(defender.health_remaining) + ".")

    while True:
        attack(attacker, defender)
        if defender.health_remaining < 1: break
        attack(defender, attacker)
        if attacker.health_remaining < 1: break
