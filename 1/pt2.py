similarity = 0

arr1 = []
arr2 = []

#Taking inputs from file
with open("input.txt", "r") as f:
    x = f.readlines()
    for line in x:
        num1 = line[:5]
        num2 = line[5:]
        arr1.append(int(num1))
        arr2.append(int(num2))
        
for i in arr1:
    score = 0
    for j in arr2:
        if i == j:
            score += 1
    similarity += score * i
    
print(similarity)