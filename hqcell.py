import hqcore

#########################################
### Cell                              ###
#########################################

class Cell:

	###########################################################
	# Initialise class
	###########################################################
	def __init__(self, north, east, south, west):
		self.north    = hqcore.int_to_bool(north)
		self.east     = hqcore.int_to_bool(east)
		self.south    = hqcore.int_to_bool(south)
		self.west     = hqcore.int_to_bool(west)
		self.monster  = None
		self.treasure = False

	###########################################################
	# Is there a live monster here
	###########################################################
	def is_live_monster(self):
		return self.monster is not None and self.monster.body > 0

	###########################################################
	# Is there a dead monster here
	###########################################################
	def is_dead_monster(self):
		return self.monster is not None and self.monster.body <= 0

	###########################################################
	# Is there a dead monster here
	###########################################################
	def is_treasure(self):
		return self.treasure
