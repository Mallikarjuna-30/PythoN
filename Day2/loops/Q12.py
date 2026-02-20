# check whether a string is palindrome or not

str1 = input("Enter a string: ")
str1 = str1.upper()
str2 = ""

for i in range(len(str1) - 1, -1, -1):
    str2 = str2 + str1[i]

if str1 == str2:
    print("String is : ", str1)
    print("Reversed String is : ", str2)
    print("String is Palindrome")
else:
    print("String is not a Palindrome")
