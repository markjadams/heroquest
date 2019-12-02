#########################################
### Core                              ###
#########################################

# library imports
import random

def roll_dice():
    return random.randint(1, 6)

def int_to_bool(oneZero):
    return True if oneZero == 1 else False

def bool_to_str(val):
    return "X" if val == True else "."

def print_file(file):
    print(open("txt\\" + file + ".txt", "r").read())
