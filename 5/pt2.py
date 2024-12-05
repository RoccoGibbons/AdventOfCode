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
    
    if correct == True:
        continue
    
    breakout = False
    if correct == False:
        while breakout == False:
            breakout = True
            for rule in rules:
                try:
                    if update_dict[rule[0]] > update_dict[rule[1]]:
                        temp = update_dict[rule[0]]
                        update_dict[rule[0]] = update_dict[rule[1]]
                        update_dict[rule[1]] = temp
                        breakout = False
                        break
                    
                except KeyError:
                    continue
                
    for rule in rules:
        try:
            if update_dict[rule[0]] > update_dict[rule[1]]:
                print("didn't work")
        except KeyError:
            continue
        
    length = len(update) + 1
    middle = int(length / 2) - 1
    # print(f"{update} => {update[middle]}\nlength:{length - 1} => middle:{middle}") 
    for key in update_dict:
        if update_dict[key] == middle:
            total += key
            break
    
print(total)
    

