import hqcell
import hqmaze

def get_map_row_1(cell):
    return "###" + ("   " if cell.north else "###") + "###"

def get_map_row_2(cell, is_current_cell=False):
    str = "   " if cell.west else "###"
    if is_current_cell:
        str += " H "
    elif cell.monster != None:
        str += " M "
    elif cell.treasure == True:
        str += " T "
    else:
        str += "   "
    str += "   " if cell.east else "###"
    return str

def get_map_row_3(cell):
    return "###" + ("   " if cell.south else "###") + "###"

def show_map(maze):

    # column header
    colHeader = "\n "
    for col in range(len(maze.rows[0])):
        colHeader += "        " + str(col)
    print(colHeader)

    for row in range(len(maze.rows)):
        line = "     "
        #for cell in maze.rows[row]:
        #    line += get_map_row_1(cell)
        for col in range(len(maze.rows[row])):
            line += get_map_row_1(maze.rows[row][col])
        print(line)
        line = "  " + str(row) + "  "
        #for cell in maze.rows[row]:
        #    line += get_map_row_2(cell)
        for col in range(len(maze.rows[row])):
            line += get_map_row_2(maze.rows[row][col], (row == maze.current_row and col == maze.current_col))
        print(line)
        line = "     "
        #for cell in maze.rows[row]:
        #    line += get_map_row_3(cell)
        for col in range(len(maze.rows[row])):
            line += get_map_row_3(maze.rows[row][col])
        print(line)
        print(line)

    #print("You are currently at row " + str(maze.current_row) + ", column " + str(maze.current_col))
    print()
