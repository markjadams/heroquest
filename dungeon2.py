from hqcell import Cell
from hqmaze import Maze
from hqchar import Character

def loadDungeon():

	maze = Maze()

	# Initialize rows - how many rows do you want?
	# One row already there
	#maze.rows.append([])
	maze.rows.append([])
	maze.rows.append([])
	maze.rows.append([])
	maze.rows.append([])
	maze.rows.append([])

	# Initialize each cell in each row with n, e, s, w

	# Row 0
	maze.rows[0].append(Cell(1, 1, 1, 1)) #0
	maze.rows[0].append(Cell(1, 1, 1, 1)) #1
	maze.rows[0].append(Cell(1, 1, 1, 1)) #2
	maze.rows[0].append(Cell(1, 1, 1, 1)) #3
	maze.rows[0].append(Cell(1, 1, 1, 1)) #4
	maze.rows[0].append(Cell(1, 1, 1, 1)) #5
	maze.rows[0].append(Cell(1, 1, 1, 1)) #6

	# Row 1
	maze.rows[1].append(Cell(1, 1, 1, 1)) #0
	maze.rows[1].append(Cell(1, 1, 1, 1)) #1
	maze.rows[1].append(Cell(1, 1, 1, 1)) #2
	maze.rows[1].append(Cell(1, 1, 1, 1)) #3
	maze.rows[1].append(Cell(1, 1, 1, 1)) #4
	maze.rows[1].append(Cell(1, 1, 1, 1)) #5
	maze.rows[1].append(Cell(1, 1, 1, 1)) #6

	# Row 2
	maze.rows[2].append(Cell(1, 1, 1, 1)) #0
	maze.rows[2].append(Cell(1, 1, 1, 1)) #1
	maze.rows[2].append(Cell(1, 1, 1, 1)) #2
	maze.rows[2].append(Cell(1, 1, 1, 1)) #3
	maze.rows[2].append(Cell(1, 1, 1, 1)) #4
	maze.rows[2].append(Cell(1, 1, 1, 1)) #5
	maze.rows[2].append(Cell(1, 1, 1, 1)) #6

	# Row 3
	maze.rows[3].append(Cell(1, 1, 1, 1)) #0
	maze.rows[3].append(Cell(1, 1, 1, 1)) #1
	maze.rows[3].append(Cell(1, 1, 1, 1)) #2
	maze.rows[3].append(Cell(1, 1, 1, 1)) #3
	maze.rows[3].append(Cell(1, 1, 1, 1)) #4
	maze.rows[3].append(Cell(1, 1, 1, 1)) #5
	maze.rows[3].append(Cell(1, 1, 1, 1)) #6

	# Row 4
	maze.rows[4].append(Cell(1, 1, 1, 1)) #0
	maze.rows[4].append(Cell(1, 1, 1, 1)) #1
	maze.rows[4].append(Cell(1, 1, 1, 1)) #2
	maze.rows[4].append(Cell(1, 1, 1, 1)) #3
	maze.rows[4].append(Cell(1, 1, 1, 1)) #4
	maze.rows[4].append(Cell(1, 1, 1, 1)) #5
	maze.rows[4].append(Cell(1, 1, 1, 1)) #6

	# Row 5
	maze.rows[5].append(Cell(1, 1, 1, 1)) #0
	maze.rows[5].append(Cell(1, 1, 1, 1)) #1
	maze.rows[5].append(Cell(1, 1, 1, 1)) #2
	maze.rows[5].append(Cell(1, 1, 1, 1)) #3
	maze.rows[5].append(Cell(1, 1, 1, 1)) #4
	maze.rows[5].append(Cell(1, 1, 1, 1)) #5
	maze.rows[5].append(Cell(1, 1, 1, 1)) #6

	# Row 6
	maze.rows[6].append(Cell(1, 1, 1, 1)) #0
	maze.rows[6].append(Cell(1, 1, 1, 1)) #1
	maze.rows[6].append(Cell(1, 1, 1, 1)) #2
	maze.rows[6].append(Cell(1, 1, 1, 1)) #3
	maze.rows[6].append(Cell(1, 1, 1, 1)) #4
	maze.rows[6].append(Cell(1, 1, 1, 1)) #5
	maze.rows[6].append(Cell(1, 1, 1, 1)) #6

	# Treasure Cells
	maze.rows[2][2].treasure = True

	# Monster Cells
	maze.rows[3][1].monster = Character("Goblin", 3, 1, 1, False)
	maze.rows[3][3].monster = Character("Goblin", 3, 1, 1, False)
	maze.rows[1][4].monster = Character("Goblin", 3, 1, 1, False)

	# Set Start Position
	maze.current_row = 4
	maze.current_col = 2

	return maze
