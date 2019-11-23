#########################################
### Character                         ###
#########################################

class Character:
	def __init__(self, name, attack, defense, body, hero):
		self.name    = name
		self.attack  = attack
		self.defense = defense
		self.body    = body
		self.hero    = hero

# characters

barbarian = Character("Thor"  , 100, 1, 100, True )
goblin    = Character("Goblin", 100, 1, 100, False)
zombie    = Character("Zombie", 4, 3, 4, False)
devil     = Character("Devil" , 5, 5, 5, False)
