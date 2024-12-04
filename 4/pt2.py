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

checked = []

with open ("input.txt", "r") as f:
    inputs = f.readlines()

for row in range(len(inputs)):
    for column in range(len(inputs[row])):
        if inputs[row][column].upper() == "m":
            if row < 2:
                #cant go up
                if column < 2:
                    #cant go left
                    if diagonal_rd(row, column, inputs) == 1:
                        if diagonal_ru(row-2, column, inputs) == 1:
                            count += 1
                            checked.append(row-2, column)
                        elif diagonal_ld(row, column+2, inputs) == 1:
                            count += 1
                            checked.append(row, column+2)

                elif column > len(inputs[row])-4: 
                    #cant go right
                    if diagonal_ld(row, column, inputs) == 1:
                        if diagonal_lu(row-2, column, inputs) == 1:
                            print()                                                      #complete this
                        elif diagonal_rd(row, column-2, inputs) == 1:
                            print()
                else:
                    #can go any direction horizontally
                    count +=diagonal_ld(row, column, inputs)
                    count +=diagonal_rd(row, column, inputs)

            elif row > len(inputs)-4:
                #cant go down
                if column < 2:
                    #cant go left
                    count +=diagonal_ru(row, column, inputs)
                elif column > len(inputs[row])-4:
                    #cant go right
                    count +=diagonal_lu(row, column, inputs)
                else:
                    #can go any direction horizontally
                    count +=diagonal_lu(row, column, inputs)
                    count +=diagonal_ru(row, column, inputs)
            
            else:
                #can go any direction vertically
                if column < 2:
                    #cant go left
                    count +=diagonal_ru(row, column, inputs)
                    count +=diagonal_rd(row, column, inputs)
                elif column > len(inputs[row])-4:
                    #cant go right
                    count +=diagonal_lu(row, column, inputs)
                    count +=diagonal_ld(row, column, inputs)
                else:
                    #can go any direction horizontally
                    count +=diagonal_ld(row, column, inputs)
                    count +=diagonal_rd(row, column, inputs)
                    count +=diagonal_lu(row, column, inputs)
                    count +=diagonal_ru(row, column, inputs)

print(count)