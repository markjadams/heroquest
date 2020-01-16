###############################################################
### Dungeon 1                                               ###
###############################################################

from hqcell import Cell
from hqmaze import Maze
from hqchar import Character
from hqtreasure import Treasure

from hqbuilder import get_monster
from hqbuilder import get_treasure

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
	maze.get_cell(2, 2).treasure = get_treasure("gold_coins")

	# Monster Cells
	maze.get_cell(3, 0).monster  = get_monster("goblin")
	maze.get_cell(3, 3).monster  = get_monster("goblin")
	maze.get_cell(1, 4).monster  = get_monster("goblin")

	# Set Start Position
	maze.set_current_position(4, 2)

	return maze
