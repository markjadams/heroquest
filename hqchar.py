#########################################
### Character                         ###
#########################################

class Character:
	def __init__(self, name, attack, defense, body, is_hero):
		self.name    = name
		self.attack  = attack
		self.defense = defense
		self.body    = body
		self.is_hero = is_hero

	def format_name(self, capitalise=False):
		if self.is_hero:
			return self.name
		else:
			return ("The " if capitalise else "the ") + self.name

#########################################
### Set Characters                    ###
#########################################

barbarian = Character("Thor"  , 4, 3, 4, True )
goblin    = Character("goblin", 3, 3, 1, False)
zombie    = Character("zombie", 4, 3, 4, False)
devil     = Character("devil" , 5, 5, 5, False)
