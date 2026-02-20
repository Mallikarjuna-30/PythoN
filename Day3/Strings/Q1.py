# take a string input from the user print the count of alphabet ,digit and special characters

str = input("Enter a string: ")
alpha = 0
digit = 0
special = 0
space = 0
for i in str:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    else:
        special += 1

print("Alphabets are : ", alpha)
print("Digits are : ", digit)
print("Special characters are : ", special)
print("Spaces are : ", space)
