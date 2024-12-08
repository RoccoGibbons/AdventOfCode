def checker(node, stripped):
    if (node[0] < 0 or node[0] > len(stripped[0]) - 1) or (node[1] < 0 or node[1] > len(stripped) - 1):
        return False
    else:
        return True
    


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
                    x = 1
                    while True:
                        node1 = (x1 + (horizontal * x) , y1 + (vertical * x))
                        if checker(node1, stripped) == True:
                            if node1 not in unique_nodes:
                                print("1")
                                print(node1)
                                unique_nodes.append(node1)
                            x += 1
                        else:
                            break
                    x = 1
                    while True:
                        node2 = (x2 - (horizontal * x) , y2 - (vertical * x))
                        if checker(node2, stripped) == True:
                            if node2 not in unique_nodes:
                                print("2")
                                print(node2)
                                unique_nodes.append(node2)
                            x += 1
                        else:
                            break

                elif y2 > y1:
                    x = 1
                    while True:
                        node1 = (x1 + (horizontal * x) , y1 - (vertical * x))
                        if checker(node1, stripped) == True:
                            if node1 not in unique_nodes:
                                print("3")
                                print(node1)
                                unique_nodes.append(node1)
                            x += 1
                        else:
                            break
                    x = 1
                    while True:
                        node2 = (x2 - (horizontal * x) , y2 + (vertical * x))
                        if checker(node2, stripped) == True:
                            if node2 not in unique_nodes:
                                print("4")
                                print(node2)
                                unique_nodes.append(node2)
                            x += 1
                        else:
                            break
                else:
                    x = 1
                    while True:
                        node1 = (x1 + (horizontal * x) , y1)
                        if checker(node1, stripped) == True:
                            if node1 not in unique_nodes:
                                print("5")
                                print(node1)
                                unique_nodes.append(node1)
                            x += 1
                        else:
                            break
                    x = 1
                    while True:
                        node2 = (x2 - (horizontal * x) , y2)
                        if checker(node2, stripped) == True:
                            if node2 not in unique_nodes:
                                print("6")
                                print(node2)
                                unique_nodes.append(node2)
                            x += 1
                        else:
                            break

            elif x2 > x1:
                if y1 > y2:
                    x = 1
                    while True:
                        node1 = (x1 - (horizontal * x) , y1 + (vertical * x))
                        if checker(node1, stripped) == True:
                            if node1 not in unique_nodes:
                                print("7")
                                print(node1)
                                unique_nodes.append(node1)
                            x += 1
                        else:
                            break
                    x = 1
                    while True:
                        node2 = (x2 + (horizontal * x) , y2 - (vertical * x))
                        if checker(node2, stripped) == True:
                            if node2 not in unique_nodes:
                                print("8")
                                print(node2)
                                unique_nodes.append(node2)
                            x += 1
                        else:
                            break
                elif y2 > y1:
                    x = 1
                    while True:
                        node1 = (x1 - (horizontal * x) , y1 - (vertical * x))
                        if checker(node1, stripped) == True:
                            if node1 not in unique_nodes:
                                print("9")
                                print(node1)
                                unique_nodes.append(node1)
                            x += 1
                        else:
                            break
                    x = 1
                    while True:
                        node2 = (x2 + (horizontal * x) , y2 + (vertical * x))
                        if checker(node2, stripped) == True:
                            if node2 not in unique_nodes:
                                print("10")
                                print(node2)
                                unique_nodes.append(node2)
                            x += 1
                        else:
                            break
                else:
                    x = 1
                    while True:
                        node1 = (x1 - (horizontal * x) , y1)
                        if checker(node1, stripped) == True:
                            if node1 not in unique_nodes:
                                print("11")
                                print(node1)
                                unique_nodes.append(node1)
                            x += 1
                        else:
                            break
                    x = 1
                    while True:
                        node2 = (x2 + (horizontal * x) , y2)
                        if checker(node2, stripped) == True:
                            if node2 not in unique_nodes:
                                print("12")
                                print(node2)
                                unique_nodes.append(node2)
                            x += 1
                        else:
                            break
            else:
                if y1 > y2:
                    x = 1
                    while True:
                        node1 = (x1, y1 + (vertical * x))
                        if checker(node1, stripped) == True:
                            if node1 not in unique_nodes:
                                print("13")
                                print(node1)
                                unique_nodes.append(node1)
                            x += 1
                        else:
                            break
                    x = 1
                    while True:
                        node2 = (x2 , y2 - (vertical * x))
                        if checker(node2, stripped) == True:
                            if node2 not in unique_nodes:
                                print("14")
                                print(node2)
                                unique_nodes.append(node2)
                            x += 1
                        else:
                            break
                elif y2 > y1:
                    x = 1
                    while True:
                        node1 = (x1 , y1 - (vertical * x))
                        if checker(node1, stripped) == True:
                            if node1 not in unique_nodes:
                                print("15")
                                print(node1)
                                unique_nodes.append(node1)
                            x += 1
                        else:
                            break
                    x = 1
                    while True:
                        node2 = (x2 , y2 + (vertical * x))
                        if checker(node2, stripped) == True:
                            if node2 not in unique_nodes:
                                print("16")
                                print(node2)
                                unique_nodes.append(node2)
                            x += 1
                        else:
                            break
                    

# for node in unique_nodes:
#     print(node)
print(len(unique_nodes))
