lines = []

with open("input.txt", "r") as f:
    lines = f.readlines()

rules = []
updates = []

change = False

for line in lines:
    if len(line) == 1:
        change = True
        continue
    
    if change == False:
        rule = []
        buf = ""
        for letter in line:
            if letter == "|" or letter == "\n":
                rule.append(int(buf))
                buf = ""
                continue
            buf += letter
        rules.append(rule)


    elif change == True:
        update = []
        buf = ""
        for letter in line:
            if letter == "," or letter == "\n":
                update.append(int(buf))
                buf = ""
                continue
            buf += letter
        updates.append(update)

total = 0

for update in updates:
    update_dict = {}
    for i in range(len(update)):
        update_dict[update[i]] = i

    correct = True

    for rule in rules:
        try:
            if update_dict[rule[0]] > update_dict[rule[1]]:
                correct = False
        except KeyError:
            continue
        

    if correct == False:
        for i in range(len(rules)):
            for j in range(len(rules)):
                try:
                    if update_dict[rules[i][0]] > update_dict[rules[i][1]]:
                        print(update)
                        index1 = update.index(rules[i][0])
                        index2 = update.index(rules[i][1])
                        
                        temp = update[index1]
                        update[index1] = update[index2]
                        update[index2] = temp
                        print(update)
                except KeyError:
                    continue

    for rule in rules:
        try:
            if update_dict[rule[0]] > update_dict[rule[1]]:
                print("didn't work")
        except KeyError:
            continue

