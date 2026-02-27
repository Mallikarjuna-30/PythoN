# Prefix sum

# input [1,2,4,7]
# output [1,3,7,14]

l = [1,2,4,7]
# l1 = []
# sum = 0
# for  i in l:
#     sum = sum+i
#     l1.append(sum)

# print(l1)

l2 = [0]*len(l)     # pr = [0,0,0,0]
l2[0]=l[0]          # pr = [1,0,0,0]
 
for i in range(0,len(l)):
    l2[i]=l2[i-1]+l[i]
    
print(l2)