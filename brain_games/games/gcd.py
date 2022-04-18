import random


def get_description():
    return 'Find the greatest common divisor of given numbers.'


def find_gcd(num_1, num_2):
    if num_2 == 0:
        return num_1
    return find_gcd(num_2, num_1 % num_2)


def find_larged_num(num_1, num_2):
    if num_1 >= num_2:
        return num_1, num_2
    return num_2, num_1


def get_gcd(num_1, num_2):
    max_num, min_num = find_larged_num(num_1, num_2)
    result = find_gcd(max_num, min_num)
    return str(result)


def get_question_and_answer():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    question = f"{num_1} {num_2}"
    answer = get_gcd(num_1, num_2)
    return question, answer
