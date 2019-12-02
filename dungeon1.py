from hqcell import Cell
from hqmaze import Maze
from hqchar import Character

def loadDungeon():

	maze = Maze()

	maze.rows.append([])
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

	# set additional cell attributes
	maze.rows[4][2].start    = True
	maze.rows[2][2].treasure = True
	maze.rows[3][0].monster  = Character("Goblin", 3, 1, 1, False)
	maze.rows[3][3].monster  = Character("Goblin", 3, 1, 1, False)
	maze.rows[1][4].monster  = Character("Goblin", 3, 1, 1, False)

	#start position
	maze.row = 4
	maze.col = 2

	return maze
