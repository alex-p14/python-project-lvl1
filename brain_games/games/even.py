import random


def get_description():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_number(num):
    return num % 2 == 0


def get_right_answer(question):
    if is_even_number(question):
        return "yes"
    else:
        return "no"


def get_question_and_answer():
    question = random.randint(1, 100)
    answer = get_right_answer(question)
    return question, answer
