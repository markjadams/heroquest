###############################################################
### HQ Builder - Predefined characters and treasure         ###
###############################################################

from random     import randint
from hqchar     import Character
from hqtreasure import Treasure

###############################################################
### Get standard hero profiles by name                      ###
###############################################################

def get_hero(name: str) -> Character:
    hero: Character = None
    if   name == "thor": hero = Character("Thor", 4, 3, 8, True)
    return hero

###############################################################
### Get standard monster profiles by name                   ###
###############################################################

def get_monster(name: str) -> Character:
    monster: Character = None
    if   name == "goblin"     : monster = Character("goblin"     , 3, 1, 1, False)
    elif name == "ogre"       : monster = Character("ogre"       , 3, 2, 2, False)
    elif name == "troll"      : monster = Character("troll"      , 3, 4, 4, False)
    elif name == "zombie"     : monster = Character("zombie"     , 3, 4, 4, False)
    elif name == "mummy"      : monster = Character("mummy"      , 3, 3, 3, False)
    elif name == "dark_elf"   : monster = Character("dark elf"   , 4, 2, 2, False)
    elif name == "evil_wizard": monster = Character("evil wizard", 6, 2, 2, False)
    elif name == "devil"      : monster = Character("devil"      , 5, 4, 4, False)
    return monster

###############################################################
### Get standard treasure profiles by name                  ###
###############################################################

def get_treasure(name: str) -> Treasure:
    treasure: Treasure = None
    if   name == "shield"    : treasure = Treasure("Shield"           , 0, 1, 100)
    elif name == "long_sword": treasure = Treasure("Long Sword"       , 1, 0, 100)
    elif name == "gold_coins": treasure = Treasure("Gold Coins"       , 1, 0,  50)
    elif name == "helmet"    : treasure = Treasure("Helmet"           , 0, 1, 100)
    elif name == "glamdring" : treasure = Treasure("Glamdring"        , 3, 0, 500)
    elif name == "mithril"   : treasure = Treasure("Mithril chainmail", 0, 3, 500)
    return treasure

###############################################################
### Wandering monster                                       ###
###############################################################

def get_wandering_monster() -> Character:

    dice_roll = randint(1, 100)
    monster = None

    if   dice_roll ==  1: monster = get_monster("goblin")
    elif dice_roll ==  2: monster = get_monster("goblin")
    elif dice_roll ==  3: monster = get_monster("goblin")
    elif dice_roll ==  4: monster = get_monster("goblin")
    elif dice_roll ==  5: monster = get_monster("ogre")
    elif dice_roll ==  6: monster = get_monster("ogre")
    elif dice_roll ==  7: monster = get_monster("troll")
    elif dice_roll ==  8: monster = get_monster("zombie")
    elif dice_roll ==  9: monster = get_monster("mummy")
    elif dice_roll == 10: monster = get_monster("dark_elf")
    
    if monster is not None:
        monster.is_wandering = True

    return monster