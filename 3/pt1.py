with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0

for line in lines:
    for i in range(len(line)):
        if line[i] == "m":
            equation = ""
            equation += line[i] + line[i+1] + line[i+2] + line[i+3]
            if equation != "mul(":
                continue

            equation += line[i+4] + line[i+5] + line[i+6] + line[i+7] + line[i+8] + line[i+9] + line[i+10] + line[i+11]
            new_eq = ""
            valid = False
            #check for end bracket and cut off string after it
            for i in range(len(equation)):
                if equation[i] == ")":
                    new_eq += equation[i]
                    valid = True
                    break
                new_eq += equation[i]

            if valid == False:
                continue

            #check interior of string
            valid = True
            has_comma = False
            for c in new_eq:
                if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "m", "u", "l", "(", ")", ","]:
                    valid = False #continue here and set valid var
                    break
                if c == ",":
                    has_comma = True

            if valid == False:
                continue
            if has_comma == False:
                continue

            num1 = ""
            num2 = ""
            num_all = new_eq[4:]
            num_all = num_all[:-1]
            
            past = False
            for c in num_all:            
                if c == ",":
                    past = True
                    continue
                if past == False:
                    num1 += c
                elif past == True:
                    num2 += c
            
            total += int(num1) * int(num2)

print(total)
            
        