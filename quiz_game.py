questions = [
    {
        "q": "What is the capital of India?",
        "options": ["A) Mumbai", "B) New Delhi", "C) Kolkata", "D) Chennai"],
        "answer": "B"
    },
    {
        "q": "Which language is used to structure web pages?",
        "options": ["A) Python", "B) C++", "C) HTML", "D) Java"],
        "answer": "C"
    },
    {
        "q": "Which data type stores True or False values in Python?",
        "options": ["A) int", "B) bool", "C) str", "D) float"],
        "answer": "B"
    },
    {
        "q": "Which keyword is used to define a function in Python?",
        "options": ["A) function", "B) define", "C) fun", "D) def"],
        "answer": "D"
    },
    {
        "q": "What does CPU stand for?",
        "options": [
            "A) Central Processing Unit",
            "B) Computer Personal Unit",
            "C) Central Program Utility",
            "D) Control Processing User"
        ],
        "answer": "A"
    },
    {
        "q": "Which data structure follows LIFO?",
        "options": ["A) Queue", "B) Array", "C) Stack", "D) Linked list"],
        "answer": "C"
    },
    {
        "q": "Which operator checks equality in Python?",
        "options": ["A) =", "B) ==", "C) !=", "D) :="],
        "answer": "B"
    },
    {
        "q": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Jupiter", "C) Saturn", "D) Mars"],
        "answer": "D"
    },
    {
        "q": "Which loop is commonly used to iterate over a list in Python?",
        "options": ["A) for", "B) switch", "C) case", "D) goto"],
        "answer": "A"
    },
    {
        "q": "What is the binary representation of decimal 5?",
        "options": ["A) 100", "B) 110", "C) 101", "D) 111"],
        "answer": "C"
    }
]
score = 0
for i, question in enumerate(questions, start=1):
    print(f"Q{i}: {question['q']}")
    for option in question["options"]:
        print(option)

    user = input("Your answer (A/B/C/D): ").upper()
    if user == question["answer"]:
        print("correct! \n")
        score += 1
    else:
        print(f"Wrong! Correct answer: {question["answer"]}\n")
print(f"final score: {score}/{len(questions)}")
