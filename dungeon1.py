###############################################################
### Dungeon 1                                               ###
###############################################################

from hqcell import Cell
from hqmaze import Maze
from hqchar import Character
from hqtreasure import Treasure

def loadDungeon() -> Maze:

	maze: Maze = Maze()

	# One row already there
	#maze.rows.append([])
	maze.rows.append([])
	maze.rows.append([])
	maze.rows.append([])
	maze.rows.append([])

	maze.rows[0].append(Cell(0, 1, 1, 0))
	maze.rows[0].append(Cell(0, 1, 1, 1))
	maze.rows[0].append(Cell(0, 1, 0, 1))
	maze.rows[0].append(Cell(0, 1, 1, 1))
	maze.rows[0].append(Cell(0, 0, 1, 1))

	maze.rows[1].append(Cell(1, 0, 1, 0))
	maze.rows[1].append(Cell(1, 0, 1, 0))
	maze.rows[1].append(Cell(0, 1, 1, 0))
	maze.rows[1].append(Cell(1, 0, 0, 1))
	maze.rows[1].append(Cell(1, 0, 0, 0))

	maze.rows[2].append(Cell(1, 1, 0, 0))
	maze.rows[2].append(Cell(1, 0, 1, 1))
	maze.rows[2].append(Cell(1, 0, 0, 0))
	maze.rows[2].append(Cell(0, 1, 1, 0))
	maze.rows[2].append(Cell(0, 0, 1, 1))

	maze.rows[3].append(Cell(0, 0, 1, 0))
	maze.rows[3].append(Cell(1, 1, 0, 0))
	maze.rows[3].append(Cell(0, 0, 1, 1))
	maze.rows[3].append(Cell(1, 0, 0, 0))
	maze.rows[3].append(Cell(1, 0, 1, 0))

	maze.rows[4].append(Cell(1, 1, 0, 0))
	maze.rows[4].append(Cell(0, 1, 0, 1))
	maze.rows[4].append(Cell(1, 1, 0, 1))
	maze.rows[4].append(Cell(0, 1, 0, 1))
	maze.rows[4].append(Cell(1, 0, 0, 1))

	# Treasure Cells
	maze.get_cell(2, 2).treasure = Treasure("Gold Coins", 1, 0, 50)

	# Monster Cells
	maze.get_cell(3, 0).monster  = Character("goblin", 3, 1, 1, False)
	maze.get_cell(3, 3).monster  = Character("goblin", 3, 1, 1, False)
	maze.get_cell(1, 4).monster  = Character("goblin", 3, 1, 1, False)

	# Set Start Position
	maze.set_current_position(4, 2)

	return maze
