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

#Sort the lists and pair up each of the smallest, 2nd smallest, etc. 
arr1.sort()
arr2.sort()

pairs = []

for i in range(len(arr1)):
    pairs.append((arr1[i], arr2[i]))


#Add up distances between pairs
distance_total = 0

for tup in pairs:
    distance = abs(tup[0] - tup[1])
    distance_total += distance
    
print(distance_total)