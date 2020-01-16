###############################################################
### Character                                               ###
###############################################################

from typing     import List
from hqtreasure import Treasure

class Character:

	###########################################################
	# Initialise class
	###########################################################

	def __init__(self, name: str, attack: int, defense: int, health: int, is_hero: bool):
		self.name            : str            = name
		self.attack          : int            = attack
		self.defense         : int            = defense
		self.health_original : int            = health
		self.health_remaining: int            = health
		self.is_hero         : bool           = is_hero
		self.treasure        : List[Treasure] = []

	#######################################################
	# Format monster names
	###########################################################

	def format_name(self, capitalise: bool = False) -> str:
		if self.is_hero:
			return self.name
		else:
			return ("The " if capitalise else "the ") + self.name

	###########################################################
	# Get total attack including best weapon
	###########################################################

	def get_attack_with_bonus(self) -> int:
		bonus = 0
		for item in self.treasure:
			if item.attack_bonus > bonus: bonus = item.attack_bonus
		return self.attack + bonus

	###########################################################
	# Get total attack including total defense
	###########################################################

	def get_defense_with_bonus(self) -> int:
		bonus = 0
		for item in self.treasure:
			bonus += item.defense_bonus
		return self.defense + bonus

	###########################################################
	# Print character stats
	###########################################################

	def print_stats(self):
		print()

		print(" *******************************************************")
		print(" *** Character Stats for " + self.name)
		print(" *******************************************************")
		print(" *** Attack  : " + str(self.attack ) + " (" + str(self.get_attack_with_bonus() ) + " including bonuses)")
		print(" *** Defence : " + str(self.defense) + " (" + str(self.get_defense_with_bonus()) + " including bonuses)")
		print(" *** Health  : " + str(self.health_original) + " (" + str(self.health_remaining) + " remaining)")
		print(" *** Treasure:")
		if len(self.treasure) == 0:
			print(" ***    (None)")
		for treasure in self.treasure:
			treasure_description = " ***    " + treasure.name + ": "
			if treasure.attack_bonus  > 0: treasure_description += "Attack Bonus (+"  + str(treasure.attack_bonus ) + "), "
			if treasure.defense_bonus > 0: treasure_description += "Defense Bonus (+" + str(treasure.defense_bonus) + "), "
			if treasure.value         > 0: treasure_description += "Value: "          + str(treasure.value)         + " gold coins"
			print(treasure_description)
		print(" *******************************************************")
