from hqcell import Cell
from hqmaze import Maze
from hqchar import Character

def loadDungeon():

	maze = Maze()

	# Initialize rows - how many rows do you want?
	maze.maze.append([])
	maze.maze.append([])
	maze.maze.append([])
	maze.maze.append([])
	maze.maze.append([])
	maze.maze.append([])

	# Initialize each cell in each row with n, e, s, w

	# Row 0
	maze.maze[0].append(Cell(1, 1, 1, 1)) #0
	maze.maze[0].append(Cell(1, 1, 1, 1)) #1
	maze.maze[0].append(Cell(1, 1, 1, 1)) #2
	maze.maze[0].append(Cell(1, 1, 1, 1)) #3
	maze.maze[0].append(Cell(1, 1, 1, 1)) #4
	maze.maze[0].append(Cell(1, 1, 1, 1)) #5
	maze.maze[0].append(Cell(1, 1, 1, 1)) #6

	# Row 1
	maze.maze[1].append(Cell(1, 1, 1, 1)) #0
	maze.maze[1].append(Cell(1, 1, 1, 1)) #1
	maze.maze[1].append(Cell(1, 1, 1, 1)) #2
	maze.maze[1].append(Cell(1, 1, 1, 1)) #3
	maze.maze[1].append(Cell(1, 1, 1, 1)) #4
	maze.maze[1].append(Cell(1, 1, 1, 1)) #5
	maze.maze[1].append(Cell(1, 1, 1, 1)) #6

	# Row 2
	maze.maze[2].append(Cell(1, 1, 1, 1)) #0
	maze.maze[2].append(Cell(1, 1, 1, 1)) #1
	maze.maze[2].append(Cell(1, 1, 1, 1)) #2
	maze.maze[2].append(Cell(1, 1, 1, 1)) #3
	maze.maze[2].append(Cell(1, 1, 1, 1)) #4
	maze.maze[2].append(Cell(1, 1, 1, 1)) #5
	maze.maze[2].append(Cell(1, 1, 1, 1)) #6

	# Row 3
	maze.maze[3].append(Cell(1, 1, 1, 1)) #0
	maze.maze[3].append(Cell(1, 1, 1, 1)) #1
	maze.maze[3].append(Cell(1, 1, 1, 1)) #2
	maze.maze[3].append(Cell(1, 1, 1, 1)) #3
	maze.maze[3].append(Cell(1, 1, 1, 1)) #4
	maze.maze[3].append(Cell(1, 1, 1, 1)) #5
	maze.maze[3].append(Cell(1, 1, 1, 1)) #6

	# Row 4
	maze.maze[4].append(Cell(1, 1, 1, 1)) #0
	maze.maze[4].append(Cell(1, 1, 1, 1)) #1
	maze.maze[4].append(Cell(1, 1, 1, 1)) #2
	maze.maze[4].append(Cell(1, 1, 1, 1)) #3
	maze.maze[4].append(Cell(1, 1, 1, 1)) #4
	maze.maze[4].append(Cell(1, 1, 1, 1)) #5
	maze.maze[4].append(Cell(1, 1, 1, 1)) #6

	# Row 5
	maze.maze[5].append(Cell(1, 1, 1, 1)) #0
	maze.maze[5].append(Cell(1, 1, 1, 1)) #1
	maze.maze[5].append(Cell(1, 1, 1, 1)) #2
	maze.maze[5].append(Cell(1, 1, 1, 1)) #3
	maze.maze[5].append(Cell(1, 1, 1, 1)) #4
	maze.maze[5].append(Cell(1, 1, 1, 1)) #5
	maze.maze[5].append(Cell(1, 1, 1, 1)) #6

	# Row 6
	maze.maze[6].append(Cell(1, 1, 1, 1)) #0
	maze.maze[6].append(Cell(1, 1, 1, 1)) #1
	maze.maze[6].append(Cell(1, 1, 1, 1)) #2
	maze.maze[6].append(Cell(1, 1, 1, 1)) #3
	maze.maze[6].append(Cell(1, 1, 1, 1)) #4
	maze.maze[6].append(Cell(1, 1, 1, 1)) #5
	maze.maze[6].append(Cell(1, 1, 1, 1)) #6

	# Treasure Cells
	maze.maze[2][2].treasure = True

	# Monster Cells
	maze.maze[3][1].monster = Character("Goblin", 3, 1, 1, False)
	maze.maze[3][3].monster = Character("Goblin", 3, 1, 1, False)
	maze.maze[1][4].monster = Character("Goblin", 3, 1, 1, False)

	# Set Start Position
	maze.row = 4
	maze.col = 2

	return maze
