with open("input.txt", "r") as f:
    positions_in = f.readlines()

found = False
for i in range(len(positions_in)):
    if found == True:
        break
    for j in range(len(positions_in[i])):
        if positions_in[i][j] == "^":
            start = [i, j]
            found = True

stripped = []
for row in positions_in:
    stripped.append(row.replace('\n',''))


seen = 0
for i in range(len(stripped)):
    for j in range(len(stripped[i])):
        distinct_pos = []
        distinct_pos.append(start)
        direction = "up"
        current_pos = start

        positions = []
        for row in range(len(stripped)):
            if row == i:
                new = stripped[row][:j] + "#" + stripped[row][j+1:]
                positions.append(new)
            else:
                positions.append(stripped[row])




        while True:
            if direction == "up":
                if current_pos[0] - 1 < 0:
                    break
                if positions[current_pos[0] - 1][current_pos[1]] not in  [".", "^"]:
                    direction = "right"
                    continue
                current_pos[0] -= 1

            elif direction == "right":
                if current_pos[1] + 1 >= len(positions[0]) -1:
                    break
                if positions[current_pos[0]][current_pos[1] + 1] not in  [".", "^"]:
                    direction = "down"
                    continue
                current_pos[1] += 1

            elif direction == "down":
                if current_pos[0] + 1 >= len(positions):
                    break
                if positions[current_pos[0] + 1][current_pos[1]] not in  [".", "^"]:
                    direction = "left"
                    continue
                current_pos[0] += 1

            elif direction == "left":
                if current_pos[1] - 1 < 0:
                    break
                if positions[current_pos[0]][current_pos[1] - 1] not in  [".", "^"]:
                    direction = "up"
                    continue
                current_pos[1] -= 1

            else:
                print("something has gone wrong -> direction if statements")
                break
            

            distinct_pos.append([current_pos[0], current_pos[1]])

print(seen)