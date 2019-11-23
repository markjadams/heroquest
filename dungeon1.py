from hqcell import Cell
from hqmaze import Maze

def loadDungeon():

	maze = Maze()

	maze.maze.append([])
	maze.maze.append([])
	maze.maze.append([])
	maze.maze.append([])
	maze.maze.append([])

	maze.maze[0].append(Cell(0, 1, 1, 0))
	maze.maze[0].append(Cell(0, 1, 1, 1))
	maze.maze[0].append(Cell(0, 1, 0, 1))
	maze.maze[0].append(Cell(0, 1, 1, 1))
	maze.maze[0].append(Cell(0, 0, 1, 1))

	maze.maze[1].append(Cell(1, 0, 1, 0))
	maze.maze[1].append(Cell(1, 0, 1, 0))
	maze.maze[1].append(Cell(0, 1, 1, 0))
	maze.maze[1].append(Cell(1, 0, 0, 1))
	maze.maze[1].append(Cell(1, 0, 0, 0))

	maze.maze[2].append(Cell(1, 1, 0, 0))
	maze.maze[2].append(Cell(1, 0, 1, 1))
	maze.maze[2].append(Cell(1, 0, 0, 0))
	maze.maze[2].append(Cell(0, 1, 1, 0))
	maze.maze[2].append(Cell(0, 0, 1, 1))

	maze.maze[3].append(Cell(0, 0, 1, 0))
	maze.maze[3].append(Cell(1, 1, 0, 0))
	maze.maze[3].append(Cell(0, 0, 1, 1))
	maze.maze[3].append(Cell(1, 0, 0, 0))
	maze.maze[3].append(Cell(1, 0, 1, 0))

	maze.maze[4].append(Cell(1, 1, 0, 0))
	maze.maze[4].append(Cell(0, 1, 0, 1))
	maze.maze[4].append(Cell(1, 1, 0, 1))
	maze.maze[4].append(Cell(0, 1, 0, 1))
	maze.maze[4].append(Cell(1, 0, 0, 1))

	# set additional cell attributes
	maze.maze[4][2].start    = True
	maze.maze[2][2].treasure = True
	maze.maze[3][0].monster  = True
	maze.maze[3][3].monster  = True
	maze.maze[1][4].monster  = True

	#start position
	maze.row = 4
	maze.col = 2

	return maze
