###############################################################
### Cell                                                    ###
###############################################################

from hqchar     import Character
from hqtreasure import Treasure

class Cell:

	###########################################################
	# Initialise class (bools are loaded as int 1/0)
	###########################################################

	def __init__(self, north: int, east: int, south: int, west: int):
		self.can_go_north: bool      = (north > 0)
		self.can_go_east : bool      = (east  > 0)
		self.can_go_south: bool      = (south > 0)
		self.can_go_west : bool      = (west  > 0)
		self.monster     : Character = None
		self.treasure    : Treasure  = None

	###########################################################
	# Is there a live monster in the current cell
	###########################################################

	def is_live_monster(self) -> bool:
		return self.monster is not None and self.monster.health_remaining > 0

	###########################################################
	# Is there a dead monster in the current cell
	###########################################################

	def is_dead_monster(self) -> bool:
		return self.monster is not None and self.monster.health_remaining <= 0

	###########################################################
	# Is there threasure in the current cell
	###########################################################

	def is_treasure(self) -> bool:
		return self.treasure is not None

