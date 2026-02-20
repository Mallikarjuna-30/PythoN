# revese a string without use in built in functions

str = input("Enter a string : ")
str = str.upper()

for i in range(len(str) - 1, -1, -1):
    print(str[i], end=" ")
