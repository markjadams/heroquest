import hqcore

#########################################
### Cell                              ###
#########################################

class Cell:
	def __init__(self, north, east, south, west):
		self.north    = hqcore.int_to_bool(north)
		self.east     = hqcore.int_to_bool(east)
		self.south    = hqcore.int_to_bool(south)
		self.west     = hqcore.int_to_bool(west)
		self.monster  = None
		self.treasure = False

	#def can_go_north(self): return self.north
	#def can_go_east (self): return self.east
	#def can_go_south(self): return self.south
	#def can_go_west (self): return self.west
	#def is_monster (self): return self.monster != None
	#def is_treasure(self): return self.treasure

