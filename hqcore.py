#########################################
### Core                              ###
#########################################

# library imports
import random

def rollDice():
	return random.randint(1, 6)

def intToBool(oneZero):
	return True if oneZero == 1 else False

def boolToStr(val):
	return "X" if val == True else "."
