# Palindrome

n = int(input("Enter a number: "))
rev = 0
temp = n
while n != 0:
    rev = rev * 10 + n % 10
    n = n // 10

if rev == temp:
    print("Palindrome")
else:
    print("Not a Palindrome")
