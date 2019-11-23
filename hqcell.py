import hqcore

#########################################
### Cell                              ###
#########################################

class Cell:
	def __init__(self, north, east, south, west):
		self.north    = hqcore.intToBool(north)
		self.east     = hqcore.intToBool(east)
		self.south    = hqcore.intToBool(south)
		self.west     = hqcore.intToBool(west)
		self.monster  = None
		self.treasure = False

	def canGoNorth(self): return self.north
	def canGoEast (self): return self.east
	def canGoSouth(self): return self.south
	def canGoWest (self): return self.west
	def isMonster (self): return self.monster != None
	def isTreasure(self): return self.treasure

	def getMapRow1(self):
		return "..." + ("###" if self.north else "...") + "..."

	def getMapRow2(self):
		return ("###" if self.west else "...") + "###" + ("###" if self.east else "...")

	def getMapRow3(self):
		return "..." + ("###" if self.south else "...") + "..."
