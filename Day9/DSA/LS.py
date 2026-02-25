# Linear Search

l = []
n = int(input("Enter the number of elements to  be inserted : "))
for i in range(n):
    item  = int(input("Enter an element : "))
    l.append(item)
key = int(input("Enter an element to search: "))
flag = 0

for i in range(n):
    if l[i] == key:
        flag = 1
        break
if flag == 1:
    print("Element found")
else:
    print("Element not found")
