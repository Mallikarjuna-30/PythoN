# Fuctions


def hello():  # No Arguments
    print("Hello World !!")
    print("Learning Python")


hello()


def add():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    print(a + b)


add()


def std(name, age):
    print(f"Name : {name}")
    print(f"Age : {age}")


std(age=20, name="John")  # Keyword Arguments
