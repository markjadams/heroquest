import hqcell
import hqmaze

def get_map_row_1(cell):
    return "###" + ("   " if cell.north else "###") + "###"

def get_map_row_2(cell):
    str = "   " if cell.west else "###"
    if cell.monster != None:
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

    for row in range(len(maze.rows) - 1):
        line = "     "
        for cell in maze.rows[row]:
            line += get_map_row_1(cell)
        print(line)
        line = "  " + str(row) + "  "
        for cell in maze.rows[row]:
            line += get_map_row_2(cell)
        print(line)
        line = "     "
        for cell in maze.rows[row]:
            line += get_map_row_3(cell)
        print(line)

    print("You are currently at row " + str(maze.row) + ", column " + str(maze.col))
    print()
