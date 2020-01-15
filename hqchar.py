#########################################
### Character                         ###
#########################################

class Character:
	def __init__(self, name, attack, defense, body, is_hero):
		self.name           = name
		self.attack         = attack
		self.defense        = defense
		self.body_remaining = body
		self.body_original  = body
		self.is_hero        = is_hero
		self.treasure       = []

	def format_name(self, capitalise=False):
		if self.is_hero:
			return self.name
		else:
			return ("The " if capitalise else "the ") + self.name

	def print_stats(self):
		print(" *** CHARACTER STATS ***")
		print(" Name: " + self.name)
		print(" Attack Dice:  " + str(self.attack))
		print(" Defence Dice: " + str(self.defense))
		print(" Body Points:  " + str(self.body_original) + " (" + str(self.body_remaining) + " remaining)")
		print(" Treasure:")
		if len(self.treasure) == 0:
			print("    (None)")
		for treasure in self.treasure:
			treasure_description = "    " + treasure.name + ": "
			if treasure.attack_bonus  > 0: treasure_description += "Attack Bonus: (+"  + str(treasure.attack_bonus ) + "), "
			if treasure.defense_bonus > 0: treasure_description += "Defense Bonus: (+" + str(treasure.defense_bonus) + "), "
			if treasure.value         > 0: treasure_description += "Value: "           + str(treasure.value) + " gold coins"
			print(treasure_description)

#########################################
### Set Characters                    ###
#########################################

barbarian = Character("Thor"  , 4, 3, 4, True )
goblin    = Character("goblin", 3, 3, 1, False)
zombie    = Character("zombie", 4, 3, 4, False)
devil     = Character("devil" , 5, 5, 5, False)
