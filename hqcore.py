#########################################
### Core                              ###
#########################################

# library imports
#import random

### Moved to combat
#def roll_dice():
#    return random.randint(1, 6)

## deprecated in favour of simple inline (> 0) check
#def int_to_bool(oneZero):
#    return True if oneZero == 1 else False

# No longer used? wrapped in map
#def bool_to_str(val):
#    return "X" if val == True else "."

# Moved to heroquest.py
#def print_file(file):
#    print(open("txt\\" + file + ".txt", "r").read())

### deprecated, using "health" rather than "body points"
#def points_to_str(points, points_name=""):
#    return str(points) + " " + points_name + ("" if points_name == "" else " ") + "point" + ("" if points == 1 else "s")
