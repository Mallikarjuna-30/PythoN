# Print positive and negative elements of a list seperately

l = [1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
l1 = []
l2 = []

for i in l:
    if i > 0:
        l1.append(i)
    else:
        l2.append(i)
        
print(l1)
print(l2)