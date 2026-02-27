# Card details

def card():
    while True:
        num = input("Enter the card number:")
        if len(num) == 12:
            if num.isnumeric():
                print("Valid number!")
                break
        else:  
            print("Invalid Card Number")
        
    while True:
        cvv = input("Enter the CVV :")
        if len(cvv) == 3:
            if cvv.isnumeric():
                print("Valid CVV!")
                break
        else:  
            print("Invalid CVV Number")
            
    while True:
        __pin = input("Enter the password (4 digits):")
        if len(__pin) == 4:
            if __pin.isnumeric():
                print("Valid PIN")
                break
        else:  
            print("Invalid PIN")
    return True


if __name__ == "__main__":
    card()