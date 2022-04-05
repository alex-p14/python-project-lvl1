import random


def get_description():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_square_number(num):
    return num * num


def is_divided_number(num_1, num_2):
    result = num_1 % num_2
    return result == 0


def find_smallest_divisor(num, divisor=2):
    if get_square_number(divisor) > num:
        return num
    elif is_divided_number(num, divisor):
        return divisor
    else:
        divisor += 1
        return find_smallest_divisor(num, divisor)


def is_prime_number(num):
    return find_smallest_divisor(num) == num


def get_right_answer(question):
    if is_prime_number(question):
        answer = "yes"
    else:
        answer = "no"
    return answer


def get_question_and_answer():
    num = random.randint(1, 100)
    question = str(num)
    answer = get_right_answer(num)
    return question, answer
