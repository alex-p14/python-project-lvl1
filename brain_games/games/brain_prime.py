#!usr/bin/env python3
from random import randint
from brain_games.general_logic import (
    check_user_answer,
    ask_question,
    welcome_user,
    finish_the_game
)


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


def begin_brain_prime(user_name, num_of_repeat=1):
    if num_of_repeat > 3:
        finish_the_game(user_name)
    else:
        random_num = randint(1, 100)
        user_answer = ask_question(random_num)
        right_answer = get_right_answer(random_num)
        if check_user_answer(user_answer, right_answer, user_name):
            num_of_repeat += 1
            return begin_brain_prime(user_name, num_of_repeat)


def main():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    begin_brain_prime(user_name)


if __name__ == 'main':
    main()
