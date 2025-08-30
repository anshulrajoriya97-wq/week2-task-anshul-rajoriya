import json

def load_questions():
    with open("quiz_questions.json", "r") as f:
        return json.load(f)

def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")
        answer = int(input("Your answer (1-4): "))
        if q["options"][answer-1].lower() == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['answer']}")
    print(f"\nFinal Score: {score}/{len(questions)}")

def main():
    questions = load_questions()
    run_quiz(questions)

if __name__ == "__main__":
    main()
