import random


def get_description():
    return 'What number is missing in the progression?.'


def get_question_and_answer():
    amount_nums = random.randint(6, 10)
    first_num = random.randint(1, 100)
    step = random.randint(2, 9)
    hidden_element = random.randint(0, amount_nums - 1)
    progression = list(range(first_num, (first_num + step * amount_nums), step))
    answer, progression[hidden_element] = str(progression[hidden_element]), '..'
    question = ' '.join(map(str, progression))
    return question, answer
