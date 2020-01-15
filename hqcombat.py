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
    if defender.hero == True:
        return get_hero_blocks(defender.defense)
    return get_monster_blocks(defender.defense)

def attack(attacker, defender):
    # attack dice
    hits = get_hits(attacker.attack)
    if hits == 0:
        print(attacker.name + " attacked " + defender.name + " but missed.")
        return
    # defense dice
    blocks = get_blocks(defender)
    if blocks >= hits:
        print(attacker.name + " attacked but " + defender.name + " blocked.")
        return
    # damage
    damage = hits - blocks
    print(attacker.name + "  inflicted " + str(damage) + " points of damange on " + defender.name + ".")
    #body points
    defender.body -= damage
    if defender.body < 1:
        print(str(defender.name) + " is defeated.")
        return
    print(str(defender.name) + " has " + str(defender.body) + " body points remaining.")

def fight(hero, monster):

    print(hero.name + " is fighting " + monster.name + ".")
    print(hero.name    + " has " + str(hero.body)    + " body points. " + monster.name + " has " + str(monster.body) + " body points.")

    while True:
        attack(hero, monster)
        if monster.body < 1: break
        attack(monster, hero)
        if hero.body < 1: break

    if hero.body == 0:
        print("You were defeated by " + monster.name)
        exit
    if monster.body == 0:
        print("You defeated " + monster.name)
