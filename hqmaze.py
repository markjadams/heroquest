import hqcore

#########################################
### Maze                              ###
#########################################

class Maze:

	def __init__(self):
		self.maze = [[]]
		self.row = 0
		self.col = 0
		self.debug = False

	def getCurrentSquare(self):
		return self.maze[self.row][self.col]

	def describeCurrentSquare(self):
		if self.isMonster (): return "There is a monster!"
		if self.isTreasure(): return "You've found some treasure!"

		message = ""
		directionCount = 0
		if self.canGoNorth(): directionCount += 1
		if self.canGoEast (): directionCount += 1
		if self.canGoSouth(): directionCount += 1
		if self.canGoWest (): directionCount += 1
		if directionCount == 1: message += "You've hit a dead end. "
		message += "You can go "
		if self.canGoNorth(): message += "north, "
		if self.canGoEast (): message += "east, "
		if self.canGoSouth(): message += "south, "
		if self.canGoWest (): message += "west, "
		message = message[0:len(message)-2] + "."
		return message

	def canGoNorth(self): return self.getCurrentSquare().canGoNorth()
	def canGoEast (self): return self.getCurrentSquare().canGoEast()
	def canGoSouth(self): return self.getCurrentSquare().canGoSouth()
	def canGoWest (self): return self.getCurrentSquare().canGoWest()
	def isMonster (self): return self.getCurrentSquare().isMonster()
	def isStart   (self): return self.getCurrentSquare().isStart()
	def isTreasure(self): return self.getCurrentSquare().isTreasure()

	def debugOn(self):
		self.debug = True

	def debugOff(self):
		self.debug = False

	def goNorth(self):
		if self.canGoNorth() == False:
			print("You cannot go north.")
			return
		self.row -= 1

	def goEast(self):
		if self.canGoEast() == False:
			print("You cannot go east.")
			return
		self.col += 1

	def goSouth(self):
		if self.canGoSouth() == False:
			print("You cannot go south.")
			return
		self.row += 1

	def goWest(self):
		if self.canGoWest() == False:
			print("You cannot go west.")
			return
		self.col -= 1

	def showMap(self):
		row = 0
		print()
		print("         0          1          2          3          4")
		while row < 5:
			line = "     "
			for square in self.maze[row]:
				line += square.getMapRow1() + "  "
			print(line)
			line = "  " + str(row) + "  "
			for square in self.maze[row]:
				line += square.getMapRow2() + "  "
			print(line)
			line = "     "
			for square in self.maze[row]:
				line += square.getMapRow3() + "  "
			print(line)
			print()
			row += 1

		print("You are currently at row " + str(self.row) + ", column " + str(self.col))

