
import random

words = [
    ("python", "A popular programming language"),
    ("computer", "An electronic device used for processing data"),
    ("keyboard", "A device used for typing"),
    ("internet", "A worldwide network"),
    ("science", "The study of the natural world"),
    ("planet", "A large object that orbits a star"),
    ("elephant", "The largest land animal"),
    ("rainbow", "A colorful arc seen in the sky"),
    ("library", "A place where books are kept"),
    ("diamond", "A precious gemstone"),
    ("airplane", "A vehicle that flies"),
    ("chocolate", "A sweet food made from cocoa"),
    ("universe", "Everything that exists in space"),
    ("mountain", "A very high natural landform"),
    ("calendar", "A system used to organize dates")
]

random.shuffle(words)

total_score = 0

for round_number in range(3):
    round_score = 0

    print("\n================================")
    print("         WORD SCRAMBLE")
    print("          ROUND", round_number + 1)
    print("================================")

    for word, hint in words[round_number * 5:(round_number + 1) * 5]:
        scrambled = "".join(random.sample(word, len(word)))

        while scrambled == word:
            scrambled = "".join(random.sample(word, len(word)))

        print("\nScrambled word:", scrambled)
        print("Hint:", hint)

        answer = input("Your guess: ").lower().strip()

        if answer == word:
            print("Correct!")
            round_score += 1
        else:
            print("Incorrect! The correct word was:", word)

    total_score += round_score

    print("\n================================")
    print("          ROUND RESULTS")
    print("================================")
    print("Your score:", round_score, "/ 5")

    if round_number < 2:
        play_again = input("\nWould you like to try another round? (yes/no): ").lower().strip()

        if play_again != "yes":
            break
    else:
        print("\nYou have completed all 15 words!")

print("\n================================")
print("          FINAL RESULTS")
print("================================")
print("Your total score:", total_score, "/", (round_number + 1) * 5)

print("\nReturning to Main Menu...")
