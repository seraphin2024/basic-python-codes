# Number guessing game

import random
target = random.randint(1, 100)
guess = -1

while guess != target:
    guess = int(input("Guess the number (1 to 100): "))
    if guess < target:
        print("Too low")
    elif guess > target:
        print("Too high")
    else:
        print("Correct! You guessed it.")