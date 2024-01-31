
#"What structure has 2 helises?"
#"What is the main ingredient of DNA in context of chemical compounds?"
#"Which has fastest source of energy?"


answers = (
    ("1.DNA", "2.RNA", "3.cDNA"),
    ("1.Carbon", "2.Oxygen", "3.Phosphor"),
    ("1.Protein", "2.Carbohydrates", "3.Lipids"),
)

def check_first_question(answers):
    answer_one = int(input(f"Welcome to miniQuizz! Choose the correct answer by selecting 1-3 for the question: What structure has 2 helices? {answers[0][0]}, {answers[0][1]}, {answers[0][2]}"))
    if answer_one == 1:
        print(f"yes, {answers[0][0]} is a double-stranded gene structure")
    elif answer_one == 2:
        print(f"no, {answers[0][1]} has a single-stranded structure")
    elif answer_one == 3:
        print(f"no, {answers[0][2]} is not correct")




def check_second_question(answers):
    answer_two = int(input(f"What is the main ingredient of DNA in context of chemical compounds? {answers[1][0]}, {answers[1][1]}, {answers[1][2]}"))
    if answer_two == 1:
        print(f"no, {answers[1][0]} is wrong")
    elif answer_two == 2:
        print(f"no, {answers[1][1]} there is very little oxygen")
    elif answer_two == 3:
        print(f"yes, {answers[1][2]} is correct")
        
check_first_question(answers)
check_second_question(answers)