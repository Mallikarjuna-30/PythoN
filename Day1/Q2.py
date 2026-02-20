'''
Accept the gender from the user as char and print the respective greetings
'''

gender = input("Enter your gender: ")
gender=gender.upper() #convert to upper case 

if(gender == 'M'):
    print("Good Morning Sir")
elif(gender == 'F'):
    print("Good Morning Maam")
else:
    print("Enter M or F")
