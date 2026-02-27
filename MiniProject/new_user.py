def new_user():
    n=input("enter the username :")
    pas=input("enter the password :")

    with open("users.txt","a") as file:
        file.write( n+":")
        file.write(pas+"\n")
    file.close()


if __name__ == "__main__":
    new_user()
    
