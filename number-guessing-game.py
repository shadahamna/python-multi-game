import random

score = 0

print("================================")
print("     NUMBER GUESSING GAME")
print("================================")
print("Welcome! Try to guess the secret number.")

while True:

    print("\nChoose your difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    difficulty = input("Enter your choice (1/2/3): ")

    if difficulty == "1":
        max_number = 10
        max_guesses = 5
        level = "Easy"

    elif difficulty == "2":
        max_number = 50
        max_guesses = 7
        level = "Medium"

    elif difficulty == "3":
        max_number = 100
        max_guesses = 5
        level = "Hard"

    else:
        print("Invalid choice! Please choose 1, 2 or 3.")
        continue

    print("\nYou selected", level, "mode!")
    print("Guess a number between 1 and", max_number)
    print("You have", max_guesses, "attempts.")

    secret_number = random.randint(1, max_number)

    guessed = False
    attempts = 0

    while attempts < max_guesses:

        guess_input = input("\nEnter your guess: ")

        if not guess_input.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        guess = int(guess_input)

        if guess < 1 or guess > max_number:
            print("Please enter a number within the given range.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print("\nCongratulations! You guessed correctly!")
            guessed = True

            points = (max_guesses - attempts + 1) * 10
            score += points

            print("Attempts used:", attempts)
            print("Points earned:", points)
            break

    if not guessed:
        print("\nGame over! You ran out of guesses.")
        print("The secret number was:", secret_number)

    print("\nYour total score:", score)

    play_again = input(
        "\nWould you like to play again? (yes/no): "
    ).lower().strip()

    if play_again != "yes":
        print("\n================================")
        print("         GAME FINISHED")
        print("================================")
        print("Your final score:", score)
        print("Thanks for playing!")
        break

