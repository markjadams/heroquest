###############################################################
### Map                                                     ###
###############################################################

from hqcell import Cell
from hqmaze import Maze

###############################################################
### Build map row 1 of 3                                    ###
###############################################################

def get_map_row_1(cell: Cell) -> str:
    return "###" + ("   " if cell.can_go_north else "###") + "###"

###############################################################
### Build map row 2 of 3                                    ###
###############################################################

def get_map_row_2(cell: Cell, is_current_cell: bool = False) -> str:
    str = "   " if cell.can_go_west else "###"
    if is_current_cell:
        str += " H "
    elif cell.is_treasure():
        str += " T "
    elif cell.is_live_monster():
        str += " M "
    else:
        str += "   "
    str += "   " if cell.can_go_east else "###"
    return str

###############################################################
### Build map row 3 of 3                                    ###
###############################################################

def get_map_row_3(cell: Cell) -> str:
    return "###" + ("   " if cell.can_go_south else "###") + "###"

###############################################################
### Print the map                                           ###
###############################################################

def show_map(maze: Maze):

    # column headers
    colHeader = "\n "
    for col in range(len(maze.rows[0])):
        colHeader += "        " + str(col)
    print(colHeader)

    # iterate rows and columns
    for row in range(len(maze.rows)):
        line = "     "
        for col in range(len(maze.rows[row])):
            line += get_map_row_1(maze.get_cell(row, col))
        print(line)
        line = "  " + str(row) + "  "
        for col in range(len(maze.rows[row])):
            line += get_map_row_2(maze.get_cell(row, col), (row == maze.get_current_row() and col == maze.get_current_col()))
        print(line)
        line = "     "
        for col in range(len(maze.rows[row])):
            line += get_map_row_3(maze.rows[row][col])
        print(line)
        print(line)

    # print an empty line
    print()
