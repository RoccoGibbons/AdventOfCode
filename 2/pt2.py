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


# def repeats(arr):
#     new_arr = arr
#     buf = []
#     print(new_arr)
#     for i in range(len(new_arr)):
#         if new_arr[i] in buf:
#             new_arr.pop(i)
#             break
#         else:
#             buf.append(new_arr[i])
#     print(new_arr)
#     return inc_or_dec(new_arr)

# def direction(arr):
#     new_arr = arr
#     if new_arr[0] < new_arr[1]:
#         for i in range(len(new_arr) - 1):
#             if new_arr[i] > new_arr[i + 1]:
#                 new_arr.pop(i)
#                 break
#     elif new_arr[0] > new_arr[1]:
#         for i in range(len(new_arr) - 1):
#             if new_arr[i] < new_arr[i + 1]:
#                 new_arr.pop(i)
#                 break
#     return inc_or_dec(new_arr)

# def size(arr):
#     new_arr = arr
#     for i in range(len(new_arr) - 1):
#         if abs(new_arr[i] - new_arr[i+1]) < 1 or abs(new_arr[i] - new_arr[i+1]) > 3:
#             new_arr.pop(i)
#             break
#     if inc_or_dec(new_arr) == "invalid":
#         new_arr = arr
#         for i in range(len(new_arr) - 1):
#             if abs(new_arr[i] - new_arr[i+1]) < 1 or abs(new_arr[i] - new_arr[i+1]) > 3:
#                 new_arr.pop(i + 1)
#                 break
#     return inc_or_dec(new_arr)

    
    
#answer to previous part
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
        continue
    
    #check for repeats
    # if repeats(nums) == "valid":
    #     safe += 1
    #     continue
    # elif direction(nums) == "valid":
    #     safe += 1
    #     continue
    # elif size(nums) == "valid":
    #     safe += 1
    #     continue

    for i in range(len(nums)):
        new = []
        for num in nums:
            new.append(num)
        new.pop(i)

        if inc_or_dec(new) == "valid":
            safe += 1
            break


print(safe)

