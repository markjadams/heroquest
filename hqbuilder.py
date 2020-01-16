###############################################################
### HQ Builder - Predefined characters and treasure         ###
###############################################################

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
    elif name == "dark elf"   : monster = Character("dark_elf"   , 4, 2, 2, False)
    elif name == "evil wizard": monster = Character("evil_wizard", 6, 2, 2, False)
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
