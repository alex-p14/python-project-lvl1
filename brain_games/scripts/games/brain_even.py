#!usr/bin/env python3
from random import randint
from brain_games.general_logic import check_user_answer
from brain_games.general_logic import ask_question
from brain_games.general_logic import welcome_user
from brain_games.general_logic import finish_the_game


def is_even_number(num):
    return num % 2 == 0


def get_right_answer(question):
    if is_even_number(question):
        answer = "yes"
    else:
        answer = "no"
    return answer


def begin_brain_even(user_name, num_of_repeat=1):
    if num_of_repeat > 3:
        finish_the_game(user_name)
    else:
        random_num = randint(1, 100)
        user_answer = ask_question(random_num)
        right_answer = get_right_answer(random_num)
        if check_user_answer(user_answer, right_answer, user_name):
            num_of_repeat += 1
            return begin_brain_even(user_name, num_of_repeat)


def main():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    begin_brain_even(user_name)


if __name__ == 'main':
    main()
