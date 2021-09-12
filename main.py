from questions import Question


question_prompt = [
    "What is Dead By Daylight?\n(a) A bad time\n(b) A video game\n(c) A cereal\n\n",
    "Which one of these is a killer?\n(a) Claudette\n(b) Ji-Woon\n(c) Dwight\n\n",
    "What is dead-hard?\n(a) A perk\n(b) A console destroyer\n(c) Both\n\n",
]
questions = [
    Question(question_prompt[0], "b"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "c"),
]
#The (questions) is a list of questions that wanna ask user. wanna loop through each one and see if right

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct!")


run_test(questions)
