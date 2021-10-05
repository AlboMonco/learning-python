from classes import Questions
questions_prompts = [
    "What is the color of the moon?\n(a) White\n(b) Red\n(c) Blue\n(d) Yellow\n",
    "What is the color of the sky when it is raining?\n(a) Red\n(b) Black\n(c) Grey\n(d) Blue\n"

]

questions = [
    Questions(questions_prompts[0], "a"),
    Questions(questions_prompts[1], "c")
]

def run_test():
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    return "You got {}/{} questions".format(score,len(questions))


if __name__ == "__main__":
    print(run_test())
    

