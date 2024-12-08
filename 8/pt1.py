with open("input.txt", "r") as f:
    inputs = f.readlines()
    
stripped = []

for line in inputs:
    stripped.append(line.replace("\n", ""))


antennas = []

for line in stripped:
    for letter in line:
        if letter not in antennas and letter != ".":
            antennas.append(letter)
            

positions_dict = {}

for x in antennas:
    positions = []
    
    for i in range(len(stripped)):
        for j in range(len(line)):
            if stripped[i][j] == x:
                positions.append((j, i))  #j acts as an x axis and i acts as a y axis
    
    positions_dict[x] = positions
    
unique_nodes = []

for antenna in positions_dict:
    for pos1 in positions_dict[antenna]:
        for pos2 in positions_dict[antenna]:
            if pos1 == pos2:
                continue
            x1 = pos1[0]
            x2 = pos2[0]
            y1 = pos1[1]
            y2 = pos2[1]
            
            horizontal = abs(x1 - x2)
            vertical = abs(y1 - y2)
            
            if x1 > x2:
                if y1 > y2:
                    node1 = (x1 + horizontal, y1 + vertical)
                    node2 = (x2 - horizontal, y2 - vertical)
                elif y2 > y1:
                    node1 = (x1 + horizontal, y1 - vertical)
                    node2 = (x2 - horizontal, y2 + vertical)
                else:
                    node1 = (x1 + horizontal, y1)
                    node2 = (x2 - horizontal, y2)
            elif x2 > x1:
                if y1 > y2:
                    node1 = (x1 - horizontal, y1 + vertical)
                    node2 = (x2 + horizontal, y2 - vertical)
                elif y2 > y1:
                    node1 = (x1 - horizontal, y1 - vertical)
                    node2 = (x2 + horizontal, y2 + vertical)
                else:
                    node1 = (x1 - horizontal, y1)
                    node2 = (x2 + horizontal, y2)
            else:
                if y1 > y2:
                    node1 = (x1, y1 + vertical)
                    node2 = (x2, y2 - vertical)
                elif y2 > y1:
                    node1 = (x1, y1 - vertical)
                    node2 = (x2, y2 + vertical)

                    
            
            if (node1[0] < 0 or node1[0] > len(stripped[0]) - 1) or (node1[1] < 0 or node1[1] > len(stripped) - 1):
                #node 1 is invalid
                print(end="")
            else:
                #node 1 is valid
                if node1 not in unique_nodes:
                    # print(antenna, node1)
                    unique_nodes.append(node1)
                    
                    
            if (node2[0] < 0 or node2[0] > len(stripped[0]) - 1) or (node2[1] < 0 or node2[1] > len(stripped) - 1):
                #node 2 is invalid
                print(end="")
            else:
                #node 2 is valid
                if node2 not in unique_nodes:
                    # print(antenna, node2)
                    unique_nodes.append(node2)

# for node in unique_nodes:
#     print(node)
print(len(unique_nodes))
