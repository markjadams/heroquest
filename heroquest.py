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
    elif action == "/op debug on":
        maze.debug_on()
    elif action == "/op debug off":
        maze.debug_off()
    else:
        print("Operator command not recognised. Enter \/OP HELP for help with operator commands.")

######################################################
### Main Program
######################################################

hero = hqchar.Character("Thor", 4, 3, 8, True )
maze = dungeon1.loadDungeon()

print_file("splash")

while True:

    print(maze.describe_current_cell())

    if maze.is_monster():
        monster = maze.get_current_cell().monster
        if monster.body == 0:
            print("there is a dead " + monster.name + " here.")
        hqcombat.fight(hero, monster)
        continue

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
        print("Command not recognised. Enter HELP for help with commands.")
