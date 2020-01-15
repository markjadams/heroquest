# # project imports
import hqcore
import hqchar
import hqcombat
import hqmaze
import hqgame
import dungeon1
import dungeon2

from hqcore import print_file

######################################################
### Handle operator commands
######################################################
def handle_op_commands(input):
    opcmd = input[4:].lower()

    if opcmd == "help":
        print_file("ophelp")
    elif opcmd == "map":
        maze.show_map()
    elif opcmd == "stats":
        hero.print_stats()
    elif action == "/op debug on":
        maze.debug_on()
    elif action == "/op debug off":
        maze.debug_off()
    else:
        print("Operator command not recognised. Enter \/OP HELP for help with operator commands.")

######################################################
### Main Program
######################################################
hero = hqchar.Character("Thor", 4, 3, 8, True)
maze = dungeon2.loadDungeon()

print_file("splash")

while True:

    # If there's a live monster here, you have to fight it first
    if maze.get_current_cell().is_live_monster():
        print("A " + maze.get_current_cell().monster.name + " has spotted you. You'll have to fight it!")
        monster = maze.get_current_cell().monster
        hqcombat.fight(hero, monster)

    # Now that the monsters are gone, if there's treasure, pick it up!
    if maze.get_current_cell().treasure is not None:
        print("You've found a " + maze.get_current_cell().treasure.name)
        hero.treasure.append(maze.get_current_cell().treasure)
        maze.get_current_cell().treasure = None

    # Now let's show where we are.
    # If we've just defeated a monster, let's not mention the body.
    print(maze.describe_current_cell(False))

    # Read input
    action = input(">").lower()

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
