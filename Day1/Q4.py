'''
Accept name and age from the user and check if he is valid to vote or not
'''
name = input("Enter ur name : ")
age  = int(input("Enter ur age: "))

if(age>=18):
    print(f"{name} is valid to vote")
else:
    print(f"{name} is not valid to vote")