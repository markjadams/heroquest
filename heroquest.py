# # project imports
import hqcore
import hqchar
import hqcombat
import hqmaze
import hqgame
import dungeon1
import dungeon2

######################################################
### showOpHelp
######################################################

def showOpHelp():
	print("Operator (op) commands can be used to check player status and change game configuration options.")
	print()
	print("DEBUG Displays a summary of operator commands")
	print("      arguments: on|off")
	print("HELP  Displays a summary of operator commands")
	print("MAP   Displays a map of the current dungeon")
	print("MOVE  Moves the player to the specified location in the current dungeon")
	print("      arguments: row col")
	print()
	

######################################################
### handleOpCommands
######################################################

def handleOpCommands(input):
	opcmd = input[4:].lower()
	print("Op Command = '" + opcmd + "'")

	if opcmd == "help":
		showOpHelp()
		return

	if opcmd == "map":
		maze.showMap()
		return

	if action == "/op debug on":
		maze.debugOn()
		return

	if action == "/op debug off":
		maze.debugOff()
		return

	print("Operator command not recognised.")

######################################################
### Show splash screen
######################################################

def splashScreen():
	print()
	print("***************************************************")
	print("***             WELCOME TO HEROQUEST            ***")
	print("***************************************************")
	print()
	print("You are entering the dungeon...")

######################################################
### Fight a monster
######################################################

def fight(monster):
	hqcombat.fight(hero, monster)
	if hero.body == 0:
		print("You were defeated by " + monster.name)
		exit
	if monster.body == 0:
		print("You defeated " + monster.name)

######################################################
### Main Program
######################################################

hero = hqchar.Character("Thor", 4, 3, 8, True )
maze = dungeon2.loadDungeon()

splashScreen()

while True:
	print(maze.describeCurrentSquare())

	if maze.isMonster():
		monster = maze.getCurrentSquare().monster
		if monster.body == 0:
			print("there is a dead " + monster.name + " here.")
		fight(monster)
		continue

	action = input(">").lower()

	if action[0:3] == "/op":
		handleOpCommands(action)
		continue

	if action == "n":
		maze.goNorth()
		continue

	if action == "e":
		maze.goEast()
		continue

	if action == "s":
		maze.goSouth()
		continue

	if action == "w":
		maze.goWest()
		continue

	if action == "q" or action == "quit":
		print("The dungeon has beaten you this time.\n")
		break

	print("Command not recognised. Press 'n' to go north, 'e' to go east, , 's' to go south, 'w' to go west, 'q' to quit.")
