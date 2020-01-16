###############################################################
### Dungeon 1                                               ###
###############################################################

from hqcell     import Cell
from hqmaze     import Maze
from hqchar     import Character
from hqtreasure import Treasure
from hqbuilder  import get_treasure
from hqbuilder  import get_monster

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
	maze.get_cell(1, 1).treasure = get_treasure("Shield")
	maze.get_cell(5, 2).treasure = get_treasure("long_sword")
	maze.get_cell(5, 1).treasure = get_treasure("gold_cooins")
	maze.get_cell(5, 5).treasure = get_treasure("helmet")
	maze.get_cell(2, 4).treasure = get_treasure("glamdring")

	# Monster Cells
	maze.get_cell(0, 4).monster = get_monster("evil_wizard")
	maze.get_cell(1, 1).monster = get_monster("goblin")
	maze.get_cell(2, 2).monster = get_monster("devil")
	maze.get_cell(3, 2).monster = get_monster("mummy")
	maze.get_cell(3, 6).monster = get_monster("ogre")
	maze.get_cell(4, 0).monster = get_monster("goblin")
	maze.get_cell(5, 1).monster = get_monster("dark_elf")
	maze.get_cell(5, 2).monster = get_monster("troll")
	maze.get_cell(5, 5).monster = get_monster("zombie")

	# Set Start Position
	maze.set_current_position(2, 1)

	return maze
