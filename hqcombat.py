#########################################
### Combat                            ###
#########################################

#project imports
import hqcore
import hqchar

def get_hits(attackPoints):
    hits = 0
    for a in range(attackPoints):
        diceResult = hqcore.roll_dice()
        if diceResult > 3: hits +=1
    return hits

def get_hero_blocks(defensePoints):
    hits = 0
    for a in range(defensePoints):
        diceResult = hqcore.roll_dice()
        if diceResult == 2 or diceResult == 3:
            hits +=1
    return hits

def get_monster_blocks(defensePoints):
    hits = 0
    for a in range(defensePoints):
        diceResult = hqcore.roll_dice()
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
    defender.body -= damage
    if defender.body < 1:
        print(defender.format_name(True) + " was defeated by " + attacker.format_name() + ".")
        return
    print(defender.format_name(True) + " has " + str(defender.body) + " body points remaining.")

def fight(hero, monster):

    print(hero.name + " is fighting the " + monster.name + ".")
    print(hero.name    + " has " + str(hero.body)    + " body points. The " + monster.name + " has " + str(monster.body) + " body points.")

    while True:
        attack(hero, monster)
        if monster.body < 1: break
        attack(monster, hero)
        if hero.body < 1: break

    #if hero.body == 0:
    #    print("You were defeated by the " + monster.name)
    #    exit
    #if monster.body == 0:
    #    print("You defeated the " + monster.name)
