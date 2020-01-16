###############################################################
### Dungeon 1                                               ###
###############################################################

from hqcell     import Cell
from hqmaze     import Maze
from hqchar     import Character
from hqtreasure import Treasure

def loadDungeon() -> Maze:

	maze: Maze = Maze()

	# Initialize rows - how many rows do you want?
	# One row already there
	maze.rows.append([])
	maze.rows.append([])
	maze.rows.append([])
	maze.rows.append([])
	maze.rows.append([])
	maze.rows.append([])

	# Initialize each cell in each row with n, e, s, w

	# Row 0
	maze.rows[0].append(Cell(0, 1, 1, 0)) #0
	maze.rows[0].append(Cell(0, 0, 1, 1)) #1
	maze.rows[0].append(Cell(0, 1, 1, 0)) #2
	maze.rows[0].append(Cell(0, 1, 0, 1)) #3
	maze.rows[0].append(Cell(0, 1, 1, 1)) #4
	maze.rows[0].append(Cell(0, 1, 1, 1)) #5
	maze.rows[0].append(Cell(0, 0, 1, 1)) #6

	# Row 1
	maze.rows[1].append(Cell(1, 0, 1, 0)) #0
	maze.rows[1].append(Cell(1, 0, 0, 0)) #1
	maze.rows[1].append(Cell(1, 1, 1, 0)) #2
	maze.rows[1].append(Cell(0, 0, 1, 1)) #3
	maze.rows[1].append(Cell(1, 0, 1, 0)) #4
	maze.rows[1].append(Cell(1, 0, 1, 0)) #5
	maze.rows[1].append(Cell(1, 0, 1, 0)) #6

	# Row 2
	maze.rows[2].append(Cell(1, 1, 1, 0)) #0
	maze.rows[2].append(Cell(0, 0, 0, 1)) #1
	maze.rows[2].append(Cell(1, 0, 0, 0)) #2
	maze.rows[2].append(Cell(1, 0, 1, 0)) #3
	maze.rows[2].append(Cell(1, 0, 0, 0)) #4
	maze.rows[2].append(Cell(1, 0, 1, 0)) #5
	maze.rows[2].append(Cell(1, 0, 1, 0)) #6

	# Row 3
	maze.rows[3].append(Cell(1, 1, 0, 0)) #0
	maze.rows[3].append(Cell(0, 0, 1, 1)) #1
	maze.rows[3].append(Cell(0, 1, 0, 0)) #2
	maze.rows[3].append(Cell(1, 0, 0, 1)) #3
	maze.rows[3].append(Cell(0, 1, 1, 0)) #4
	maze.rows[3].append(Cell(1, 0, 0, 1)) #5
	maze.rows[3].append(Cell(1, 0, 0, 0)) #6

	# Row 4
	maze.rows[4].append(Cell(0, 1, 1, 0)) #0
	maze.rows[4].append(Cell(1, 1, 0, 1)) #1
	maze.rows[4].append(Cell(0, 1, 0, 1)) #2
	maze.rows[4].append(Cell(0, 0, 1, 1)) #3
	maze.rows[4].append(Cell(1, 1, 1, 0)) #4
	maze.rows[4].append(Cell(0, 1, 0, 1)) #5
	maze.rows[4].append(Cell(0, 0, 1, 1)) #6

	# Row 5
	maze.rows[5].append(Cell(1, 1, 1, 0)) #0
	maze.rows[5].append(Cell(0, 0, 0, 1)) #1
	maze.rows[5].append(Cell(0, 0, 1, 0)) #2
	maze.rows[5].append(Cell(1, 0, 1, 0)) #3
	maze.rows[5].append(Cell(1, 1, 0, 0)) #4
	maze.rows[5].append(Cell(0, 0, 0, 1)) #5
	maze.rows[5].append(Cell(1, 0, 1, 0)) #6

	# Row 6
	maze.rows[6].append(Cell(1, 1, 0, 0)) #0
	maze.rows[6].append(Cell(0, 1, 0, 1)) #1
	maze.rows[6].append(Cell(1, 0, 0, 1)) #2
	maze.rows[6].append(Cell(1, 1, 0, 0)) #3
	maze.rows[6].append(Cell(0, 1, 0, 1)) #4
	maze.rows[6].append(Cell(0, 1, 0, 1)) #5
	maze.rows[6].append(Cell(1, 0, 0, 1)) #6

	# Treasure Cells
	maze.get_cell(1, 1).treasure = Treasure("Shield    "   , 0, 1, 100)
	maze.get_cell(5, 2).treasure = Treasure("Long Sword"   , 1, 0, 100)
	maze.get_cell(5, 1).treasure = Treasure("Gold Coins"   , 1, 0,  50)
	maze.get_cell(5, 5).treasure = Treasure("Helmet"       , 0, 1, 100)
	maze.get_cell(2, 4).treasure = Treasure("Magical Sword", 2, 0, 500)

	# Monster Cells
	maze.get_cell(0, 4).monster = Character("evil wizard", 6, 2, 2, False)
	maze.get_cell(1, 1).monster = Character("goblin"     , 3, 1, 1, False)
	maze.get_cell(2, 2).monster = Character("devil"      , 5, 4, 4, False)
	maze.get_cell(3, 2).monster = Character("mummy"      , 3, 3, 3, False)
	maze.get_cell(3, 6).monster = Character("ogre"       , 3, 2, 2, False)
	maze.get_cell(4, 0).monster = Character("goblin"     , 3, 1, 1, False)
	maze.get_cell(5, 1).monster = Character("dark elf"   , 4, 2, 2, False)
	maze.get_cell(5, 2).monster = Character("troll"      , 3, 4, 4, False)
	maze.get_cell(5, 5).monster = Character("zombie"     , 3, 4, 4, False)

	# Set Start Position
	maze.set_current_position(2, 1)

	return maze
