import random
import operator


def get_description():
    return 'What is the result of the expression?'


def get_question_and_answer():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    operation = random.choice(list(operations.keys()))
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    question = f"{num_1} {operation} {num_2}"
    answer = str(operations[operation](num_1, num_2))
    return question, answer
