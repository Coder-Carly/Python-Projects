#Computer Science & Coding Quiz!

questions = [
    {
        "question": "1. What does CPU stand for?",
        "options": ["a) Computer Personal Unit", "b) Central Program Unit", "c) Cone Processor Unit", "d) Central Processing Unit"],
        "correct":{"d"}
    },
    {
            "question": "2. Which of these are programming languages?",
            "options": ["a) Windows", "b) Java", "c) Python", "d) Google"],
            "correct":{"b","c"}
    },
    {
            "question": "3. What is a variable used for in programming?",
            "options": ["a) To store data or a value", "b) To connect a computer to Wi-Fi", "c) To delete code", "d) To make a computer run faster"],
            "correct":{"a"}
    },
    {
            "question": "4. Which of these are input devices?",
            "options": ["a) Speaker", "b) Monitor", "c) Keyboard", "d) Mouse"],
            "correct":{"c","d"}
    },
    {
            "question": "5. What is an algorithm?",
            "options": ["a) A type of computer virus", "b) A set of instructions used to solve a problem or complete a task", "c) A programming language", "d) A piece of computer hardware"],
            "correct":{"b"}
    }

]

score = 0

print("Welcome to the Computer Science and Programming Quiz!")
print("Choose the correct option(s) (example: a c) \n")

for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)

    user_input = input("Your answer: ").lower().split()
    user_set = set(user_input)

    correct_set = q["correct"]

    print("Correct answers: ", correct_set)

    #Using set operations
    if user_set == correct_set:
        print("Perfect answer! \n")
        score += 1
    else:
        print("Correct choices: ", user_set & correct_set)
        print("Wrong choices: ", user_set - correct_set)
        print("Missed: ", correct_set - user_set, "\n")

print("Final Score:", score, "/", len(questions))

if score == len(questions):
    print("Tech Genius! You know your computers well!")
elif score >=3:
    print("Well done! Keep learning to know your way around computers!")
else:
    print("Lets learn more in preparation to the AI ERA!")
