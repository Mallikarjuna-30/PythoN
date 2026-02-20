# Find the second greatest element in a list

l = [166,20,13,15,18,2]
# n=len(l)-2
# l.sort()
# print(l[n])

# l1 = sorted(l)
# print(l1[-2])


largest = l[0]
seclar = l[0]
index = 0

for i in range(len(l)):
    if l[i]>largest:
        seclar = largest
        largest=l[i]
        index=i
    elif l[i]>seclar:
        seclar = l[i]
        
print("Largest : ",largest)
print("Index : ",index)
print("Second Largest : ",seclar)