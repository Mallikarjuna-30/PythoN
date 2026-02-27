## PROJECT
from login import login
from new_user import new_user
from card import card
from product import product


u = input("Are you already an user? y/n :")
u =  u.lower()
if u == "y":
    t = login()
else:
    new_user()
    t = login()

if t == True:
    total = product()
    print("Total Amount to be paid is :",total)
    print("\nChoose Payment Method:")
    print("1. COD")
    print("2. UPI")
    print("3. CARD")

    pm = int(input("Enter choice: "))
    def payment():
        if pm == 1:
            print("You choose Cash on Delivery : COD")
            addr = input("Enter the address:")
            print("Adress:", addr)
            print("Order Successful!")
            return True
        elif pm == 2:
            print("You choose UPI Payent")
            upi_id = input("Enter your UPI ID:")
            print("Notification will be sent to UPI ID:", upi_id)
            print("Order Successful!")
            return True
        elif pm == 3:
            print("You choose Card Payment")
            while True:
                c = card()
                if c == True:
                    print("Card details are stored and proteted")
                    print("Order Successful!")
                    return True
                else:
                    print("Card Details Invalid")
                    r = input("Do you want to retry? y/n")
                    r = r.lower()
                    if r != 'y':
                        print("Payment cancelled")
                        return False
        else:
            print("INVALID PAYMENT METHOD")
            return False
    p = payment()

    if p != True:
        print("Payment Failed. Exiting Program.")
        exit()

    with open("cart.txt", "w") as c:
        pass
else:
    print("Invalid login!!!!")