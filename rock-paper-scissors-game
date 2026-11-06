
import random

print("\n================================")
print("       ROCK PAPER SCISSORS")
print("================================")

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

while True:
    print("\nChoose your move:")
    print("Enter the number (1, 2 or 3) to select your move.")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("0. Return to Main Menu")

    choice = input("\nEnter your choice: ").lower().strip()

    if choice == "0":
        print("\nReturning to Main Menu...")
        break

    if choice in ["1", "rock"]:
        player = "rock"
    elif choice in ["2", "paper"]:
        player = "paper"
    elif choice in ["3", "scissors"]:
        player = "scissors"
    else:
        print("\nInvalid choice! Please enter 1, 2 or 3.")
        continue

    computer = random.choice(choices)

    print("\nYou chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("\nIt's a tie!")

    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("\nYou win!")
        player_score += 1

    else:
        print("\nComputer wins!")
        computer_score += 1

    print("\nYour score:", player_score)
    print("Computer score:", computer_score)

    play_again = input("\nWould you like to play again? (yes/no): ").lower().strip()

    if play_again != "yes":
        print("\nReturning to Main Menu...")
        break
