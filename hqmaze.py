###############################################################
### Maze                                                    ###
###############################################################

#import hqcore
from hqchar     import Character
from hqtreasure import Treasure
from hqcell     import Cell

class Maze:

	###########################################################
	# Initialise class
	###########################################################

	def __init__(self):
		self.rows = [[]]
		self.__current_row: int = 0
		self.__current_col: int = 0

	###########################################################
	# Get row count
	###########################################################

	def get_row_count(self) -> int:
		return len(rows)

	###########################################################
	# Get column count
	###########################################################

	def get_col_count(self) -> int:
		return len(rows[0])

	###########################################################
	# Get cell
	###########################################################

	def get_cell(self, row: int, col: int) -> Cell:
		return self.rows[row][col]

	###########################################################
	# Set current position (start or teleport)
	###########################################################

	def set_current_position(self, row: int, col: int) -> None:
		self.__current_row = row
		self.__current_col = col

	###########################################################
	# Get current row
	###########################################################

	def get_current_row(self) -> int:
		return self.__current_row

	###########################################################
	# Get current col
	###########################################################

	def get_current_col(self) -> int:
		return self.__current_col

	###########################################################
	# Get current cell
	###########################################################

	def get_current_cell(self) -> Cell:
		return self.get_cell(self.__current_row, self.__current_col)

	###########################################################
	# Can go north in the current cell
	###########################################################

	def can_go_north(self) -> bool:
		return self.get_current_cell().can_go_north

	###########################################################
	# Can go east in the current cell
	###########################################################

	def can_go_east(self) -> bool:
		return self.get_current_cell().can_go_east

	###########################################################
	# Can go south in the current cell
	###########################################################

	def can_go_south(self) -> bool:
		return self.get_current_cell().can_go_south

	###########################################################
	# Can go west in the current cell
	###########################################################

	def can_go_west(self) -> bool:
		return self.get_current_cell().can_go_west

	###########################################################
	# Is there a live monster in the current cell
	###########################################################

	def is_live_monster(self) -> bool:
		cell = self.get_current_cell()
		return cell.monster is not None and cell.monster.health_remaining > 0

	###########################################################
	# Is there a dead monster in the current cell
	###########################################################

	def is_dead_monster(self) -> bool:
		cell = self.get_current_cell()
		return cell.monster is not None and cell.monster.health_remaining <= 0

	###########################################################
	# Get monster in the current cell
	###########################################################

	def get_monster(self) -> Treasure:
		return self.get_current_cell().monster

	###########################################################
	# Is there threasure in the current cell
	###########################################################

	def is_treasure(self) -> bool:
		return self.get_current_cell().treasure is not None

	###########################################################
	# Get treasure in the current cell
	###########################################################

	def get_treasure(self) -> Treasure:
		return self.get_current_cell().treasure

	###########################################################
	# Pickup (remove) treasure in the current cell
	###########################################################

	def remove_treasure(self) -> None:
		self.get_current_cell().treasure = None

	###########################################################
	# Describe the current cell
	###########################################################

	def describe_current_cell(self, include_dead_monsters: bool) -> str:
		if self.is_treasure():
			print("Congratulations! You've found the treasure.")

		# if there is a dead monster here, mention it
		if include_dead_monsters and self.is_dead_monster():
			print("There is a dead " + self.get_monster().name + " here. You must have been here before.")

		if self.is_dead_end():
			print("You're in a dead end.")

		message = "You can go "
		if self.can_go_north(): message += "north, "
		if self.can_go_east() : message += "east, "
		if self.can_go_south(): message += "south, "
		if self.can_go_west() : message += "west, "
		message = message[0:len(message)-2] + "."

		return message

	###########################################################
	# Is this a dead end with only one direction available
	###########################################################

	def is_dead_end(self) -> bool:
		return \
			(1 if self.can_go_north() else 0) + \
			(1 if self.can_go_east()  else 0) + \
			(1 if self.can_go_south() else 0) + \
			(1 if self.can_go_west()  else 0) == 1

	###########################################################
	# Go north
	###########################################################

	def go_north(self) -> None:
		if self.can_go_north() == False:
			print("You cannot go north.")
			return
		self.__current_row -= 1

	###########################################################
	# Go east
	###########################################################

	def go_east(self) -> None:
		if self.can_go_east() == False:
			print("You cannot go east.")
			return
		self.__current_col += 1

	###########################################################
	# Go south
	###########################################################

	def go_south(self) -> None:
		if self.can_go_south() == False:
			print("You cannot go south.")
			return
		self.__current_row += 1

	###########################################################
	# Go west
	###########################################################

	def go_west(self) -> None:
		if self.can_go_west() == False:
			print("You cannot go west.")
			return
		self.__current_col -= 1
