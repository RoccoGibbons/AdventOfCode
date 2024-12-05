inputs1 = []
inputs2 = []
count = 0

with open ("input.txt", "r") as f:
    inputs1 = f.readlines()

for row in inputs1:
    inputs2.append(row.strip())

inputs = []
length = len(inputs2[0]) + 8

#creates buffer around the edge
for i in range(4):
    inputs.append("*" * length)

for row in inputs2:
    inputs.append("****" + row + "****")
    
for i in range(4):
    inputs.append("*" * length)
    
        

for row in range(len(inputs)):
    for column in range(len(inputs)):
        if inputs[row][column] == "A":
            if (inputs[row-1][column-1] == "M" and inputs[row+1][column+1] == "S") or (inputs[row-1][column-1] == "S" and inputs[row+1][column+1] == "M"):
                if (inputs[row+1][column-1] == "M" and inputs[row-1][column+1] == "S") or (inputs[row+1][column-1] == "S" and inputs[row-1][column+1] == "M"):
                    count += 1
            elif (inputs[row+1][column-1] == "M" and inputs[row-1][column+1] == "S") or (inputs[row+1][column-1] == "S" and inputs[row-1][column+1] == "M"):
                if (inputs[row-1][column-1] == "M" and inputs[row+1][column+1] == "S") or (inputs[row-1][column-1] == "S" and inputs[row+1][column+1] == "M"):
                    count += 1

print(count)