import random

board = [" " for _ in range(9)]

def display_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combination in winning_combinations:
        a, b, c = combination

        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None

print("\n================================")
print("          TIC-TAC-TOE")
print("================================")
print("You are X and the computer is O.")
print("Choose a position from 1 to 9.")

while True:
    board = [" " for _ in range(9)]

    while True:
        display_board()

        choice = input("Choose a position (1-9) or enter 0 to return to menu: ")

        if choice == "0":
            print("\nReturning to Main Menu...")
            break

        if not choice.isdigit() or int(choice) not in range(1, 10):
            print("Invalid choice! Please enter a number from 1 to 9.")
            continue

        position = int(choice) - 1

        if board[position] != " ":
            print("That position is already taken! Choose another.")
            continue

        board[position] = "X"

        winner = check_winner()

        if winner:
            display_board()
            print("Congratulations! You beat the computer!")
            break

        if " " not in board:
            display_board()
            print("It's a draw!")
            break

        computer_position = random.choice(
            [i for i in range(9) if board[i] == " "]
        )

        board[computer_position] = "O"

        print("The computer chose position", computer_position + 1)

        winner = check_winner()

        if winner:
            display_board()
            print("The computer wins! Better luck next time!")
            break

        if " " not in board:
            display_board()
            print("It's a draw!")
            break

    if choice == "0":
        break

    play_again = input("\nWould you like to play again? (yes/no): ").lower().strip()

    if play_again != "yes":
        print("\nReturning to Main Menu...")
        break
