#########################################
### Combat                            ###
#########################################

#project imports
from hqcore import roll_dice
from hqcore import points_to_str

from hqchar import Character

def get_hits(attackPoints):
    hits = 0
    for a in range(attackPoints):
        diceResult = roll_dice()
        if diceResult > 3: hits +=1
    return hits

def get_hero_blocks(defensePoints):
    hits = 0
    for a in range(defensePoints):
        diceResult = roll_dice()
        if diceResult == 2 or diceResult == 3:
            hits +=1
    return hits

def get_monster_blocks(defensePoints):
    hits = 0
    for a in range(defensePoints):
        diceResult = roll_dice()
        if diceResult == 1:
            hits +=1
    return hits

def get_blocks(defender):
    if defender.is_hero == True:
        return get_hero_blocks(defender.defense)
    return get_monster_blocks(defender.defense)

def attack(attacker, defender):
    # attack dice
    hits = get_hits(attacker.attack)
    if hits == 0:
        print(attacker.format_name(True) + " attacked the " + defender.format_name() + " but missed.")
        return
    # defense dice
    blocks = get_blocks(defender)
    if blocks >= hits:
        print(attacker.format_name(True) + " attacked but the " + defender.format_name() + " blocked.")
        return
    # damage
    damage = hits - blocks
    print(attacker.format_name(True) + " inflicted " + str(damage) + " " + ("point" if damage == 1 else "points") + " of damange on " + defender.format_name() + ".")
    #body points
    defender.body_remaining -= damage
    if defender.body_remaining < 1:
        print(defender.format_name(True) + " was defeated by " + attacker.format_name() + ".")
        return
    print(defender.format_name(True) + " has " + str(defender.body_remaining) + " body points remaining.")

def fight(hero, monster):

    print(hero.name + " is fighting the " + monster.name + ".")
    print(hero.name    + " has " + points_to_str(hero.body_remaining, "body") + ". The " + monster.name + " has " + points_to_str(monster.body_remaining, "body") + ".")

    while True:
        attack(hero, monster)
        if monster.body_remaining < 1: break
        attack(monster, hero)
        if hero.body_remaining < 1: break
