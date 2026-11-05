
import random

secret_number = random.randint(1, 20)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 20.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("Congratulations! You guessed it!")
        print("Number of attempts:", attempts)
        break

