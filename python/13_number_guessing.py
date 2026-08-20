"""Simple number guessing game using Python's random module."""

import random

secret = random.randint(1, 10)

while True:
    guess = int(input("Guess a number (1-10): "))

    if guess == secret:
        print("Correct! 🎉")
        break
    if guess < secret:
        print("Too low.")
    else:
        print("Too high.")
