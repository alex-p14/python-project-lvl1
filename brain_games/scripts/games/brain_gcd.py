#!usr/bin/env python3
from random import randint
from brain_games.general_logic import check_user_answer
from brain_games.general_logic import ask_question
from brain_games.general_logic import welcome_user
from brain_games.general_logic import the_end


def get_remainder(num_1, num_2):
    return num_1 % num_2


def find_gcd(num_1, num_2):
    if num_2 == 0:
        return num_1
    else:
        return find_gcd(num_2, get_remainder(num_1, num_2))


def find_larged_num(num_1, num_2):
    if num_1 >= num_2:
        return (num_1, num_2)
    else:
        return (num_2, num_1)


def get_gcd(num_1, num_2):
    (max_num, min_num) = find_larged_num(num_1, num_2)
    result = find_gcd(max_num, min_num)
    return str(result)


def brain_gcd(user_name, num_of_repeat=1):
    if num_of_repeat > 3:
        the_end(user_name)
    else:
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        question = f"{num_1} {num_2}"
        user_answer = ask_question(question)
        right_answer = get_gcd(num_1, num_2)
        if check_user_answer(user_answer, right_answer, user_name):
            num_of_repeat += 1
            return brain_gcd(user_name, num_of_repeat)


def main():
    user_name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    brain_gcd(user_name)


if __name__ == 'main':
    main()
