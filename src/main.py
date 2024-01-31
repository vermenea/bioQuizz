from questions import questions

def show_question(question_base):
    print("\n" + question_base["question"])
    for q, option in enumerate(question_base["options"], start=1):
        print(f"{q}. {option}")
    user_answer = int(input("Choose the correct answer by entering 1-3: "))
    return user_answer == question_base["options"].index(question_base["correct_answer"]) + 1

def quizz():
    score = 0
    proceed = input(f"Hello! Welcome to the short bioQuizz. If you're ready, press 'y' to continue: ")
    if proceed.lower() == "y":
        for question_data in questions:
            if show_question(question_data):
                print(f"Correct! {question_data['correct_answer']} is the right answer.")
                score += 1
            else:
                print(f"Sorry, the correct answer is {question_data['correct_answer']}")

        print(f"You scored {score} out of {len(questions)}!")
    else:
        print("Okay then :(, may we see eachother soon <3")

quizz()
