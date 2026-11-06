import random

questions = [
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "How many continents are there?",
        "options": ["A. Five", "B. Six", "C. Seven", "D. Eight"],
        "answer": "C"
    },
    {
        "question": "Which language is mainly used for web page structure?",
        "options": ["A. Python", "B. HTML", "C. Java", "D. C++"],
        "answer": "B"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["A. Seoul", "B. Beijing", "C. Bangkok", "D. Tokyo"],
        "answer": "D"
    },
    {
        "question": "What does AI stand for?",
        "options": ["A. Artificial Intelligence", "B. Automated Internet", "C. Advanced Information", "D. Artificial Integration"],
        "answer": "A"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
        "answer": "C"
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["A. Five", "B. Six", "C. Seven", "D. Eight"],
        "answer": "B"
    },
    {
        "question": "Which animal is known as the King of the Jungle?",
        "options": ["A. Tiger", "B. Elephant", "C. Leopard", "D. Lion"],
        "answer": "D"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["A. Carbon dioxide", "B. Oxygen", "C. Nitrogen", "D. Hydrogen"],
        "answer": "A"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Pablo Picasso", "B. Vincent van Gogh", "C. Leonardo da Vinci", "D. Michelangelo"],
        "answer": "C"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A. 0", "B. 1", "C. 3", "D. 2"],
        "answer": "D"
    },
    {
        "question": "Which country is famous for the Eiffel Tower?",
        "options": ["A. Italy", "B. France", "C. Spain", "D. Germany"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A. Ag", "B. Fe", "C. Au", "D. Go"],
        "answer": "C"
    },
    {
        "question": "How many players are on the field for one football team during a standard match?",
        "options": ["A. 11", "B. 10", "C. 12", "D. 9"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Saturn", "C. Mercury", "D. Mars"],
        "answer": "D"
    }
]

random.shuffle(questions)

total_score = 0

for round_number in range(3):
    round_score = 0

    print("\n================================")
    print("          QUIZ ROUND", round_number + 1)
    print("================================")

    for question in questions[round_number * 5:(round_number + 1) * 5]:
        print("\n" + question["question"])

        for option in question["options"]:
            print(option)

        answer = input("\nYour answer: ").upper().strip()

        while answer not in ["A", "B", "C", "D"]:
            print("Invalid choice! Please enter A, B, C or D.")
            answer = input("Your answer: ").upper().strip()

        if answer == question["answer"]:
            print("Correct!")
            round_score += 1
        else:
            print("Incorrect! The correct answer is", question["answer"])

    total_score += round_score

    print("\n================================")
    print("          ROUND RESULTS")
    print("================================")
    print("Your score:", round_score, "/ 5")

    if round_number < 2:
        play_again = input("\nWould you like to try another quiz? (yes/no): ").lower().strip()

        if play_again != "yes":
            break
    else:
        print("\nYou have completed all 15 questions!")

print("\n================================")
print("          FINAL RESULTS")
print("================================")
print("Your total score:", total_score, "/ 15")

print("\nReturning to Main Menu...")
