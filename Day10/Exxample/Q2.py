# Move Zeroes to End

# input [0,1,0,3,12]
# output [1,3,12,0,0]

l = [0,1,0,3,12,0,2]
# l1 = sorted(l)
count = 0

# for i in l:
#     if i == 0:
#         count = count+1
#         l1.remove(0)

# for i in range(count):
#     l1.append(0)



# for i in l:
#     if i == 0:
#         l1.remove(0)
#         l1.append(0)



# for i in l:
#     if i == 0:
#         l.remove(0)
#         l.append(0)

j=0
for i  in range(len(l)):
    if l[i]!=0:
        l[i],l[j]=l[j],l[i]
        j=j+1
        
print(l)
