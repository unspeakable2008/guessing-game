import random
print("number guessing game")
number = random.randint(1,9)
chances = 0
print("guess a number from 1-9")
while(chances<5):
    guess = int(input("enter your guess"))
    if (guess == number):
        print("congratulations you won ")
        break
    elif(guess<number):
        print("your guess is too low, try and win next time")
    else:
        print("your guess is too high")
    chances = chances+1
if (chances>=5):
    print("you lost, try to win next time")
    