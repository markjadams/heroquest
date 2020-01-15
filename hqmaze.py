import hqcore
import hqchar
import hqmap

###############################################################
### Maze                                                    ###
###############################################################

class Maze:

	###########################################################
	# Initialise class
	###########################################################
	def __init__(self):
		self.rows = [[]]
		self.current_row = 0
		self.current_col = 0
		self.debug = False

	###########################################################
	# Get cell
	###########################################################
	def get_cell(row, col):
		return rows[x][y]

	###########################################################
	# Get current cell
	###########################################################
	def get_current_cell(self):
		return self.rows[self.current_row][self.current_col]

	###########################################################
	# Describe current cell
	###########################################################
	def describe_current_cell(self, include_dead_monsters):
		if self.get_current_cell().is_treasure():
			print("Congratulations! You've found the treasure.")

		# if there is a dead monster here, mention it
		if include_dead_monsters and self.get_current_cell().is_dead_monster():
			print("There is a dead " + self.get_current_cell().monster.name + " here. You must have been here before.")

		if self.is_dead_end():
			print("You're in a dead end.")

		message = "You can go "
		if self.get_current_cell().north: message += "north, "
		if self.get_current_cell().east : message += "east, "
		if self.get_current_cell().south: message += "south, "
		if self.get_current_cell().west : message += "west, "
		message = message[0:len(message)-2] + "."

		return message

	###########################################################
	# Is this a dead end with only one direction available
	###########################################################
	def is_dead_end(self):
		return \
			(1 if self.get_current_cell().north else 0) + \
			(1 if self.get_current_cell().east  else 0) + \
			(1 if self.get_current_cell().south else 0) + \
			(1 if self.get_current_cell().west  else 0) == 1

	###########################################################
	# Go north
	###########################################################
	def go_north(self):
		if self.get_current_cell().north == False:
			print("You cannot go north.")
			return
		self.current_row -= 1

	###########################################################
	# Go east
	###########################################################
	def go_east(self):
		if self.get_current_cell().east == False:
			print("You cannot go east.")
			return
		self.current_col += 1

	###########################################################
	# Go south
	###########################################################
	def go_south(self):
		if self.get_current_cell().south == False:
			print("You cannot go south.")
			return
		self.current_row += 1

	###########################################################
	# Go west
	###########################################################
	def go_west(self):
		if self.get_current_cell().west == False:
			print("You cannot go west.")
			return
		self.current_col -= 1

	###########################################################
	# Show map
	###########################################################
	def show_map(self):
		hqmap.show_map(self)
