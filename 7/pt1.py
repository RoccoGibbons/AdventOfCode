import itertools

with open("input.txt", "r") as f:
    inputs = f.readlines()


int_lists = []
for line in inputs:
    temp = ""
    int_line = []
    for letter in line:
        if letter == ":" or letter == " " or letter == "\n":
            if temp == "":
                continue
            int_line.append(int(temp))
            temp = ""
            continue
        temp += letter
    int_lists.append(int_line)

total = 0


for l in int_lists:
    goal = l[0]
    rest = l[1:]

    operations = len(l) - 2
    options = list(itertools.product("*+", repeat=operations))
    
    for group in options:
        count = 1
        num = rest[0]
        for o in group:
            if o == "*":
                if num * rest[count] > goal+ 1:
                    break
                num *= rest[count]
                count += 1
                
            elif o == "+":
                if num + rest[count] > goal+ 1:
                    break
                num += rest[count]
                count += 1
            else:
                print("Error: for loop (o in options)")

        if num == goal:
            total += goal
            break

print(total)