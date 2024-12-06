with open("input.txt", "r") as f:
    positions = f.readlines()

found = False
for i in range(len(positions)):
    if found == True:
        break
    for j in range(len(positions[i])):
        if positions[i][j] == "^":
            start = [i, j]
            found = True
            
for row in positions:
    row = row.replace('\n','')


distinct_pos = []
distinct_pos.append(start)
direction = "up"

current_pos = start

while True:
    if direction == "up":
        if current_pos[0] - 1 < 0:
            break
        if positions[current_pos[0] - 1][current_pos[1]] not in  [".", "^"]:
            print(positions[current_pos[0] - 1][current_pos[1]])
            direction = "right"
            continue
        current_pos[0] -= 1

    elif direction == "right":
        if current_pos[1] + 1 >= len(positions[0]) -1:
            break
        if positions[current_pos[0]][current_pos[1] + 1] not in  [".", "^"]:
            print(positions[current_pos[0]][current_pos[1] + 1])
            direction = "down"
            continue
        current_pos[1] += 1

    elif direction == "down":
        if current_pos[0] + 1 >= len(positions):
            break
        if positions[current_pos[0] + 1][current_pos[1]] not in  [".", "^"]:
            print(positions[current_pos[0] + 1][current_pos[1]])
            direction = "left"
            continue
        current_pos[0] += 1

    elif direction == "left":
        if current_pos[1] - 1 < 0:
            break
        if positions[current_pos[0]][current_pos[1] - 1] not in  [".", "^"]:
            print(positions[current_pos[0]][current_pos[1] - 1])
            direction = "up"
            continue
        current_pos[1] -= 1

    else:
        print("something has gone wrong -> direction if statements")
        break
    

    print(current_pos, direction)
    distinct_pos.append([current_pos[0], current_pos[1]])



#remove duplicates and print length
no_dup_pos = []
for pos in distinct_pos:
    if pos not in no_dup_pos:
        no_dup_pos.append(pos)

print(len(no_dup_pos) + 1) #the add 1 is because the list.append didn't include the last position