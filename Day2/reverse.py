# Reversing a number

n = int(input("Enter a number: "))
temp = 0
rev = 0

# while n != 0:
#     temp = n % 10
#     rev = rev * 10 + temp
#     n = n // 10

# print(rev)


while n != 0:
    print(n % 10)
    n = n // 10
