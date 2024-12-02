def inc_or_dec(arr):
    direction = ""
    if len(arr) > 1:
        if arr[0] < arr[1]:
            direction = "inc"
        elif arr[0] > arr[1]:
            direction = "dec"
        else:
            return "invalid"
        
        for i in range(len(arr) - 1):
            if direction == "inc":
                if arr[i] > arr[i+1]:
                    return "invalid"
                if abs(arr[i] - arr[i+1]) < 1 or abs(arr[i] - arr[i+1]) > 3:
                    return "invalid"
                
            elif direction == "dec":
                if arr[i] < arr[i+1]:
                    return "invalid"
                if abs(arr[i] - arr[i+1]) < 1 or abs(arr[i] - arr[i+1]) > 3:
                    return "invalid"
                
        return "valid"
    return "invalid"
        

safe = 0

#Taking inputs from file
with open("input.txt", "r") as f:
    lines = f.readlines()


for line in lines:
    #Takes each line from file and converts to list of ints
    nums = []
    buf = ""
    for char in line:
        if char not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            nums.append(int(buf))
            buf = ""
            continue
        buf += char
    if inc_or_dec(nums) == "valid":
        safe+=1
    else:
        print(line, end="")


print(safe)

