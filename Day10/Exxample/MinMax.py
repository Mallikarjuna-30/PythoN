# Find minimum and maximum ele in list without using built in function

l = [1121,2,3,4,5,6,7,8,9,10,12,112]

max = min = l[0]

for i in l:
    if i < min:
        min = i
    if i > max:
        max = i

print(f"Minimum element is {min} and Maximum element is {max}")
