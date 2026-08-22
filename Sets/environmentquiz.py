#Environment Quiz Game

questions = [
    {
        "question": "1. Which of these help reduce pollution?",
        "options": ["a) Planting trees", "b) Burning plastic", "c) Using bicycles", "d) Wasting water"],
        "correct":{"a","c"}
    },
    {
            "question": "2. Which are renewable energy sources?",
            "options": ["a) Solar energy", "b) Coal", "c) Wind energy", "d) Petrol"],
            "correct":{"a","c"}
    },
    {
            "question": "3. What actions save water?",
            "options": ["a) Fixing leaks", "b) Leaving tap running", "c) Using buckets for bathing", "d) Overwatering plants"],
            "correct":{"a","c"}
    },
    {
            "question": "4. Which items can be recycled?",
            "options": ["a) Paper", "b) Plastic bottles", "c) Glass", "d) Food waste"],
            "correct":{"a","b", "c"}
    },
    {
            "question": "5. Which helps protect wildlife?",
            "options": ["a) Destroying forests", "b) Creating sanctuaries", "c) Avoiding plastic", "d) Hunting animals"],
            "correct":{"b","c"}
    }

]

score = 0

print("Welcome to the  Environmental Protection Quiz!")
print("Choose the correct options (example: a c) \n")

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
        print("Perfect! \n")
        score += 1
    else:
        print("You got these right: ", user_set & correct_set)
        print("Wrong choices: ", user_set - correct_set)
        print("Missed: ", correct_set - user_set, "\n")

print("Final Score:", score, "/", len(questions))

if score == len(questions):
    print("Eco Hero! You know your planet well!")
elif score >=3:
    print("Good job! Keep learning to protect Earth!")
else:
    print("Lets do better for our planet!")
