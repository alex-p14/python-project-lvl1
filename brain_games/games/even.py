import random


def get_description():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_right_answer(question):
    return "no" if question % 2 else "yes"


def get_question_and_answer():
    question = random.randint(1, 100)
    answer = get_right_answer(question)
    return question, answer
