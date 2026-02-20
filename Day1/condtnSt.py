# Conditional Statements

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if(a>b):
    print(f"{a} is greater than {b}")
elif(a<b):
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")


# Nested if-else

if(a>b):
    if(a>c):
        print(f"{a} is greater than {b} and {c}")
    else:
        print(f"{c} is greater than {a} and {b}")
else:
    if(b>c):
        print(f"{b} is greater than {a} and {c}")
    else:
        print(f"{c} is greater than {a} and {b}")

# Ternary Operator
print(f"{a} is greater than {b}") if a>b else print(f"{b} is greater than {a}")

#elif
if(a>b):
    print(f"{a} is greater than {b}")
elif(a<b):
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")