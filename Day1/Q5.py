'''
Accept a  year and check whether it is a leap year or not
'''
yr=int(input("Enter a year: "))

# if(yr%4==0 and yr%100!=0 or yr%400==0):
#     print(f"{yr} is a leap year")
# else:
#     print(f"{yr} is not a leap year")

if(yr%100==0 and yr%400==0):
    print(f"year {yr} is a leap year")
elif(yr%100!=100 and yr%4==0):
    print(f"year {yr} is a leap year")
else:
    print(f"year {yr} is not a leap year")