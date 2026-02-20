# Find  the greatest element and print its index too

l = [34,342,42,6,78,645,345,345,645]

# print(max(l))
# print(l.index(max(l)))

largest = l[0]
index = 0

for i in range(len(l)):
    if l[i]>largest:
        largest=l[i]
        index=i
        
print(largest)
print(index)