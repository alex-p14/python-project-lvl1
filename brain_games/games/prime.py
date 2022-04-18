import random


def get_description():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def find_smallest_divisor(num, divisor=2):
    if divisor ** 2 > num:
        return num
    elif num % divisor == 0:
        return divisor
    return find_smallest_divisor(num, divisor + 1)


def is_prime_number(num):
    if num == 1:
        return False
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
