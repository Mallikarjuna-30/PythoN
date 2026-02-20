# <----- Rock Paper Scissor -----> #

import random

print("# <----- Rock Paper Scissor -----> #")

choices = ('rock','paper','scissor')

win = 1
while win == 1:
    computer = random.choice(choices)
    user = input("Enter rock paper scissor : ").lower()
    if user == computer:
        print("Draw")
    elif(user == 'rock' and computer == "scissor") or (user == 'paper' and  computer == 'rock') or (user == 'scissor' and  computer == 'paper'):
        print("User win")
        win = 1
    elif(user == 'rock' and computer == 'paper') or (user == 'paper' and computer == 'scissor') or (user == 'scissor' and computer == 'rock'):
        print("Computer win")
        win = 0
    else:
        print("Invalid input")
