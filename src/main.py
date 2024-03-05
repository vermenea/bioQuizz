import tkinter as tk
from tkinter import messagebox
from questions import questions

def show_question(question_base, radio_buttons, radio_var, question_label):
    question_label.config(text=question_base["question"])
    for i, radio_button in enumerate(radio_buttons):
        radio_button.config(text=question_base["options"][i])
    radio_var.set(0)

def submit_answer(question_data, user_answer, score_label, current_question, radio_buttons, question_label, radio_var):
    correct_answer = question_data["correct_answer"]

    if correct_answer == question_data["options"][user_answer - 1]:
        messagebox.showinfo("Correct!", f"Correct! {question_data['options'][user_answer - 1]} is the right answer.")
        score_label.config(text=f"Score: {int(score_label.cget('text').split(': ')[-1]) + 1}")
    else:
        messagebox.showinfo("Incorrect", f"Sorry, the correct answer is {correct_answer}")

    current_question[0] += 1
    if current_question[0] < len(questions):
        show_question(questions[current_question[0]], radio_buttons, radio_var, question_label)
    else:
        messagebox.showinfo("Quiz Finished", f"You scored {int(score_label.cget('text').split(': ')[-1])} out of {len(questions)}!")


def quizz():
    root = tk.Tk()
    root.title("BioQuizz")

    question_label = tk.Label(root, text="")
    question_label.pack()

    radio_var = tk.IntVar()

    radio_buttons = []
    for i in range(3):
        radio_button = tk.Radiobutton(root, text="", variable=radio_var, value=i + 1)
        radio_buttons.append(radio_button)
        radio_button.pack()

    score_label = tk.Label(root, text="Score: 0")
    score_label.pack()

    current_question = [0]

    show_question(questions[current_question[0]], radio_buttons, radio_var, question_label)

    submit_button = tk.Button(root, text="Submit", command=lambda: submit_answer(
        questions[current_question[0]], radio_var.get(), score_label, current_question, radio_buttons, question_label, radio_var
    ))
    submit_button.pack()
    
    submit_button.configure(
    background="blue",  
    foreground="white",  
    font=("Helvetica", 10),  
    width=5,  
    height=1,  
    bd=2, 
)

    root.mainloop()

if __name__ == "__main__":
    quizz()
