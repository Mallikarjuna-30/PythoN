# GAME
# Number Guessing Game

import random

n = random.randint(1, 100)
count = 0
guess = 0
while guess != n:
    guess = int(input("Guess the number: "))
    count += 1
    if guess < n:
        print("Too low")
        print("Please try again")
    elif guess > n:
        print("Too high")
        print("Please try again")
    else:
        print("Correct")


print(f"You guessed the number in {count} attempts")
