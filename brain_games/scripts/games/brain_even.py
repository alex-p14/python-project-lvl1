#!usr/bin/env python3
from random import randint
from brain_games.general_logic import check_user_answer
from brain_games.general_logic import ask_question
from brain_games.general_logic import welcome_user
from brain_games.general_logic import the_end


def is_even_num(num):
    if num % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return answer


def brain_even(user_name, num_of_repeat=1):
    if num_of_repeat > 3:
        the_end(user_name)
    else:
        random_num = randint(1, 100)
        right_answer = is_even_num(random_num)
        user_answer = ask_question(random_num)
        if check_user_answer(user_answer, right_answer, user_name):
            num_of_repeat += 1
            return brain_even(user_name, num_of_repeat)


def main():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    brain_even(user_name)


if __name__ == 'main':
    main()
