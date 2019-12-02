import hqcore
import hqchar
import hqmap

#########################################
### Maze                              ###
#########################################

class Maze:

	def __init__(self):
		self.rows = [[]]
		self.row = 0
		self.col = 0
		self.debug = False

	def get_cell(row, col):
		return rows[x][y]

	def get_current_cell(self):
		return self.rows[self.row][self.col]

	def describe_current_cell(self):
		if self.is_monster (): return "There is a monster!"
		if self.is_treasure(): return "You've found some treasure!"

		message = ""
		directionCount = 0
		if self.can_go_north(): directionCount += 1
		if self.can_go_east (): directionCount += 1
		if self.can_go_south(): directionCount += 1
		if self.can_go_west (): directionCount += 1
		if directionCount == 1: message += "You've hit a dead end. "
		message += "You can go "
		if self.can_go_north(): message += "north, "
		if self.can_go_east (): message += "east, "
		if self.can_go_south(): message += "south, "
		if self.can_go_west (): message += "west, "
		message = message[0:len(message)-2] + "."
		return message

	def can_go_north(self): return self.get_current_cell().north
	def can_go_east (self): return self.get_current_cell().east
	def can_go_south(self): return self.get_current_cell().south
	def can_go_west (self): return self.get_current_cell().west
	def is_monster (self): return self.get_current_cell().monster != None
	def is_treasure(self): return self.get_current_cell().treasure

	def debug_on(self):
		self.debug = True

	def debug_off(self):
		self.debug = False

	def go_north(self):
		if self.can_go_north() == False:
			print("You cannot go north.")
			return
		self.row -= 1

	def go_east(self):
		if self.can_go_east() == False:
			print("You cannot go east.")
			return
		self.col += 1

	def go_south(self):
		if self.can_go_south() == False:
			print("You cannot go south.")
			return
		self.row += 1

	def go_west(self):
		if self.can_go_west() == False:
			print("You cannot go west.")
			return
		self.col -= 1

	def show_map(self):
		hqmap.show_map(self)
