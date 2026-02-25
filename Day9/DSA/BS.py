# Searching an element using Binary Search

l = []
n = int(input("Enter the number of elements to  be inserted : "))
for i in range(n):
    item  = int(input("Enter an element : "))
    l.append(item)
key = int(input("Enter an element to search: "))
flag = 0
left = 0
l = sorted(l)
right = len(l) - 1

while left <= right:
    mid = (left + right) // 2
    if l[mid] == key:
        flag = 1
        break
    elif l[mid] < key:
        left = mid + 1
    else:
        right = mid - 1

if flag == 1:
    print("Element found at index", mid)
else:
    print("Element not found")