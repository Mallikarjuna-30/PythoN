# print the sum of even and odd numbers seperatly

n = int(input("Enter a number"))
s1 = 0
s2 = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        s1 = s1 + i
    else:
        s2 = s2 + i

print("sum of even numbers is ", s1)
print("sum of odd numbers is ", s2)
