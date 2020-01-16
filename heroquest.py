###############################################################
###  _   _                _____                 _           ###
### | | | |              |  _  |               | |          ###
### | |_| | ___ _ __ ___ | | | |_   _  ___  ___| |_         ###
### |  _  |/ _ \ '__/ _ \| | | | | | |/ _ \/ __| __|        ###
### | | | |  __/ | | (_) \ \/' / |_| |  __/\__ \ |_         ###
### \_| |_/\___|_|  \___/ \_/\_\\__,_|\___||___/\__|        ###
###                                                         ###
###############################################################

from hqchar   import Character
from hqmaze   import Maze
from hqcombat import fight
from hqmap    import show_map
import re

import dungeon1
import dungeon2

###############################################################
### Print file
###############################################################
def print_file(filename: str) -> None:
    print(open("txt\\" + filename + ".txt", "r").read())

###############################################################
### Handle operator commands
###############################################################
def handle_op_commands(input: str) -> None:
    opcmd: str = input[4:].lower()

    # help
    if opcmd == "help":
        print_file("ophelp")
        return

    # map
    if opcmd == "map":
        show_map(maze)
        return

    # stats
    if opcmd == "stats":
        hero.print_stats()
        return

    # teleport
    pattern: str = "teleport (\d+) (\d+)"
    match = re.search(pattern, opcmd)
    if match is not None:
        row = int(match.group(1))
        col = int(match.group(2))
        maze.set_current_position(row, col)
        print("Teleported to " + str(row) + ", " + str(col))
        return

    # if nothing above was matched, it's junk.
    print("Operator command not recognised. You can type \/OP HELP for help with operator commands.")

###############################################################
### Main Program
###############################################################

hero: Character = Character("Thor", 4, 3, 8, True)
maze: Maze      = dungeon1.loadDungeon()

print_file("splash")

while True:

    # If there's a live monster here, you have to fight it first
    if maze.is_live_monster():
        print("A " + maze.get_monster().name + " has spotted you. You'll have to fight it!")
        monster = maze.get_monster()
        fight(hero, monster)

    # Now that the monsters are gone, if there's treasure, pick it up!
    if maze.is_treasure():
        print("You've found a " + maze.get_treasure().name)
        hero.treasure.append(maze.get_treasure())
        maze.remove_treasure()

    # Now let's show where we are.
    # If we've just defeated a monster, let's not mention the body.
    print(maze.describe_current_cell(False))

    # Read input
    action: str = input(">").lower()

    if action[0:3] == "/op":
        handle_op_commands(action)
    elif action in ["h", "help"]:
        print_file("help")
    elif action in ["n", "north"]:
        maze.go_north()
    elif action in ["e", "east"]:
        maze.go_east()
    elif action in ["s", "south"]:
        maze.go_south()
    elif action in ["w", "west"]:
        maze.go_west()
    elif action in ["q", "quit"]:
        print("The dungeon has beaten you this time.\n")
        break
    else:
        print("Sorry, I didn't understand that. You can type 'HELP' for a list of commands.")
