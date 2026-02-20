"""College Placement"""

print("----COLLEGE PLACEMENT TRAINING----")
name = input("Enter your name ")
name = name.upper()
age = int(input("Enter  your age "))
atd = int(input("Enter your attendence : "))
marks = float(input("enter tour marks: "))
fees = 20000
discount = 0

if age < 18 or marks < 60 or atd < 75:
    print("Your not eligible to vote ")
else:
    if marks >= 85 and marks <= 100:
        discount = fees * 0.30
        fees = fees - discount
    elif marks >= 75:
        discount = fees * 0.10
        fees = fees - discount
    else:
        print("No discount")
    if fees < 15000:
        print("Special Approval Required")
        hst = input("Enter Y/N is u r a hosteller")
        hst = hst.upper()
    if hst == "Y":
        print("Hostel fees applied")
        fees = fees + 5000
    week = input("Do u need weekend classes : (Y?N)")
    week = week.upper()
    if week == "Y":
        fees = fees + 2000
    print(f"{name} is eligible for the training")
    print("The details of the student are:")
    print(f"Student name : {name}")
    print(f"Student age : {age}")
    print(f"Student markd are : {marks}")
    print(f"Student discounts are : {discount}")
    print(f"Student total fees required to pay : {fees}")
