def login():
    username = input("Enter your username : ").strip()
    password = input("Enter your password : ").strip()
    try:
        with open("users.txt", "r") as f:
            if f"{username}:{password}" in f.read().splitlines():
                return True
            return False

    except FileNotFoundError:
        print("Error: users.txt not found.")
        return False

if __name__ == "__main__":
    if login():
        print("Login successful")
    else:
        print("Login failed")
        
