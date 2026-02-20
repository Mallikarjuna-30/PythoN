# Check if the list is sorted or not

l = []
n = int(input("Enter the number of elements to be stored in the list : "))

for i in range(n):
    l.append(int(input("Enter the element to bo stored : ")))

print(l)
l1 = sorted(l)

if(l==l1):
    print("Sorted")
else:
    print("Not Sorted")