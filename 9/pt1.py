with open("input.txt", "r") as f:
    disk_map = f.readline()

formatted_disk_map = []

counter = 0
for i in range(len(disk_map)):
    if i % 2 == 0:
        for j in range(int(disk_map[i])):
            formatted_disk_map.append(str(counter))
        counter += 1
    elif i % 2 == 1:
        for j in range(int(disk_map[i])):
            formatted_disk_map.append(".")

# print(formatted_disk_map)

start = len(formatted_disk_map) - 1
exit_loop = True
for i in range(len(formatted_disk_map)):
    if formatted_disk_map[i] == ".":
        for k in range(i + 1, len(formatted_disk_map)):     #not working am going to crash out
            
            if formatted_disk_map[k] != ".":
                exit_loop = False
        if exit_loop == True:
            break
        for j in range(start, 0, -1):
            if formatted_disk_map[j] != ".":
                temp = formatted_disk_map[i]
                formatted_disk_map[i] = formatted_disk_map[j]
                formatted_disk_map[j] = temp
                start = j
                break
print(formatted_disk_map)

total = 0
for i in range(len(formatted_disk_map)):
    if formatted_disk_map[i] == ".":
        break
    total += i * int(formatted_disk_map[i])

print(total)