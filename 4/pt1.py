def up(row, column, inputs):
    word = ""
    word += inputs[row][column] + inputs[row-1][column] + inputs[row-2][column] + inputs[row-3][column]
    if word.upper() == "XMAS":
        return 1
    return 0


def down(row, column, inputs):
    word = ""
    word += inputs[row][column] + inputs[row+1][column] + inputs[row+2][column] + inputs[row+3][column]
    if word.upper() == "XMAS":
        return 1
    return 0

def left(row, column, inputs):
    word = ""
    word += inputs[row][column] + inputs[row][column-1] + inputs[row][column-2] + inputs[row][column-3]
    if word.upper() == "XMAS":
        return 1
    return 0

def right(row, column, inputs):
    word = ""
    word += inputs[row][column] + inputs[row][column+1] + inputs[row][column+2] + inputs[row][column+3]
    if word.upper() == "XMAS":
        return 1
    return 0

def diagonal_lu(row, column, inputs):
    word = ""
    word += inputs[row][column] + inputs[row-1][column-1] + inputs[row-2][column-2] + inputs[row-3][column-3]
    if word.upper() == "XMAS":
        return 1
    return 0

def diagonal_ru(row, column, inputs):
    word = ""
    word += inputs[row][column] + inputs[row-1][column+1] + inputs[row-2][column+2] + inputs[row-3][column+3]
    if word.upper() == "XMAS":
        return 1
    return 0

def diagonal_ld(row, column, inputs):
    word = ""
    word += inputs[row][column] + inputs[row+1][column-1] + inputs[row+2][column-2] + inputs[row+3][column-3]
    if word.upper() == "XMAS":
        return 1
    return 0

def diagonal_rd(row, column, inputs):
    word = ""
    word += inputs[row][column] + inputs[row+1][column+1] + inputs[row+2][column+2] + inputs[row+3][column+3]
    if word.upper() == "XMAS":
        return 1
    return 0



inputs = []
count = 0

with open ("input.txt", "r") as f:
    inputs = f.readlines()

for row in range(len(inputs)):
    for column in range(len(inputs[row])):
        if inputs[row][column].upper() == "X":
            if row < 3:
                #cant go up
                if column < 3:
                    #cant go left
                    count +=down(row, column, inputs)
                    count +=right(row, column, inputs)
                    count +=diagonal_rd(row, column, inputs)
                elif column > len(inputs[row])-5: #take 5 instead of 4 due to \n on end of line
                    #cant go right
                    count +=down(row, column, inputs)
                    count +=left(row, column, inputs)
                    count +=diagonal_ld(row, column, inputs)
                else:
                    #can go any direction horizontally
                    count +=down(row, column, inputs)
                    count +=right(row, column, inputs)
                    count +=left(row, column, inputs)
                    count +=diagonal_ld(row, column, inputs)
                    count +=diagonal_rd(row, column, inputs)

            elif row > len(inputs)-4:
                #cant go down
                if column < 3:
                    #cant go left
                    count +=up(row, column, inputs)
                    count +=right(row, column, inputs)
                    count +=diagonal_ru(row, column, inputs)
                elif column > len(inputs[row])-5:
                    #cant go right
                    count +=up(row, column, inputs)
                    count +=left(row, column, inputs)
                    count +=diagonal_lu(row, column, inputs)
                else:
                    #can go any direction horizontally
                    count +=up(row, column, inputs)
                    count +=right(row, column, inputs)
                    count +=left(row, column, inputs)
                    count +=diagonal_lu(row, column, inputs)
                    count +=diagonal_ru(row, column, inputs)
            
            else:
                #can go any direction vertically
                if column < 3:
                    #cant go left
                    count +=up(row, column, inputs)
                    count +=down(row, column, inputs)
                    count +=right(row, column, inputs)
                    count +=diagonal_ru(row, column, inputs)
                    count +=diagonal_rd(row, column, inputs)
                elif column > len(inputs[row])-5:
                    #cant go right
                    count +=up(row, column, inputs)
                    count +=down(row, column, inputs)
                    count +=left(row, column, inputs)
                    count +=diagonal_lu(row, column, inputs)
                    count +=diagonal_ld(row, column, inputs)
                else:
                    #can go any direction horizontally
                    count +=up(row, column, inputs)
                    count +=down(row, column, inputs)
                    count +=right(row, column, inputs)
                    count +=left(row, column, inputs)
                    count +=diagonal_ld(row, column, inputs)
                    count +=diagonal_rd(row, column, inputs)
                    count +=diagonal_lu(row, column, inputs)
                    count +=diagonal_ru(row, column, inputs)

print(count)


