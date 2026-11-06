
import subprocess
import sys
from pathlib import Path

games = {
    "1": ("Number Guessing Game", "number-guessing-game.py"),
    "2": ("Rock Paper Scissors", "rock-paper-scissors-game.py"),
    "3": ("Quiz Challenge", "quiz-challenge.py"),
    "4": ("Word Scramble", "scramble-word-game.py"),
    "5": ("Tic-Tac-Toe", "tic-tac-toe.py")
}

while True:
    print("\n================================")
    print("       PYTHON MINI GAMES")
    print("================================")

    for number, (name, filename) in games.items():
        print(number + ". " + name)

    print("0. Exit")

    choice = input("\nChoose a game (0-5): ")

    if choice == "0":
        print("\nThanks for playing!")
        break

    elif choice in games:
        game_name, filename = games[choice]
        game_path = Path(__file__).parent / filename

        if game_path.exists():
            print("\nStarting", game_name, "...")
            subprocess.run([sys.executable, str(game_path)])
        else:
            print("\nThis game is coming soon!")

    else:
        print("\nInvalid choice! Please choose from 0 to 5.")
